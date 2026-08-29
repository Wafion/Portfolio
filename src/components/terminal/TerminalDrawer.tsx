"use client";

import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, Terminal as TerminalIcon, CornerDownLeft } from "lucide-react";
import { sound } from "@/components/audio/SoundEngine";
import { EXHIBITION_PROJECTS } from "@/lib/data/projects";
import { encodeText } from "@/lib/data/cipher";
import { GlyphSymbol } from "@/components/ui/GlyphSymbol";

interface TerminalDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectProject?: (slug: string) => void;
}

interface CommandLog {
  id: string;
  type: "input" | "output" | "error" | "system" | "cipher";
  content: string | React.ReactNode;
}

export function TerminalDrawer({ isOpen, onClose, onSelectProject }: TerminalDrawerProps) {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState<number>(-1);
  const [logs, setLogs] = useState<CommandLog[]>([
    {
      id: "init",
      type: "system",
      content: "Hidden layer activated.\nType 'help' to see available commands.",
    },
  ]);
  const inputRef = useRef<HTMLInputElement | null>(null);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  }, [isOpen]);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) {
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  const handleCommand = (rawCmd: string) => {
    const trimmed = rawCmd.trim();
    if (!trimmed) return;

    sound.playSoftClick(400);
    setHistory((prev) => [...prev, trimmed]);
    setHistoryIndex(-1);

    const newLogs: CommandLog[] = [
      ...logs,
      { id: `in-${Date.now()}`, type: "input", content: `$ ${trimmed}` },
    ];

    const args = trimmed.split(" ");
    const cmd = args[0].toLowerCase();
    const param = args.slice(1).join(" ");

    switch (cmd) {
      case "help":
      case "?":
        newLogs.push({
          id: `out-${Date.now()}`,
          type: "output",
          content: (
            <div className="space-y-1 text-xs text-white/80">
              <p className="text-[#B8B6AF] font-semibold mb-1">COMMANDS:</p>
              <div className="grid grid-cols-[120px_1fr] gap-1 text-[11px]">
                <span className="text-[#D4C87A]">projects</span>
                <span className="text-[#7A7874]">List all projects</span>
                <span className="text-[#D4C87A]">open &lt;slug&gt;</span>
                <span className="text-[#7A7874]">Open case study (e.g. open page-os)</span>
                <span className="text-[#D4C87A]">cipher &lt;text&gt;</span>
                <span className="text-[#7A7874]">Encode text to glyphs</span>
                <span className="text-[#D4C87A]">about</span>
                <span className="text-[#7A7874]">About me</span>
                <span className="text-[#D4C87A]">clear</span>
                <span className="text-[#7A7874]">Clear terminal</span>
                <span className="text-[#D4C87A]">close</span>
                <span className="text-[#7A7874]">Close terminal</span>
              </div>
            </div>
          ),
        });
        break;

      case "projects":
      case "ls":
        newLogs.push({
          id: `out-${Date.now()}`,
          type: "output",
          content: (
            <div className="space-y-1.5 text-xs">
              {EXHIBITION_PROJECTS.map((p) => (
                <div key={p.id} className="flex items-center justify-between border-b border-white/5 pb-1">
                  <span className="text-[#B8B6AF]">
                    <span className="text-[#4A90D9] font-bold">{p.slug}</span>
                    <span className="text-[#7A7874] ml-2">[{p.domain}]</span>
                  </span>
                  <button
                    onClick={() => {
                      onSelectProject?.(p.slug);
                      onClose();
                    }}
                    className="text-[#D4C87A] hover:text-[#D4C87A]/80 text-[10px] underline"
                  >
                    open
                  </button>
                </div>
              ))}
            </div>
          ),
        });
        break;

      case "open":
      case "inspect":
        if (!param) {
          newLogs.push({
            id: `err-${Date.now()}`,
            type: "error",
            content: "Usage: open <slug>. Try: open page-os",
          });
        } else {
          const match = EXHIBITION_PROJECTS.find(
            (p) => p.slug.toLowerCase() === param.toLowerCase()
          );
          if (match) {
            onSelectProject?.(match.slug);
            onClose();
          } else {
            newLogs.push({
              id: `err-${Date.now()}`,
              type: "error",
              content: `Project '${param}' not found.`,
            });
          }
        }
        break;

      case "cipher":
        if (!param) {
          newLogs.push({
            id: `err-${Date.now()}`,
            type: "error",
            content: "Usage: cipher <text>. Example: cipher HELLO",
          });
        } else {
          const glyphs = encodeText(param.toUpperCase());
          glyphs.forEach((_, i) => {
            setTimeout(() => sound.playCipherChirp(0.7 + i * 0.05), i * 40);
          });
          newLogs.push({
            id: `cipher-${Date.now()}`,
            type: "cipher",
            content: (
              <div className="space-y-2 p-2 rounded border border-[#D4C87A]/20">
                <div className="text-[10px] text-[#D4C87A] font-mono">
                  &quot;{param.toUpperCase()}&quot;
                </div>
                <div className="flex flex-wrap gap-2 items-center">
                  {param.split("").map((c, i) => (
                    <div key={i} className="flex flex-col items-center gap-0.5 p-1 rounded">
                      <GlyphSymbol char={c} size={20} color="#D4C87A" />
                      <span className="text-[8px] text-[#7A7874]">{c.toUpperCase()}</span>
                    </div>
                  ))}
                </div>
              </div>
            ),
          });
        }
        break;

      case "about":
        newLogs.push({
          id: `out-${Date.now()}`,
          type: "output",
          content: (
            <div className="space-y-2 text-xs border-l border-[#F2F0EA]/10 pl-3">
              <p className="font-serif italic text-sm text-[#B8B6AF]">
                &ldquo;I like taking things apart. Machines. Software. Stories. Interfaces. Systems.
                Then I try to understand what makes them work.&rdquo;
              </p>
            </div>
          ),
        });
        break;

      case "clear":
      case "cls":
        setLogs([]);
        setInput("");
        return;

      case "close":
      case "exit":
        onClose();
        setInput("");
        return;

      default:
        newLogs.push({
          id: `err-${Date.now()}`,
          type: "error",
          content: `Unknown command: '${trimmed}'. Type 'help'.`,
        });
        break;
    }

    setLogs(newLogs);
    setInput("");
  };

  const handleKeyDownInput = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleCommand(input);
    } else if (e.key === "ArrowUp") {
      if (history.length > 0) {
        const nextIndex = historyIndex + 1 < history.length ? historyIndex + 1 : historyIndex;
        setHistoryIndex(nextIndex);
        setInput(history[history.length - 1 - nextIndex]);
      }
    } else if (e.key === "ArrowDown") {
      if (historyIndex > 0) {
        setHistoryIndex(historyIndex - 1);
        setInput(history[history.length - 1 - (historyIndex - 1)]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setInput("");
      }
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-8">
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="absolute inset-0 bg-[#050505]/85 backdrop-blur-2xl"
          />

          <motion.div
            initial={{ opacity: 0, scale: 0.97, y: 15 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.97, y: 15 }}
            transition={{ type: "spring", damping: 30, stiffness: 250 }}
            className="relative w-full max-w-3xl h-[70vh] max-h-[560px] flex flex-col rounded-xl border border-[#F2F0EA]/[0.06] bg-[#0B0B0C] overflow-hidden font-mono text-xs z-10"
          >
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-[#F2F0EA]/[0.04]">
              <div className="flex items-center gap-2">
                <TerminalIcon className="w-3.5 h-3.5 text-[#7A7874]" />
                <span className="text-[10px] text-[#7A7874] tracking-wider">TERMINAL</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-[9px] text-[#7A7874]">ESC to close</span>
                <button
                  onClick={onClose}
                  className="p-1 text-[#7A7874] hover:text-[#F2F0EA] transition-colors"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Output */}
            <div ref={scrollRef} className="flex-1 p-4 overflow-y-auto space-y-3 leading-relaxed">
              {logs.map((log) => (
                <div key={log.id}>
                  {log.type === "input" && (
                    <div className="text-[#D4C87A] font-semibold">{log.content}</div>
                  )}
                  {log.type === "output" && <div className="text-[#B8B6AF] pl-2">{log.content}</div>}
                  {log.type === "system" && (
                    <div className="text-[#5BAA8A]/80 whitespace-pre-wrap pl-2 border-l border-[#5BAA8A]/20">
                      {log.content}
                    </div>
                  )}
                  {log.type === "error" && (
                    <div className="text-[#C4565A] pl-2">! {log.content}</div>
                  )}
                  {log.type === "cipher" && <div className="pl-2">{log.content}</div>}
                </div>
              ))}
            </div>

            {/* Input */}
            <div className="flex items-center gap-2 px-4 py-3 border-t border-[#F2F0EA]/[0.04]">
              <span className="text-[#D4C87A] font-bold">$</span>
              <input
                ref={inputRef}
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDownInput}
                placeholder="help, projects, cipher <text>..."
                className="flex-1 bg-transparent text-[#F2F0EA] placeholder-[#7A7874]/40 outline-none font-mono text-xs"
                autoFocus
              />
              <button
                onClick={() => handleCommand(input)}
                className="p-1.5 rounded text-[#7A7874] hover:text-[#F2F0EA] transition-colors"
              >
                <CornerDownLeft className="w-3.5 h-3.5" />
              </button>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}
