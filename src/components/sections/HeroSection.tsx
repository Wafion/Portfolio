"use client";

import React, { useEffect, useRef, useState } from "react";
import dynamic from "next/dynamic";
import { motion } from "framer-motion";

const UnfinishedArtifactCanvas = dynamic(
  () => import("@/components/3d/UnfinishedArtifactCanvas").then((mod) => mod.UnfinishedArtifactCanvas),
  {
    ssr: false,
    loading: () => (
      <div className="w-full h-full flex items-center justify-center">
        <div className="w-48 h-48 rounded-lg border border-[#F2F0EA]/10 bg-[#0A0A0A] animate-pulse" />
      </div>
    ),
  }
);

const DISCIPLINE_WORDS = [
  { text: "ENGINEERING", x: "78%", y: "18%", size: "text-lg md:text-2xl", color: "#D4A753", delay: 0.6 },
  { text: "AI", x: "85%", y: "32%", size: "text-4xl md:text-6xl", color: "#5BB8D4", delay: 0.4 },
  { text: "FILM", x: "8%", y: "72%", size: "text-3xl md:text-5xl", color: "#E07A3A", delay: 0.5 },
  { text: "3D", x: "82%", y: "65%", size: "text-5xl md:text-7xl", color: "#94A3B8", delay: 0.3 },
  { text: "WRITING", x: "12%", y: "85%", size: "text-base md:text-xl", color: "#C8C0AE", delay: 0.7 },
  { text: "SYSTEMS", x: "75%", y: "82%", size: "text-sm md:text-lg", color: "#7A7874", delay: 0.8 },
  { text: "CODE", x: "5%", y: "45%", size: "text-sm md:text-base", color: "#8B5CF6", delay: 0.9 },
  { text: "CIPHER", x: "90%", y: "50%", size: "text-xs md:text-sm", color: "#D4C87A", delay: 1.0 },
];

const FLOATING_PROJECTS = [
  { label: "PAGE.OS", x: "68%", y: "20%", width: "w-28 md:w-36", rotation: "-3deg", color: "#4A90D9" },
  { label: "ANE", x: "72%", y: "45%", width: "w-24 md:w-32", rotation: "5deg", color: "#D4A753" },
  { label: "RESIDUAL", x: "15%", y: "28%", width: "w-20 md:w-28", rotation: "-7deg", color: "#E07A3A" },
  { label: "3D / BLENDER", x: "80%", y: "72%", width: "w-22 md:w-30", rotation: "3deg", color: "#94A3B8" },
];

export function HeroSection() {
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const heroRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleMouse = (e: MouseEvent) => {
      if (!heroRef.current) return;
      const rect = heroRef.current.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
      const y = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
      setMousePos({ x, y });
    };
    window.addEventListener("mousemove", handleMouse);
    return () => window.removeEventListener("mousemove", handleMouse);
  }, []);

  return (
    <section
      id="hero"
      ref={heroRef}
      className="relative w-full min-h-screen overflow-hidden bg-[#050505]"
    >
      {/* Background 3D Layer */}
      <div className="absolute inset-0 z-0 opacity-60 md:opacity-80">
        <UnfinishedArtifactCanvas />
      </div>

      {/* Atmospheric overlays */}
      <div className="absolute inset-0 z-[1] bg-gradient-to-b from-[#050505]/30 via-transparent to-[#050505] pointer-events-none" />
      <div className="absolute inset-0 z-[1] bg-[radial-gradient(ellipse_at_30%_50%,rgba(139,92,246,0.06)_0%,transparent_50%)] pointer-events-none" />
      <div className="absolute inset-0 z-[1] bg-[radial-gradient(ellipse_at_70%_30%,rgba(91,184,212,0.04)_0%,transparent_50%)] pointer-events-none" />

      {/* Grid overlay for depth */}
      <div className="absolute inset-0 z-[1] grid-overlay opacity-40 pointer-events-none" />

      {/* === DENSE COMPOSITION === */}
      <div className="hero-content relative z-10 w-full min-h-screen px-6 md:px-12 lg:px-20 py-28 md:py-32">

        {/* Top bar: identity + nav */}
        <div className="flex items-center justify-between mb-12 md:mb-20">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.1 }}
            className="text-[10px] font-mono tracking-[0.25em] text-[#7A7874]"
          >
            MUMBAI, IN — MECHATRONICS & CREATIVE TECH
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] hidden md:block"
          >
            2024 — PRESENT
          </motion.div>
        </div>

        {/* Main composition grid */}
        <div className="hero-main-composition relative w-full" style={{ minHeight: "calc(100vh - 200px)" }}>

          {/* === GIANT NAME — primary visual anchor === */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.2, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            className="hero-name relative z-20"
            style={{
              transform: `translate(${mousePos.x * 5}px, ${mousePos.y * 3}px)`,
            }}
          >
            <h1 className="font-display text-[5rem] sm:text-[7rem] md:text-[9rem] lg:text-[12rem] xl:text-[14rem] font-black text-[#F2F0EA] leading-[0.85] tracking-tight select-none">
              YASH
            </h1>
          </motion.div>

          {/* === ENCLOSED 3D CARD — visual frame containing the artifact === */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 30 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ duration: 1, delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
            className="hero-artifact-card absolute top-[15%] left-[2%] md:left-[5%] w-[280px] h-[200px] md:w-[420px] md:h-[300px] lg:w-[520px] lg:h-[360px] hero-card z-10"
            style={{
              transform: `translate(${mousePos.x * -8}px, ${mousePos.y * -5}px)`,
            }}
          >
            <div className="hero-card-inner w-full h-full flex items-center justify-center">
              <div className="text-[6rem] md:text-[8rem] font-display font-black text-[#8B5CF6]/20 select-none">
                Y
              </div>
            </div>
            {/* Card metadata */}
            <div className="absolute bottom-3 left-4 right-4 flex items-center justify-between">
              <span className="text-[8px] font-mono text-[#7A7874] tracking-wider">01 — IDENTITY</span>
              <span className="text-[8px] font-mono text-[#8B5CF6]">● LIVE</span>
            </div>
          </motion.div>

          {/* === SUBTITLE & FIRST-PERSON COPY — right-aligned, large === */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 1, delay: 0.7, ease: [0.16, 1, 0.3, 1] }}
            className="hero-subtitle absolute top-[8%] right-0 md:right-[2%] w-[280px] md:w-[340px] lg:w-[400px] z-20"
            style={{
              transform: `translate(${mousePos.x * 4}px, ${mousePos.y * 2}px)`,
            }}
          >
            <div className="space-y-2">
              <h2 className="font-heading text-3xl md:text-4xl lg:text-5xl font-bold text-[#F2F0EA] leading-tight">
                I MAKE
                <br />
                THINGS
                <br />
                <span className="text-[#8B5CF6]">THAT CROSS</span>
                <br />
                DISCIPLINES.
              </h2>
            </div>
          </motion.div>

          {/* === BOTTOM LEFT — personal copy === */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.9, delay: 0.9 }}
            className="hero-personal-copy absolute bottom-[25%] left-[2%] md:left-[5%] max-w-sm z-20"
          >
            <p className="text-sm md:text-base text-[#B8B6AF] font-sans leading-relaxed">
              I build things across engineering, software, film, and art.
              Some become projects. Some become experiments. Some become stories.
            </p>
            <div className="mt-6 flex items-center gap-4">
              <a
                href="#work"
                className="px-5 py-2.5 rounded-full bg-[#F2F0EA] text-[#050505] text-xs font-heading font-semibold tracking-wider hover:bg-[#8B5CF6] hover:text-white transition-all duration-300"
              >
                EXPLORE WORK
              </a>
              <a
                href="#me"
                className="text-xs font-mono text-[#7A7874] hover:text-[#F2F0EA] transition-colors tracking-wider"
              >
                ABOUT →
              </a>
            </div>
          </motion.div>

          {/* === BOTTOM RIGHT — metadata === */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 1.1 }}
            className="hero-meta absolute bottom-[25%] right-0 md:right-[2%] text-right z-20"
          >
            <div className="text-[10px] font-mono text-[#7A7874] space-y-1 tracking-wider">
              <p>MECHATRONICS ENGINEER</p>
              <p>SOFTWARE DEVELOPER</p>
              <p>FILMMAKER</p>
              <p>3D ARTIST</p>
              <p>WRITER</p>
            </div>
          </motion.div>

          {/* === FLOATING DISCIPLINE WORDS — scattered at different depths === */}
          {DISCIPLINE_WORDS.map((word, i) => (
            <motion.div
              key={word.text}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 1.2, delay: word.delay }}
              className={`hero-discipline-word absolute font-display font-bold tracking-wider select-none pointer-events-none ${word.size}`}
              style={{
                left: word.x,
                top: word.y,
                color: word.color,
                opacity: 0.08,
                transform: `translate(${mousePos.x * (10 + i * 3)}px, ${mousePos.y * (6 + i * 2)}px)`,
                textShadow: `0 0 80px ${word.color}20`,
              }}
            >
              {word.text}
            </motion.div>
          ))}

          {/* === FLOATING PROJECT PREVIEWS — scattered cards === */}
          {FLOATING_PROJECTS.map((proj, i) => (
            <motion.div
              key={proj.label}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.8, delay: 1.2 + i * 0.15 }}
              className={`hero-project-preview absolute ${proj.width} z-15`}
              style={{
                left: proj.x,
                top: proj.y,
                transform: `rotate(${proj.rotation}) translate(${mousePos.x * (6 + i * 2)}px, ${mousePos.y * (4 + i * 1.5)}px)`,
              }}
            >
              <div
                className="p-3 rounded-lg border backdrop-blur-sm transition-all duration-500 hover:scale-105"
                style={{
                  borderColor: `${proj.color}30`,
                  background: `linear-gradient(135deg, ${proj.color}08, ${proj.color}03)`,
                }}
              >
                <span
                  className="text-[9px] font-mono tracking-wider font-medium"
                  style={{ color: proj.color }}
                >
                  {proj.label}
                </span>
              </div>
            </motion.div>
          ))}
        </div>

        {/* === BOTTOM SCROLL INDICATOR === */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 1.5 }}
          className="absolute bottom-8 left-6 md:left-12 right-6 md:right-12 flex items-center justify-between z-20"
        >
          <span className="text-[10px] font-mono text-[#7A7874] tracking-[0.15em]">
            SCROLL TO EXPLORE
          </span>
          <span className="text-[10px] font-mono text-[#7A7874] tracking-[0.15em]">
            ↓
          </span>
        </motion.div>
      </div>
    </section>
  );
}
