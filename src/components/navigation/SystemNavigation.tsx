"use client";

import { useState } from "react";
import { Terminal, Volume2, VolumeX } from "lucide-react";
import { sound } from "@/components/audio/SoundEngine";

const NAV_ITEMS = [
  { id: "hero", label: "ORIGIN", code: "00" },
  { id: "work", label: "WORK", code: "01" },
  { id: "channels", label: "CHANNELS", code: "02" },
  { id: "archive", label: "ARCHIVE", code: "03" },
  { id: "intersections", label: "FIELD", code: "04" },
  { id: "writing", label: "TEXT", code: "05" },
  { id: "experiments", label: "LAB", code: "06" },
  { id: "contact", label: "CONTACT", code: "07" },
];

const MOBILE_PRIMARY_IDS = ["hero", "work", "channels", "writing", "experiments"];

export function SystemNavigation({
  activeSection,
  onOpenTerminal,
}: {
  activeSection: string;
  onOpenTerminal: () => void;
}) {
  const [isMuted, setIsMuted] = useState(true);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleSound = () => {
    const isPlaying = sound.toggleMute();
    setIsMuted(!isPlaying);
  };

  return (
    <>
      <header className="fixed inset-x-0 top-0 z-40 px-3 pt-3 md:px-6 md:pt-5">
        <div className="system-nav mx-auto flex max-w-[1440px] items-center justify-between px-3 py-2.5 md:px-4">
          <a href="#hero" className="flex items-center gap-3" data-cursor="ORIGIN">
            <span className="system-mark">Y</span>
            <span className="font-mono-tech text-[11px] font-medium tracking-[0.28em] text-[#f2f0ea]">YASH.OS</span>
            <span className="hidden border-l border-white/10 pl-3 text-[9px] tracking-[0.2em] text-[#77736d] sm:inline">PERSONAL SYSTEM</span>
          </a>

          <div className="flex items-center gap-2">
            <span className="hidden items-center gap-2 px-3 text-[9px] tracking-[0.18em] text-[#77736d] md:flex">
              <span className="status-dot" /> CORE ONLINE
            </span>
            <button onClick={toggleSound} className="system-control" data-cursor={isMuted ? "ENABLE SOUND" : "MUTE SOUND"}>
              {isMuted ? <VolumeX className="h-3.5 w-3.5" /> : <Volume2 className="h-3.5 w-3.5 text-[#d5bb76]" />}
              <span className="hidden sm:inline">AUDIO {isMuted ? "OFF" : "ON"}</span>
            </button>
            <button onClick={onOpenTerminal} className="system-control system-control-active" data-cursor="OPEN TERMINAL" aria-label="Open terminal">
              <Terminal className="h-3.5 w-3.5" />
              <span className="hidden sm:inline">CMD</span>
              <kbd className="hidden text-[8px] text-white/45 lg:inline">/</kbd>
            </button>
          </div>
        </div>
      </header>

      <nav className="fixed bottom-4 left-1/2 z-40 hidden -translate-x-1/2 items-center gap-1 rounded-full border border-white/10 bg-[#0a0a0b]/85 p-1.5 shadow-[0_16px_50px_rgba(0,0,0,0.4)] backdrop-blur-xl lg:flex" aria-label="Primary navigation">
        {NAV_ITEMS.map((item) => {
          const active = activeSection === item.id;
          return (
            <a
              key={item.id}
              href={`#${item.id}`}
              className={`group flex items-center gap-2 rounded-full px-3 py-2 text-[9px] tracking-[0.16em] transition-all ${active ? "bg-[#f2f0ea] text-[#080808]" : "text-[#77736d] hover:bg-white/8 hover:text-[#f2f0ea]"}`}
              data-cursor={`GO TO ${item.label}`}
            >
              <span className="font-mono-tech text-[8px] opacity-55">{item.code}</span>
              <span>{item.label}</span>
            </a>
          );
        })}
      </nav>

      <div className="mobile-nav-dock fixed bottom-3 left-3 right-3 z-40 flex items-center justify-between rounded-xl border border-white/10 bg-[#0a0a0b]/90 p-1.5 backdrop-blur-xl lg:hidden">
        <a href="#hero" className="system-mark ml-1">Y</a>
        <div className="flex items-center gap-1 overflow-x-auto">
          {NAV_ITEMS.filter((item) => MOBILE_PRIMARY_IDS.includes(item.id)).map((item) => (
            <a key={item.id} href={`#${item.id}`} className={`whitespace-nowrap rounded-lg px-2.5 py-2 text-[8px] tracking-[0.12em] ${activeSection === item.id ? "bg-[#f2f0ea] text-[#080808]" : "text-[#77736d]"}`}>
              {item.code} / {item.label}
            </a>
          ))}
        </div>
        <div className="relative flex items-center gap-1">
          <button onClick={() => setIsMenuOpen((open) => !open)} className={`rounded-lg border p-2 text-[#d5bb76] ${isMenuOpen ? "border-[#d5bb76]/70 bg-[#d5bb76]/10" : "border-[#d5bb76]/30"}`} aria-label="Open secondary navigation" aria-expanded={isMenuOpen}>
            <span className="block h-3.5 w-3.5 text-[10px] leading-3">•••</span>
          </button>
          <button onClick={onOpenTerminal} className="rounded-lg border border-[#d5bb76]/30 p-2 text-[#d5bb76]" aria-label="Open terminal">
            <Terminal className="h-3.5 w-3.5" />
          </button>
          {isMenuOpen && <div className="mobile-nav-menu absolute bottom-[calc(100%+0.65rem)] right-0 grid min-w-[10rem] gap-1 rounded-xl border border-white/10 bg-[#0a0a0b]/95 p-2 shadow-2xl backdrop-blur-xl">{NAV_ITEMS.filter((item) => !MOBILE_PRIMARY_IDS.includes(item.id)).map((item) => <a key={item.id} href={`#${item.id}`} onClick={() => setIsMenuOpen(false)} className={`rounded-lg px-3 py-2.5 text-[9px] tracking-[0.14em] ${activeSection === item.id ? "bg-[#f2f0ea] text-[#080808]" : "text-[#aaa39a] hover:bg-white/8"}`}>{item.code} / {item.label}</a>)}</div>}
        </div>
      </div>
    </>
  );
}
