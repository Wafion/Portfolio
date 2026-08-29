"use client";

import React, { useState, useEffect } from "react";
import { sound } from "@/components/audio/SoundEngine";
import { Volume2, VolumeX, Terminal, Compass, Radio } from "lucide-react";
import { GlyphSymbol } from "@/components/ui/GlyphSymbol";

interface YashOsHUDProps {
  onOpenTerminal: () => void;
}

export function YashOsHUD({ onOpenTerminal }: YashOsHUDProps) {
  const [isMuted, setIsMuted] = useState(true);
  const [timeString, setTimeString] = useState("");
  const [systemUptime, setSystemUptime] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date();
      setTimeString(
        now.toLocaleTimeString("en-US", {
          hour12: false,
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        })
      );
      setSystemUptime((prev) => prev + 1);
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const handleAudioToggle = () => {
    const unmuted = sound.toggleMute();
    setIsMuted(!unmuted);
  };

  const formatUptime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `+${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
  };

  return (
    <>
      {/* Top Telemetry Header */}
      <header className="fixed top-0 left-0 right-0 z-40 flex items-center justify-between px-4 py-3 md:px-8 border-b border-white/10 bg-[#0c0f17]/90 backdrop-blur-md text-[11px] font-mono select-none">
        {/* Left: System Status & Logo */}
        <div className="flex items-center gap-4">
          <a
            href="#hero"
            className="flex items-center gap-2.5 text-white hover:text-cyan-300 transition-colors group"
            data-cursor="ORIGIN"
          >
            <div className="relative flex items-center justify-center w-5 h-5 rounded border border-white/30 bg-white/10 group-hover:border-cyan-400">
              <GlyphSymbol char="Y" size={14} interactive={false} color="#38bdf8" />
            </div>
            <span className="font-bold tracking-widest text-xs text-white">YASH.OS</span>
            <span className="hidden sm:inline-block text-[10px] text-cyan-400 font-semibold tracking-normal border-l border-white/15 pl-2">
              v2.6.4_STUDIO
            </span>
          </a>

          <div className="hidden lg:flex items-center gap-2 text-white/60">
            <Radio className="w-3 h-3 text-emerald-400 animate-pulse" />
            <span className="text-white/80">CORE: ONLINE</span>
            <span className="text-white/30">|</span>
            <span>MPSTME MUMBAI</span>
          </div>
        </div>

        {/* Center: Navigation Links */}
        <nav className="hidden md:flex items-center gap-6 text-white/75 font-medium">
          <a
            href="#manifesto"
            className="hover:text-white transition-colors tracking-wider"
            data-cursor="MIND"
          >
            01//MIND
          </a>
          <a
            href="#projects"
            className="hover:text-cyan-300 transition-colors tracking-wider"
            data-cursor="LABORATORY"
          >
            02//PROJECTS
          </a>
          <a
            href="#cipher-lab"
            className="hover:text-amber-300 transition-colors tracking-wider"
            data-cursor="CIPHER"
          >
            03//CIPHER
          </a>
          <a
            href="#creative-coding"
            className="hover:text-emerald-300 transition-colors tracking-wider"
            data-cursor="SKETCHBOOK"
          >
            04//EXPERIMENTS
          </a>
          <a
            href="#constellation"
            className="hover:text-purple-300 transition-colors tracking-wider"
            data-cursor="OBSESSIONS"
          >
            05//OBSESSIONS
          </a>
          <a
            href="#capabilities"
            className="hover:text-white transition-colors tracking-wider"
            data-cursor="CAPABILITIES"
          >
            06//MAP
          </a>
        </nav>

        {/* Right: Controls & Time */}
        <div className="flex items-center gap-3">
          {/* Spatial Sound Toggle */}
          <button
            onClick={handleAudioToggle}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded border transition-all ${
              isMuted
                ? "border-white/15 text-white/60 hover:border-white/30 hover:text-white"
                : "border-cyan-400 bg-cyan-950/60 text-cyan-200 shadow-[0_0_12px_rgba(56,189,248,0.3)]"
            }`}
            data-cursor={isMuted ? "ENABLE SOUND" : "MUTE SOUND"}
            title="Toggle synthesized ambient soundscape & click acoustics"
          >
            {isMuted ? <VolumeX className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5 animate-pulse" />}
            <span className="hidden sm:inline text-[10px] tracking-wider uppercase font-semibold">
              {isMuted ? "AUDIO: OFF" : "AUDIO: ON"}
            </span>
          </button>

          {/* Terminal Launcher */}
          <button
            onClick={() => {
              sound.playSoftClick(400);
              onOpenTerminal();
            }}
            className="flex items-center gap-1.5 px-2.5 py-1 rounded border border-white/20 hover:border-white/40 text-white bg-white/10 hover:bg-white/15 transition-all"
            data-cursor="OPEN TERMINAL"
            title="Launch YASH.OS interactive command line (/)"
          >
            <Terminal className="w-3.5 h-3.5 text-cyan-400" />
            <span className="hidden sm:inline text-[10px] tracking-wider font-semibold">CMD</span>
            <kbd className="hidden lg:inline-block px-1 py-0.2 text-[8px] bg-white/15 rounded text-white/70">
              ` / `
            </kbd>
          </button>

          {/* Clock */}
          <div className="hidden sm:flex items-center gap-1.5 px-2.5 py-1 text-white/70 border border-white/10 bg-white/5 rounded">
            <span className="text-cyan-400 text-[9px]">IST</span>
            <span className="text-white font-medium">{timeString || "15:00:00"}</span>
          </div>
        </div>
      </header>

      {/* Floating Bottom Telemetry Bar */}
      <div className="fixed bottom-3 left-4 right-4 md:left-8 md:right-8 z-30 flex items-center justify-between text-[10px] font-mono text-white/50 pointer-events-none select-none">
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1.5 bg-[#121622]/90 backdrop-blur px-3 py-1 rounded border border-white/10 pointer-events-auto">
            <Compass className="w-3 h-3 text-cyan-400" />
            <span className="text-white/80">19.1030° N, 72.8360° E (MUMBAI)</span>
          </div>
          <div className="hidden sm:flex items-center gap-1.5 bg-[#121622]/90 backdrop-blur px-3 py-1 rounded border border-white/10">
            <span>UPTIME: {formatUptime(systemUptime)}</span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="bg-[#121622]/90 backdrop-blur px-3 py-1 rounded border border-white/10">
            <span className="text-cyan-300">MECHATRONICS / AI / CINEMA / 3D</span>
          </div>
        </div>
      </div>
    </>
  );
}
