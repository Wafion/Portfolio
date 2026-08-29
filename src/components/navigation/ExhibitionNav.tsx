"use client";

import React, { useState, useEffect } from "react";
import { sound } from "@/components/audio/SoundEngine";
import { Volume2, VolumeX } from "lucide-react";

export function ExhibitionNav() {
  const [isMuted, setIsMuted] = useState(true);
  const [scrolled, setScrolled] = useState(false);
  const [activeSection, setActiveSection] = useState("hero");

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 60);
      const sections = [
        "hero", "me", "work", "explore", "build", "make",
        "write", "experiments", "currently", "contact",
      ];
      for (const id of [...sections].reverse()) {
        const el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top < window.innerHeight * 0.4) {
          setActiveSection(id);
          break;
        }
      }
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleAudioToggle = () => {
    const unmuted = sound.toggleMute();
    setIsMuted(!unmuted);
  };

  const navItems = [
    { id: "work", label: "WORK", href: "#work" },
    { id: "explore", label: "EXPLORE", href: "#explore" },
    { id: "build", label: "BUILD", href: "#build" },
    { id: "make", label: "MAKE", href: "#make" },
    { id: "write", label: "WRITE", href: "#write" },
    { id: "contact", label: "CONTACT", href: "#contact" },
  ];

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-40 transition-all duration-500 ${
        scrolled
          ? "bg-[#050505]/95 backdrop-blur-xl border-b border-[#F2F0EA]/[0.04]"
          : "bg-transparent"
      }`}
    >
      <nav className="flex items-center justify-between px-6 md:px-12 lg:px-20 py-4 md:py-5">
        {/* Identity — left */}
        <a
          href="#hero"
          className="font-display text-sm font-bold tracking-[0.3em] text-[#F2F0EA] hover:text-[#8B5CF6] transition-colors"
        >
          YASH
        </a>

        {/* Navigation — center, hidden on mobile */}
        <div className="hidden lg:flex items-center gap-8">
          {navItems.map((item) => (
            <a
              key={item.id}
              href={item.href}
              className={`text-[11px] font-heading font-medium tracking-[0.1em] transition-all duration-300 ${
                activeSection === item.id
                  ? "text-[#F2F0EA]"
                  : "text-[#7A7874] hover:text-[#B8B6AF]"
              }`}
            >
              {item.label}
            </a>
          ))}
        </div>

        {/* Controls — right */}
        <div className="flex items-center gap-3">
          <button
            onClick={handleAudioToggle}
            className="flex items-center gap-2 px-3 py-1.5 rounded-full border transition-all duration-300 text-[10px] font-mono tracking-wider"
            style={{
              borderColor: isMuted ? "rgba(242,240,234,0.08)" : "rgba(139,92,246,0.3)",
              color: isMuted ? "#7A7874" : "#A78BFA",
            }}
            title="Toggle ambient sound"
          >
            {isMuted ? <VolumeX className="w-3 h-3" /> : <Volume2 className="w-3 h-3" />}
            <span className="hidden sm:inline uppercase">{isMuted ? "Sound" : "Sound"}</span>
          </button>
        </div>
      </nav>
    </header>
  );
}
