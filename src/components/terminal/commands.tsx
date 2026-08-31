/**
 * YASH.OS TERMINAL 2.0 — Command Registry
 *
 * Extensible command system. Each command is declarative:
 *   name, aliases, description, category, hidden, execute(ctx) => ReactNode
 *
 * Hidden commands do NOT appear in help.
 * Easter eggs are triggered by command sequences or special inputs.
 */

import React from "react";
import { EXHIBITION_PROJECTS } from "@/lib/data/projects";
import { encodeText, decodeCipherText, CIPHER_DICTIONARY } from "@/lib/data/cipher";
import { GlyphSymbol } from "@/components/ui/GlyphSymbol";
import { sound } from "@/components/audio/SoundEngine";

/* ── Types ────────────────────────────────────────────────────── */

export interface TerminalContext {
  /** Append output logs to the terminal */
  addLogs: (logs: CommandLogEntry[]) => void;
  /** Replace all logs */
  setLogs: React.Dispatch<React.SetStateAction<CommandLogEntry[]>>;
  /** Close the terminal */
  onClose: () => void;
  /** Open a project modal */
  onSelectProject: (slug: string) => void;
  /** Smooth scroll to a section */
  scrollToSection: (id: string) => void;
  /** Current command history */
  history: string[];
  /** Terminal open timestamp */
  openTime: number;
  /** Command count this session */
  commandCount: number;
  /** Discovered secrets state */
  secrets: SecretState;
  /** Update secrets */
  setSecrets: React.Dispatch<React.SetStateAction<SecretState>>;
  /** Game state */
  gameState: GameState;
  /** Update game state */
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
  /** Check command sequence triggers */
  checkSequence: (cmd: string) => void;
}

export interface CommandLogEntry {
  id: string;
  type: "input" | "output" | "error" | "system" | "cipher" | "secret" | "game";
  content: string | React.ReactNode;
}

export interface CommandDef {
  name: string;
  aliases: string[];
  description: string;
  category: "CORE" | "NAVIGATION" | "PROJECTS" | "SYSTEM" | "CIPHER" | "UTILITY";
  hidden: boolean;
  execute: (args: string, ctx: TerminalContext) => CommandLogEntry[];
}

export interface SecretState {
  secretFound: boolean;
  archiveFragments: number[];
  cipherKeyFound: boolean;
  fifthExitClueFound: boolean;
  fifthExitTriggered: boolean;
  iraFound: boolean;
  sequenceDetected: boolean;
}

export interface GameState {
  phase: "idle" | "playing" | "won" | "lost";
  round: number;
  score: number;
  target: number;
  attempts: number;
  history: { guess: number; direction: string }[];
}

/* ── Helpers ────────────────────────────────────────────────────── */

let _idCounter = 0;
const makeId = (prefix: string) => `${prefix}-${Date.now()}-${_idCounter++}`;

const out = (content: string | React.ReactNode): CommandLogEntry => ({
  id: makeId("out"),
  type: "output",
  content,
});

const sys = (content: string | React.ReactNode): CommandLogEntry => ({
  id: makeId("sys"),
  type: "system",
  content,
});

const err = (content: string | React.ReactNode): CommandLogEntry => ({
  id: makeId("err"),
  type: "error",
  content,
});

const secret = (content: string | React.ReactNode): CommandLogEntry => ({
  id: makeId("sec"),
  type: "secret",
  content,
});

const game = (content: string | React.ReactNode): CommandLogEntry => ({
  id: makeId("game"),
  type: "game",
  content,
});

const cipher = (content: React.ReactNode): CommandLogEntry => ({
  id: makeId("ciph"),
  type: "cipher",
  content,
});

/** Format a tree-style filesystem display */
function treeBlock(lines: string): React.ReactNode {
  return (
    <pre className="text-[11px] text-[#B8B6AF] leading-relaxed font-mono whitespace-pre">{lines}</pre>
  );
}

/** Status bar renderer */
function statusBar(label: string, status: string, color: string): React.ReactNode {
  return (
    <div className="flex items-center gap-2 text-[11px]">
      <span className="text-[#7A7874] w-36">{label}</span>
      <span className={`font-semibold`} style={{ color }}>{status}</span>
    </div>
  );
}

/* ── Fortune quotes ────────────────────────────────────────────── */

const FORTUNES: { quote: string; source: string }[] = [
  { quote: "Where literature ceases to be a flat page and becomes a searchable, navigable architecture.", source: "PAGE.OS" },
  { quote: "Audio that understands the story with the same nuance as the listener.", source: "ANE" },
  { quote: "Cinema is not about showing everything; it is about crafting the shadow where the imagination lives.", source: "RESIDUAL" },
  { quote: "You did not enter the building. The building materialized around your silence.", source: "THE FIFTH EXIT" },
  { quote: "If the mirror remembers what stood before it yesterday, who is the stranger looking back today?", source: "A ROOM FOR ONE MORE" },
  { quote: "Giving digital vertices the permanence and tactile coldness of carved stone.", source: "3D ART" },
  { quote: "Language is the first machine human beings ever invented.", source: "CIPHER" },
  { quote: "Code is not merely an instruction set; it is a brush with infinite precision.", source: "CREATIVE CODING" },
  { quote: "Software designed for the mind must respect cognitive focus above all else.", source: "PAGE.OS" },
  { quote: "Architecture can be as much of a character in a film as the actor.", source: "THE FIFTH EXIT" },
];

/* ── Command Definitions ────────────────────────────────────── */

export const COMMANDS: CommandDef[] = [

  /* ═══════════════════════ CORE ═══════════════════════ */

  {
    name: "help",
    aliases: ["?"],
    description: "Show available commands",
    category: "CORE",
    hidden: false,
    execute: (_args, ctx) => {
      const visibleCmds = COMMANDS.filter((c) => !c.hidden);
      const categories = ["CORE", "NAVIGATION", "PROJECTS", "SYSTEM", "CIPHER", "UTILITY"] as const;
      return [
        out(
          <div className="space-y-3 text-[11px]">
            {categories.map((cat) => {
              const cmds = visibleCmds.filter((c) => c.category === cat);
              if (cmds.length === 0) return null;
              return (
                <div key={cat}>
                  <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] mb-1.5 font-semibold">{cat}</p>
                  <div className="grid grid-cols-[110px_1fr] gap-x-2 gap-y-0.5">
                    {cmds.map((c) => (
                      <React.Fragment key={c.name}>
                        <span className="text-[#D4C87A]">{c.name}{c.aliases.length ? ` / ${c.aliases[0]}` : ""}</span>
                        <span className="text-[#7A7874]">{c.description}</span>
                      </React.Fragment>
                    ))}
                  </div>
                </div>
              );
            })}
            <div className="pt-2 border-t border-white/5 text-[9px] text-[#7A7874]/60">
              {visibleCmds.length} commands available. Some systems remain undocumented.
            </div>
          </div>
        ),
      ];
    },
  },

  {
    name: "whoami",
    aliases: ["me", "identity"],
    description: "Display identity record",
    category: "SYSTEM",
    hidden: false,
    execute: () => [
      out(
        <div className="space-y-1.5 text-[11px]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">IDENTITY RECORD</p>
          <div className="text-[#B8B6AF]">
            <p><span className="text-[#7A7874]">NAME:</span> YASH</p>
            <p className="mt-1"><span className="text-[#7A7874]">PRIMARY MODE:</span></p>
            <p className="pl-2">BUILD / DESIGN / EXPERIMENT</p>
            <p className="mt-1"><span className="text-[#7A7874]">ACTIVE SYSTEMS:</span></p>
            <div className="pl-2 flex flex-wrap gap-x-3 gap-y-0.5">
              {["SOFTWARE", "AI", "CINEMA", "3D", "WRITING", "ENGINEERING"].map((s) => (
                <span key={s} className="text-[#4A90D9]">{s}</span>
              ))}
            </div>
            <p className="mt-1"><span className="text-[#7A7874]">STATUS:</span> <span className="text-[#D4C87A]">CURIOUS</span></p>
          </div>
        </div>
      ),
    ],
  },

  {
    name: "status",
    aliases: [],
    description: "System diagnostic",
    category: "SYSTEM",
    hidden: false,
    execute: (_args, ctx) => {
      const uptime = Math.floor((Date.now() - ctx.openTime) / 1000);
      const mins = Math.floor(uptime / 60);
      const secs = uptime % 60;
      return [
        out(
          <div className="space-y-2 text-[11px]">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">YASH.OS STATUS</p>
            <div className="space-y-0.5">
              {statusBar("CORE", "ONLINE", "#5BAA8A")}
              {statusBar("VISUAL ENGINE", "ACTIVE", "#5BAA8A")}
              {statusBar("AUDIO ENGINE", sound.getIsMuted() ? "MUTED" : "ACTIVE", sound.getIsMuted() ? "#D4C87A" : "#5BAA8A")}
              {statusBar("ARCHIVE", "INDEXED", "#5BAA8A")}
              {statusBar("CIPHER SYSTEM", "ACTIVE", "#4A90D9")}
              {statusBar("UNKNOWN PROCESSES", "03", "#D4C87A")}
            </div>
            <div className="pt-1 border-t border-white/5">
              <p className="text-[#7A7874]">SESSION: {mins}m {secs}s · {ctx.commandCount} commands executed</p>
            </div>
          </div>
        ),
      ];
    },
  },

  {
    name: "version",
    aliases: ["ver"],
    description: "System version info",
    category: "SYSTEM",
    hidden: false,
    execute: () => [
      out(
        <div className="space-y-1 text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">VERSION</p>
          <p><span className="text-[#7A7874]">YASH.OS</span> 2.6.4</p>
          <p><span className="text-[#7A7874]">BUILD:</span> STUDIO</p>
          <p><span className="text-[#7A7874]">KERNEL:</span> CUSTOM</p>
          <p><span className="text-[#7A7874]">STATE:</span> <span className="text-[#D4C87A]">EXPERIMENTAL</span></p>
        </div>
      ),
    ],
  },

  {
    name: "date",
    aliases: ["time", "clock"],
    description: "Current system time",
    category: "SYSTEM",
    hidden: false,
    execute: () => {
      const now = new Date();
      const months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"];
      const dayOfYear = Math.floor((now.getTime() - new Date(now.getFullYear(), 0, 0).getTime()) / 86400000);
      const time = now.toLocaleTimeString("en-US", { hour12: false, hour: "2-digit", minute: "2-digit", second: "2-digit" });
      return [
        out(
          <div className="text-[11px] text-[#B8B6AF]">
            <span className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">CLOCK</span>
            <p className="mt-1">
              {now.getDate()} {months[now.getMonth()]} {now.getFullYear()} · {time} IST · DAY {dayOfYear} · SYSTEM CLOCK ACTIVE
            </p>
          </div>
        ),
      ];
    },
  },

  {
    name: "pwd",
    aliases: [],
    description: "Print working directory",
    category: "UTILITY",
    hidden: false,
    execute: () => [out(<span className="text-[11px] text-[#B8B6AF]">/architecture/of/unfinished/ideas</span>)],
  },

  {
    name: "history",
    aliases: [],
    description: "Session command history",
    category: "UTILITY",
    hidden: false,
    execute: (_args, ctx) => {
      if (ctx.history.length === 0) return [sys("No commands executed this session.")];
      return [
        out(
          <div className="space-y-0.5 text-[11px]">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">SESSION HISTORY</p>
            {ctx.history.map((cmd, i) => (
              <div key={i} className="flex gap-3">
                <span className="text-[#7A7874] w-5 text-right">{String(i + 1).padStart(2, "0")}</span>
                <span className="text-[#B8B6AF]">{cmd}</span>
              </div>
            ))}
          </div>
        ),
      ];
    },
  },

  {
    name: "clear",
    aliases: ["cls"],
    description: "Clear terminal output",
    category: "UTILITY",
    hidden: false,
    execute: (_args, ctx) => {
      ctx.setLogs([]);
      return [];
    },
  },

  {
    name: "close",
    aliases: [],
    description: "Close terminal",
    category: "UTILITY",
    hidden: false,
    execute: (_args, ctx) => {
      setTimeout(() => ctx.onClose(), 50);
      return [];
    },
  },

  /* ═══════════════════════ NAVIGATION ═══════════════════════ */

  {
    name: "goto",
    aliases: ["go", "jump", "scroll"],
    description: "Navigate to section",
    category: "NAVIGATION",
    hidden: false,
    execute: (args, ctx) => {
      const sectionMap: Record<string, string> = {
        hero: "hero", origin: "hero",
        about: "about", mind: "about",
        work: "work", projects: "work",
        channels: "channels", channel: "channels",
        archive: "archive",
        cipher: "cipher", cipherlab: "cipher",
        constellation: "constellation", obsessions: "constellation",
        contact: "contact",
        field: "field", text: "text", lab: "lab",
      };
      const target = args.toLowerCase().trim();
      if (!target) {
        return [err(`Usage: goto <section>\nAvailable: ${Object.keys(sectionMap).join(", ")}`)];
      }
      const sectionId = sectionMap[target];
      if (!sectionId) {
        return [err(`Section '${target}' not found.\nAvailable: ${Array.from(new Set(Object.values(sectionMap))).join(", ")}`)];
      }
      ctx.scrollToSection(sectionId);
      setTimeout(() => ctx.onClose(), 150);
      return [sys(`Navigating to ${target.toUpperCase()}...`)];
    },
  },

  /* ═══════════════════════ PROJECTS ═══════════════════════ */

  {
    name: "projects",
    aliases: ["ls"],
    description: "List all projects",
    category: "PROJECTS",
    hidden: false,
    execute: (_args, ctx) => [
      out(
        <div className="space-y-1.5 text-[11px]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">INDEX</p>
          {EXHIBITION_PROJECTS.map((p) => (
            <div key={p.id} className="flex items-center justify-between border-b border-white/5 pb-1">
              <span className="text-[#B8B6AF]">
                <span className="text-[#4A90D9] font-bold">{p.slug}</span>
                <span className="text-[#7A7874] ml-2">[{p.domain}]</span>
                <span className="text-[#7A7874] ml-2 text-[9px]">{p.status}</span>
              </span>
              <button
                onClick={() => { ctx.onSelectProject(p.slug); ctx.onClose(); }}
                className="text-[#D4C87A] hover:text-[#D4C87A]/80 text-[10px] underline"
              >
                open
              </button>
            </div>
          ))}
        </div>
      ),
    ],
  },

  {
    name: "open",
    aliases: ["inspect"],
    description: "Open project case study",
    category: "PROJECTS",
    hidden: false,
    execute: (args, ctx) => {
      const slug = args.trim().toLowerCase();
      if (!slug) {
        return [err("Usage: open <slug>\nTry: open page-os")];
      }
      const match = EXHIBITION_PROJECTS.find((p) => p.slug.toLowerCase() === slug);
      if (match) {
        ctx.onSelectProject(match.slug);
        ctx.onClose();
        return [];
      }
      return [err(`PROJECT NOT FOUND\n\nSEARCHED: ${slug}\n\nTry: projects`)];
    },
  },

  {
    name: "scan",
    aliases: [],
    description: "Scan portfolio systems",
    category: "PROJECTS",
    hidden: false,
    execute: () => {
      const lines = [
        "SCANNING PORTFOLIO...",
        "",
        ...EXHIBITION_PROJECTS.map((p) => {
          const statusColors: Record<string, string> = {
            "BUILDING": "#D4C87A",
            "ACTIVE": "#5BAA8A",
            "IN DEVELOPMENT": "#4A90D9",
            "EXPERIMENTAL": "#C4565A",
          };
          const color = statusColors[p.status] || "#7A7874";
          const dots = ".".repeat(Math.max(1, 20 - p.slug.length));
          return `${p.slug} ${dots} ${p.status}`;
        }),
        "",
        "SCAN COMPLETE",
      ];
      return [
        out(
          <div className="text-[11px] font-mono space-y-0.5">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">SYSTEM SCAN</p>
            {lines.map((line, i) => (
              <p key={i} className={
                line === "SCANNING PORTFOLIO..." ? "text-[#D4C87A]" :
                line === "SCAN COMPLETE" ? "text-[#5BAA8A]" :
                line === "" ? "" :
                "text-[#B8B6AF]"
              }>{line}</p>
            ))}
          </div>
        ),
      ];
    },
  },

  {
    name: "tree",
    aliases: [],
    description: "View filesystem structure",
    category: "PROJECTS",
    hidden: false,
    execute: () => [
      out(
        treeBlock(
`YASH.OS/
├── WORK/
│   ├── PAGE.OS
│   ├── ANE
│   ├── RESIDUAL
│   └── FIFTH_EXIT
│
├── LAB/
│   ├── 3D
│   ├── AUDIO
│   └── CODE
│
├── ARCHIVE/
│   ├── WRITING
│   └── CIPHER
│
└── UNKNOWN/
    └── ??????`
        ),
      ),
    ],
  },

  /* ═══════════════════════ CIPHER ═══════════════════════ */

  {
    name: "cipher",
    aliases: ["encode"],
    description: "Encode text to glyphs",
    category: "CIPHER",
    hidden: false,
    execute: (args, ctx) => {
      if (!args.trim()) {
        return [err("Usage: cipher <text>\nExample: cipher HELLO")];
      }
      const text = args.trim().toUpperCase();
      const glyphs = encodeText(text);
      glyphs.forEach((_, i) => {
        setTimeout(() => sound.playCipherChirp(0.7 + i * 0.05), i * 40);
      });
      return [
        cipher(
          <div className="space-y-2 p-2 rounded border border-[#D4C87A]/20">
            <div className="text-[10px] text-[#D4C87A] font-mono">"{text}"</div>
            <div className="flex flex-wrap gap-2 items-center">
              {text.split("").map((c, i) => (
                <div key={i} className="flex flex-col items-center gap-0.5 p-1 rounded">
                  <GlyphSymbol char={c} size={20} color="#D4C87A" />
                  <span className="text-[8px] text-[#7A7874]">{c}</span>
                </div>
              ))}
            </div>
          </div>
        ),
      ];
    },
  },

  {
    name: "decode",
    aliases: [],
    description: "Decode cipher text (requires key)",
    category: "CIPHER",
    hidden: false,
    execute: (args) => {
      if (!args.trim()) {
        return [err("Usage: decode <encoded-text> [key]\nExample: decode XMNNB SECRET")];
      }
      const parts = args.trim().split(/\s+/);
      const encoded = parts[0].toUpperCase();
      const key = (parts[1] || "SECRET").toUpperCase();
      const result = decodeCipherText(encoded, key);
      return [
        out(
          <div className="text-[11px] space-y-1">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">DECODE</p>
            <p className="text-[#7A7874]">KEY: {key}</p>
            <p className="text-[#B8B6AF]">RESULT: <span className="text-[#D4C87A]">{result.text}</span></p>
          </div>
        ),
      ];
    },
  },

  {
    name: "glyph",
    aliases: ["glyphs", "alphabet"],
    description: "Display glyph alphabet index",
    category: "CIPHER",
    hidden: false,
    execute: () => {
      const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
      return [
        out(
          <div className="space-y-2 text-[11px]">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">GLYPH INDEX</p>
            <div className="grid grid-cols-6 sm:grid-cols-9 gap-1.5">
              {letters.map((l) => {
                const g = CIPHER_DICTIONARY[l];
                return (
                  <div key={l} className="flex flex-col items-center gap-0.5 p-1 rounded border border-white/5 hover:border-[#D4C87A]/30 transition-colors">
                    <GlyphSymbol char={l} size={18} color="#D4C87A" interactive={false} />
                    <span className="text-[7px] text-[#7A7874]">{g?.name?.split(" ")[0] || l}</span>
                  </div>
                );
              })}
            </div>
            <p className="text-[9px] text-[#7A7874]">SYSTEM TYPE: VISUAL LANGUAGE · STATUS: PARTIALLY DOCUMENTED</p>
          </div>
        ),
      ];
    },
  },

  /* ═══════════════════════ UTILITY ═══════════════════════ */

  {
    name: "about",
    aliases: [],
    description: "About the operator",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="space-y-2 text-xs border-l border-[#F2F0EA]/10 pl-3">
          <p className="font-serif italic text-sm text-[#B8B6AF]">
            &ldquo;I like taking things apart. Machines. Software. Stories. Interfaces. Systems.
            Then I try to understand what makes them work.&rdquo;
          </p>
        </div>
      ),
    ],
  },

  {
    name: "fortune",
    aliases: ["quote"],
    description: "Random project quote",
    category: "UTILITY",
    hidden: false,
    execute: () => {
      const f = FORTUNES[Math.floor(Math.random() * FORTUNES.length)];
      return [
        out(
          <div className="space-y-1.5 text-[11px] border-l border-[#D4C87A]/20 pl-3">
            <p className="text-[#B8B6AF] italic">&ldquo;{f.quote}&rdquo;</p>
            <p className="text-[#7A7874] text-[9px]">— {f.source}</p>
          </div>
        ),
      ];
    },
  },

  {
    name: "contact",
    aliases: [],
    description: "Contact information",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="space-y-1 text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">CONTACT</p>
          <p><span className="text-[#7A7874]">STATUS:</span> <span className="text-[#5BAA8A]">AVAILABLE</span></p>
          <p><span className="text-[#7A7874]">LOCATION:</span> Mumbai, India</p>
          <p><span className="text-[#7A7874]">MODE:</span> Open to collaboration</p>
        </div>
      ),
    ],
  },

  {
    name: "reality",
    aliases: [],
    description: "Check reality status",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">REALITY</p>
          <p>STATUS: <span className="text-[#D4C87A]">UNVERIFIED</span></p>
        </div>
      ),
    ],
  },

  {
    name: "nothing",
    aliases: [],
    description: "Display nothing",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">NOTHING</p>
          <p>No additional information.</p>
        </div>
      ),
    ],
  },

  {
    name: "why",
    aliases: [],
    description: "Ask why",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(<span className="text-[11px] text-[#B8B6AF] italic">Because &ldquo;how&rdquo; was not enough.</span>),
    ],
  },

  {
    name: "meaning",
    aliases: [],
    description: "Search for meaning",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">MEANING</p>
          <p>No universal result returned.</p>
        </div>
      ),
    ],
  },

  {
    name: "void",
    aliases: [],
    description: "Query the void",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">VOID</p>
          <p>Query accepted.</p>
          <p className="mt-2 text-center text-[#D4C87A]">.</p>
        </div>
      ),
    ],
  },

  {
    name: "404",
    aliases: [],
    description: "Look for something",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#C4565A] font-semibold mb-1">404</p>
          <p>NOT FOUND.</p>
          <p className="text-[#7A7874] mt-1">You expected something here.</p>
        </div>
      ),
    ],
  },

  {
    name: "coffee",
    aliases: [],
    description: "Brew coffee",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">COFFEE</p>
          <p>BREWING...</p>
          <p className="font-mono text-[#D4C87A]">██████████████░░</p>
          <p className="mt-1 text-[#C4565A]">ERROR: THERMODYNAMICS UNAVAILABLE.</p>
        </div>
      ),
    ],
  },

  {
    name: "sleep",
    aliases: [],
    description: "Request sleep mode",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF]">
          <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">SLEEP</p>
          <p className="text-[#C4565A]">REQUEST DENIED.</p>
          <p className="text-[#7A7874] mt-1">Active processes detected.</p>
        </div>
      ),
    ],
  },

  {
    name: "page",
    aliases: [],
    description: "PAGE.OS status",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF] space-y-1">
          <p className="text-[#4A90D9] font-semibold">PAGE.OS</p>
          <p>STATUS: <span className="text-[#D4C87A]">STILL BECOMING.</span></p>
          <p className="text-[#7A7874] italic">Somewhere between a library and an operating system.</p>
        </div>
      ),
    ],
  },

  {
    name: "ane",
    aliases: [],
    description: "ANE system status",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF] space-y-1">
          <p className="text-[#D4C87A] font-semibold">ANE</p>
          <p>AUDIO NARRATIVE ENGINE</p>
          <p>STATUS: <span className="text-[#5BAA8A]">LISTENING.</span></p>
        </div>
      ),
    ],
  },

  {
    name: "residual",
    aliases: [],
    description: "RESIDUAL status",
    category: "UTILITY",
    hidden: false,
    execute: () => [
      out(
        <div className="text-[11px] text-[#B8B6AF] space-y-1">
          <p className="text-[#94a3b8] font-semibold">RESIDUAL</p>
          <p>STONE · SHADOW · SILENCE</p>
          <p>IMAGE ARCHIVE: <span className="text-[#5BAA8A]">ACTIVE</span></p>
        </div>
      ),
    ],
  },

  {
    name: "matrix",
    aliases: [],
    description: "Brief signal interference",
    category: "UTILITY",
    hidden: false,
    execute: () => {
      const chars = "01アイウエオカキクケコ";
      const lines: string[] = [];
      for (let i = 0; i < 8; i++) {
        let line = "";
        for (let j = 0; j < 60; j++) {
          line += Math.random() > 0.7 ? chars[Math.floor(Math.random() * chars.length)] : " ";
        }
        lines.push(line);
      }
      return [
        out(
          <div className="text-[10px] font-mono text-[#5BAA8A]/40 leading-tight">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold mb-1">SIGNAL INTERFERENCE</p>
            {lines.map((l, i) => <p key={i} className="whitespace-pre">{l}</p>)}
            <p className="text-[#7A7874] mt-1">Interference cleared.</p>
          </div>
        ),
      ];
    },
  },

  {
    name: "play",
    aliases: ["game"],
    description: "Signal decoder minigame",
    category: "UTILITY",
    hidden: false,
    execute: (_args, ctx) => {
      if (ctx.gameState.phase === "playing") {
        return [sys("Game already in progress. Type a number to guess.")];
      }
      const target = Math.floor(Math.random() * 50) + 1;
      ctx.setGameState({ phase: "playing", round: 1, score: 0, target, attempts: 0, history: [] });
      return [
        game(
          <div className="space-y-2 text-[11px]">
            <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">YASH.OS // GUESS THE NUMBER</p>
            <p className="text-[#B8B6AF]">I'm thinking of a number between <span className="text-[#D4C87A]">1</span> and <span className="text-[#D4C87A]">50</span>.</p>
            <p className="text-[#7A7874]">Type a number to guess. Type "quit" to abort.</p>
          </div>
        ),
      ];
    },
  },

  /* ═══════════════════════ HIDDEN COMMANDS ═══════════════════════ */

  {
    name: "secret",
    aliases: ["archive", "fragments"],
    description: "",
    category: "SYSTEM",
    hidden: true,
    execute: (_args, ctx) => {
      const s = ctx.secrets;
      if (!s.secretFound) {
        ctx.setSecrets((prev) => ({ ...prev, secretFound: true }));
        return [
          secret(
            <div className="space-y-2 text-[11px]">
              <p className="text-[#D4C87A] font-semibold">ENCRYPTED ARCHIVE DETECTED.</p>
              <p className="text-[#7A7874]">ACCESSING...</p>
              <div className="flex gap-2 my-2">
                {[0, 1, 2].map((i) => (
                  <div key={i} className="p-1.5 border border-[#D4C87A]/20 rounded text-center">
                    <span className="text-[#D4C87A]">[{String(i + 1).padStart(2, "0")}]</span>
                  </div>
                ))}
              </div>
              <p className="text-[#B8B6AF]">One fragment appears to reference:</p>
              <p className="text-[#C4565A] font-semibold">EXIT 5</p>
              <p className="text-[#7A7874] text-[9px]">Try: cipher, decode, glyph</p>
            </div>
          ),
        ];
      }
      return [
        secret(
          <div className="text-[11px] text-[#B8B6AF]">
            <p className="text-[#D4C87A]">ARCHIVE ALREADY ACCESSED.</p>
            <p className="text-[#7A7874] mt-1">Fragments collected: {s.archiveFragments.length}/3</p>
          </div>
        ),
      ];
    },
  },

  {
    name: "ira",
    aliases: [],
    description: "",
    category: "SYSTEM",
    hidden: true,
    execute: (_args, ctx) => {
      ctx.setSecrets((prev) => ({ ...prev, iraFound: true }));
      return [
        secret(
          <div className="space-y-2 text-[11px]">
            <p className="text-[#C4565A] font-semibold">ARCHIVE ENTRY FOUND</p>
            <p className="text-[#7A7874]">SUBJECT:</p>
            <p className="text-[#B8B6AF] font-semibold">IRA ELOWEN MIREILLE</p>
            <p className="text-[#7A7874]">STATUS: <span className="text-[#D4C87A]">INCOMPLETE</span></p>
            <p className="text-[#7A7874] mt-2">LAST KNOWN NOTE:</p>
            <p className="text-[#B8B6AF] italic">&ldquo;Something is wrong with the room.&rdquo;</p>
          </div>
        ),
      ];
    },
  },

  {
    name: "sudo",
    aliases: [],
    description: "",
    category: "SYSTEM",
    hidden: true,
    execute: (args, ctx) => {
      const sub = args.trim().toLowerCase();
      if (!sub) {
        return [
          secret(
            <div className="text-[11px] text-[#B8B6AF]">
              <p className="text-[#D4C87A] font-semibold">PRIVILEGE ESCALATION</p>
              <p className="mt-1">Nice try.</p>
              <p className="text-[#7A7874]">You already have access.</p>
            </div>
          ),
        ];
      }
      // sudo scan gives special output
      if (sub === "scan") {
        return [
          secret(
            <div className="text-[11px] text-[#B8B6AF] space-y-1">
              <p className="text-[#D4C87A] font-semibold">ROOT ACCESS REQUESTED</p>
              <p className="text-[#7A7874]">...</p>
              <p className="text-[#5BAA8A]">ACCESS GRANTED</p>
              <p className="mt-2 text-[#C4565A]">You probably shouldn&apos;t have done that.</p>
            </div>
          ),
        ];
      }
      // For any other sub-command, just execute it normally
      const cmd = COMMANDS.find((c) => c.name === sub || c.aliases.includes(sub));
      if (cmd && !cmd.hidden) {
        return cmd.execute(args.split(/\s+/).slice(1).join(" "), ctx);
      }
      return [err(`Unknown command: '${sub}'`)];
    },
  },

  {
    name: "rm",
    aliases: [],
    description: "",
    category: "UTILITY",
    hidden: true,
    execute: (args) => {
      if (args.trim() === "-rf /" || args.trim() === "-rf /" || args.includes("-rf /")) {
        return [
          secret(
            <div className="text-[11px] text-[#B8B6AF]">
              <p className="text-[#C4565A] font-semibold">WARNING</p>
              <p className="mt-1">REQUEST WOULD DESTROY YASH.OS</p>
              <p className="text-[#7A7874]">...</p>
              <p className="text-[#D4C87A] mt-1">REQUEST DENIED.</p>
              <p className="text-[#7A7874] mt-1">Some things are better left intact.</p>
            </div>
          ),
        ];
      }
      return [err("Insufficient permissions.")];
    },
  },

  {
    name: "exit",
    aliases: [],
    description: "",
    category: "UTILITY",
    hidden: true,
    execute: (args, ctx) => {
      // exit 5 — The Fifth Exit easter egg
      if (args.trim() === "5") {
        if (!ctx.secrets.fifthExitClueFound) {
          return [
            out(
              <div className="text-[11px] text-[#B8B6AF] space-y-1">
                <p className="text-[#5BAA8A]/60 text-[9px] tracking-[0.2em] font-semibold">EXIT ROUTINE</p>
                <p>1 ........ AVAILABLE</p>
                <p>2 ........ AVAILABLE</p>
                <p>3 ........ AVAILABLE</p>
                <p>4 ........ AVAILABLE</p>
                <p className="text-[#C4565A]">5 ........ UNKNOWN</p>
                <p className="text-[#7A7874] mt-2">Resolving...</p>
                <p className="text-[#C4565A] mt-1">ERROR: Exit 5 is not a navigation target.</p>
                <p>It is a location.</p>
              </div>
            ),
          ];
        }
        // If they found the clue first
        ctx.setSecrets((prev) => ({ ...prev, fifthExitTriggered: true }));
        sound.playArtifactResonance();
        return [
          secret(
            <div className="text-[11px] space-y-1">
              <p className="text-[#C4565A] font-semibold animate-pulse">EXIT 5</p>
              <p className="text-[#B8B6AF]">You did not enter the building.</p>
              <p className="text-[#B8B6AF]">The building materialized around your silence.</p>
              <p className="text-[#D4C87A] mt-2 font-semibold">ARCHIVE COMPLETE</p>
              <p className="text-[#B8B6AF]">You found the part that wasn&apos;t supposed to be obvious.</p>
              <p className="text-[#B8B6AF]">There is no reward.</p>
              <p className="text-[#B8B6AF]">Except this.</p>
              <p className="text-[#7A7874] mt-2">KEEP LOOKING.</p>
              <div className="mt-2 flex justify-center">
                <GlyphSymbol char="X" size={28} color="#D4C87A" interactive={false} />
              </div>
            </div>
          ),
        ];
      }
      // Normal exit
      setTimeout(() => ctx.onClose(), 50);
      return [];
    },
  },
];

/* ── Minigame Logic ──────────────────────────────────────────── */

export function handleGameState(
  input: string,
  ctx: TerminalContext,
): CommandLogEntry[] {
  const gs = ctx.gameState;
  if (gs.phase !== "playing") return [];

  const trimmed = input.trim().toLowerCase();
  if (trimmed === "quit" || trimmed === "exit") {
    ctx.setGameState((prev) => ({ ...prev, phase: "idle" }));
    return [sys("Game aborted.")];
  }

  const guess = parseInt(trimmed, 10);
  if (isNaN(guess) || guess < 1 || guess > 50) {
    return [err("Enter a number between 1 and 50.")];
  }

  const newAttempts = gs.attempts + 1;
  const direction = guess < gs.target ? "HIGHER" : guess > gs.target ? "LOWER" : "CORRECT";

  if (direction === "CORRECT") {
    ctx.setGameState((prev) => ({ ...prev, phase: "won", score: prev.score + 1, attempts: newAttempts }));
    return [
      game(
        <div className="text-[11px] space-y-1">
          <p className="text-[#5BAA8A] font-semibold">ACCESS GRANTED.</p>
          <p className="text-[#B8B6AF]">That was unnecessary.</p>
          <p className="text-[#7A7874]">Well done. {newAttempts} attempt{newAttempts !== 1 ? "s" : ""}.</p>
        </div>
      ),
    ];
  }

  if (newAttempts >= 10) {
    ctx.setGameState((prev) => ({ ...prev, phase: "lost" }));
    return [
      game(
        <div className="text-[11px] space-y-1">
          <p className="text-[#C4565A] font-semibold">LOCKOUT.</p>
          <p className="text-[#7A7874]">The number was {gs.target}.</p>
          <p className="text-[#7A7874]">Try again: play</p>
        </div>
      ),
    ];
  }

  ctx.setGameState((prev) => ({
    ...prev,
    attempts: newAttempts,
    history: [...prev.history, { guess, direction }],
  }));

  return [
    game(
      <div className="text-[11px] space-y-1">
        <p className="text-[#D4C87A] font-semibold">{direction}.</p>
        <p className="text-[#7A7874]">Attempt {newAttempts}/10</p>
      </div>
    ),
  ];
}

/* ── Sequence Detection ──────────────────────────────────────── */

export function checkCommandSequence(
  history: string[],
  ctx: TerminalContext,
): CommandLogEntry | null {
  const last5 = history.slice(-5).map((h) => h.toLowerCase().trim());

  // Pattern: help, ls, ls, pwd → "YOU ARE SEARCHING LIKE A MACHINE."
  if (
    last5.length >= 4 &&
    last5.slice(-4).join(",") === "help,ls,ls,pwd"
  ) {
    if (!ctx.secrets.sequenceDetected) {
      ctx.setSecrets((prev) => ({ ...prev, sequenceDetected: true }));
      return secret(
        <div className="text-[11px] text-[#D4C87A]">
          <p>PATTERN DETECTED.</p>
          <p className="text-[#B8B6AF] mt-1">YOU ARE SEARCHING LIKE A MACHINE.</p>
        </div>
      );
    }
  }

  return null;
}

/* ── Lookup Helpers ──────────────────────────────────────────── */

export function findCommand(input: string): { command: CommandDef; args: string } | null {
  const parts = input.trim().split(/\s+/);
  const cmdName = parts[0].toLowerCase();
  const args = parts.slice(1).join(" ");

  // Special case: "rm -rf /" needs to match "rm" with the rest as args
  if (cmdName === "rm") {
    return { command: COMMANDS.find((c) => c.name === "rm")!, args: args || "-rf /" };
  }

  // Special case: "exit 5" triggers easter egg, bare "exit" closes
  if (cmdName === "exit") {
    if (args.trim() === "5") {
      const exitCmd = COMMANDS.find((c) => c.name === "exit" && c.hidden);
      if (exitCmd) return { command: exitCmd, args };
    }
    // Bare exit — use close
    const closeCmd = COMMANDS.find((c) => c.name === "close");
    if (closeCmd) return { command: closeCmd, args: "" };
  }

  const cmd = COMMANDS.find((c) => c.name === cmdName || c.aliases.includes(cmdName));
  if (cmd) return { command: cmd, args };

  return null;
}
