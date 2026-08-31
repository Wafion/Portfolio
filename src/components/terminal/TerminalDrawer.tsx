"use client";

import React, { useState, useEffect, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, Terminal as TerminalIcon, CornerDownLeft } from "lucide-react";
import { sound } from "@/components/audio/SoundEngine";
import {
  COMMANDS,
  findCommand,
  handleGameState,
  checkCommandSequence,
  type CommandLogEntry,
  type SecretState,
  type GameState,
} from "./commands";

interface TerminalDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectProject?: (slug: string) => void;
}

const INITIAL_SECRETS: SecretState = {
  secretFound: false,
  archiveFragments: [],
  cipherKeyFound: false,
  fifthExitClueFound: false,
  fifthExitTriggered: false,
  iraFound: false,
  sequenceDetected: false,
};

const INITIAL_GAME: GameState = {
  phase: "idle",
  round: 0,
  score: 0,
  target: 0,
  attempts: 0,
  history: [],
};

const BOOT_LINES = [
  { text: "YASH.OS v2.6.4", delay: 0 },
  { text: "KERNEL: CUSTOM BUILD", delay: 80 },
  { text: "INITIALIZING HIDDEN LAYER...", delay: 200 },
  { text: "ARCHIVE INDEXED.", delay: 380 },
  { text: "CIPHER ENGINE: ACTIVE", delay: 520 },
  { text: "TYPE 'help' TO SEE AVAILABLE COMMANDS.", delay: 700 },
];

export function TerminalDrawer({
  isOpen,
  onClose,
  onSelectProject,
}: TerminalDrawerProps) {
  const [input, setInput] = useState("");
  const [history, setHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState<number>(-1);
  const [logs, setLogs] = useState<CommandLogEntry[]>([]);
  const [booting, setBooting] = useState(true);
  const [secrets, setSecrets] = useState<SecretState>(INITIAL_SECRETS);
  const [gameState, setGameState] = useState<GameState>(INITIAL_GAME);
  const [commandCount, setCommandCount] = useState(0);
  const openTimeRef = useRef(Date.now());
  const inputRef = useRef<HTMLInputElement | null>(null);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  /* ── Boot sequence ────────────────────────────────────── */
  useEffect(() => {
    if (!isOpen) {
      setBooting(true);
      setLogs([]);
      setInput("");
      setHistory([]);
      setHistoryIndex(-1);
      setCommandCount(0);
      setSecrets(INITIAL_SECRETS);
      setGameState(INITIAL_GAME);
      openTimeRef.current = Date.now();
      return;
    }

    // Run boot animation
    setBooting(true);
    setLogs([]);
    const timers: ReturnType<typeof setTimeout>[] = [];

    BOOT_LINES.forEach((line, i) => {
      timers.push(
        setTimeout(() => {
          setLogs((prev) => [
            ...prev,
            {
              id: `boot-${i}`,
              type: "system" as const,
              content: line.text,
            },
          ]);
        }, line.delay)
      );
    });

    timers.push(
      setTimeout(() => {
        setBooting(false);
        setTimeout(() => inputRef.current?.focus(), 50);
      }, BOOT_LINES[BOOT_LINES.length - 1].delay + 200)
    );

    return () => timers.forEach(clearTimeout);
  }, [isOpen]);

  /* ── Auto-scroll ──────────────────────────────────────── */
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  /* ── Escape to close ──────────────────────────────────── */
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) {
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  /* ── Context object for commands ──────────────────────── */
  const ctx = useCallback(
    () => ({
      addLogs: (newLogs: CommandLogEntry[]) =>
        setLogs((prev) => [...prev, ...newLogs]),
      setLogs,
      onClose,
      onSelectProject: onSelectProject || (() => {}),
      scrollToSection: (id: string) => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      },
      history,
      openTime: openTimeRef.current,
      commandCount,
      secrets,
      setSecrets,
      gameState,
      setGameState,
      checkSequence: (cmd: string) => {
        // Will be called after command execution
      },
    }),
    [history, commandCount, secrets, gameState, onClose, onSelectProject]
  );

  /* ── Command execution ────────────────────────────────── */
  const executeCommand = useCallback(
    (rawCmd: string) => {
      const trimmed = rawCmd.trim();
      if (!trimmed) return;
      if (booting) return;

      sound.playSoftClick(400);

      const newHistory = [...history, trimmed];
      setHistory(newHistory);
      setHistoryIndex(-1);
      setCommandCount((c) => c + 1);

      const context = ctx();

      const inputLog: CommandLogEntry = {
        id: `in-${Date.now()}`,
        type: "input",
        content: `$ ${trimmed}`,
      };

      // Check if game is active
      if (gameState.phase === "playing") {
        const gameInput = trimmed.toLowerCase();
        if (gameInput === "quit" || gameInput === "exit") {
          setGameState((prev) => ({ ...prev, phase: "idle" }));
          setLogs((prev) => [...prev, inputLog, { id: `sys-${Date.now()}`, type: "system", content: "Game aborted." }]);
          setInput("");
          return;
        }
        const guess = parseInt(trimmed, 10);
        if (!isNaN(guess) && guess >= 1 && guess <= 50) {
          const result = handleGameState(trimmed, context);
          setLogs((prev) => [...prev, inputLog, ...result]);
          setInput("");
          return;
        }
        // Not a valid game input — still show it
        const result = handleGameState(trimmed, context);
        setLogs((prev) => [...prev, inputLog, ...result]);
        setInput("");
        return;
      }

      // Normal command lookup
      const found = findCommand(trimmed);
      if (found) {
        const result = found.command.execute(found.args, context);
        if (result.length > 0) {
          setLogs((prev) => [...prev, inputLog, ...result]);
        } else {
          setLogs((prev) => [...prev, inputLog]);
        }
      } else {
        // Unknown command
        setLogs((prev) => [
          ...prev,
          inputLog,
          {
            id: `err-${Date.now()}`,
            type: "error",
            content: (
              <div className="text-[11px]">
                <p>UNKNOWN COMMAND</p>
                <p className="text-[#7A7874] mt-1">Input: {trimmed}</p>
                <p className="text-[#7A7874]">Suggestion: help</p>
              </div>
            ),
          },
        ]);
      }

      // Check for hidden sequence triggers
      const seqResult = checkCommandSequence(newHistory, context);
      if (seqResult) {
        setTimeout(() => {
          setLogs((prev) => [...prev, seqResult]);
        }, 300);
      }

      setInput("");
    },
    [booting, history, gameState, ctx]
  );

  /* ── Keyboard handler ─────────────────────────────────── */
  const handleKeyDownInput = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      executeCommand(input);
    } else if (e.key === "ArrowUp") {
      if (history.length > 0) {
        const nextIndex =
          historyIndex + 1 < history.length ? historyIndex + 1 : historyIndex;
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
                <span className="text-[10px] text-[#7A7874] tracking-wider">
                  TERMINAL
                </span>
                {secrets.fifthExitTriggered && (
                  <span className="text-[9px] text-[#C4565A] animate-pulse">
                    ■ ARCHIVE COMPLETE
                  </span>
                )}
              </div>
              <div className="flex items-center gap-2">
                <span className="text-[9px] text-[#7A7874]">
                  {commandCount > 0 && `${commandCount} cmds · `}
                  ESC to close
                </span>
                <button
                  onClick={onClose}
                  className="p-1 text-[#7A7874] hover:text-[#F2F0EA] transition-colors"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Output */}
            <div
              ref={scrollRef}
              className="flex-1 p-4 overflow-y-auto space-y-3 leading-relaxed"
            >
              {logs.map((log) => (
                <div key={log.id}>
                  {log.type === "input" && (
                    <div className="text-[#D4C87A] font-semibold text-[11px]">
                      {log.content}
                    </div>
                  )}
                  {log.type === "output" && (
                    <div className="text-[#B8B6AF] pl-2">{log.content}</div>
                  )}
                  {log.type === "system" && (
                    <div className="text-[#5BAA8A]/80 whitespace-pre-wrap pl-2 border-l border-[#5BAA8A]/20">
                      {log.content}
                    </div>
                  )}
                  {log.type === "error" && (
                    <div className="text-[#C4565A] pl-2 text-[11px]">
                      ! {log.content}
                    </div>
                  )}
                  {log.type === "cipher" && <div className="pl-2">{log.content}</div>}
                  {log.type === "secret" && (
                    <div className="pl-2 border-l border-[#D4C87A]/20">{log.content}</div>
                  )}
                  {log.type === "game" && (
                    <div className="pl-2 border-l border-[#5BAA8A]/20">{log.content}</div>
                  )}
                </div>
              ))}
            </div>

            {/* Input */}
            <div className="flex items-center gap-2 px-4 py-3 border-t border-[#F2F0EA]/[0.04]">
              <span className="text-[#D4C87A] font-bold text-[11px]">$</span>
              <input
                ref={inputRef}
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDownInput}
                placeholder={
                  booting
                    ? "Initializing..."
                    : gameState.phase === "playing"
                      ? "Enter your guess (1-50)..."
                      : "help, projects, cipher <text>..."
                }
                className="flex-1 bg-transparent text-[#F2F0EA] placeholder-[#7A7874]/40 outline-none font-mono text-xs"
                autoFocus
                disabled={booting}
              />
              <button
                onClick={() => executeCommand(input)}
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
