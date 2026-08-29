"use client";

import React, { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";

interface DisciplineWord {
  name: string;
  x: number;
  y: number;
  scale: string;
  color: string;
  depth: number; // 0 = background, 1 = foreground
}

const DISCIPLINES: DisciplineWord[] = [
  { name: "FILM", x: 10, y: 15, scale: "text-4xl md:text-6xl", color: "#D4A753", depth: 0.9 },
  { name: "AI", x: 55, y: 10, scale: "text-5xl md:text-7xl", color: "#5BB8D4", depth: 1 },
  { name: "MECHATRONICS", x: 30, y: 35, scale: "text-3xl md:text-5xl", color: "#B8860B", depth: 0.8 },
  { name: "HORROR", x: 65, y: 55, scale: "text-4xl md:text-5xl", color: "#C4565A", depth: 0.85 },
  { name: "WRITING", x: 8, y: 65, scale: "text-3xl md:text-4xl", color: "#B8B6AF", depth: 0.75 },
  { name: "ROBOTICS", x: 40, y: 70, scale: "text-2xl md:text-4xl", color: "#8B7355", depth: 0.6 },
  { name: "PHILOSOPHY", x: 72, y: 28, scale: "text-xl md:text-3xl", color: "#7A7874", depth: 0.5 },
  { name: "CRYPTOGRAPHY", x: 18, y: 85, scale: "text-lg md:text-2xl", color: "#D4C87A", depth: 0.4 },
  { name: "3D", x: 80, y: 75, scale: "text-3xl md:text-5xl", color: "#6B9FD4", depth: 0.7 },
  { name: "SYSTEMS", x: 50, y: 88, scale: "text-lg md:text-2xl", color: "#7A7874", depth: 0.45 },
  { name: "TYPOGRAPHY", x: 35, y: 50, scale: "text-lg md:text-2xl", color: "#B8B6AF", depth: 0.4 },
  { name: "PHYSICS", x: 78, y: 45, scale: "text-base md:text-xl", color: "#7A7874", depth: 0.35 },
  { name: "CREATIVE CODING", x: 55, y: 65, scale: "text-lg md:text-xl", color: "#5BAA8A", depth: 0.55 },
  { name: "ARCHITECTURE", x: 85, y: 60, scale: "text-base md:text-lg", color: "#7A7874", depth: 0.3 },
  { name: "FILMMAKING", x: 25, y: 45, scale: "text-xl md:text-3xl", color: "#D4A753", depth: 0.65 },
];

export function ExploreSection() {
  const [scrollProgress, setScrollProgress] = useState(0);
  const sectionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleScroll = () => {
      if (!sectionRef.current) return;
      const rect = sectionRef.current.getBoundingClientRect();
      const sectionHeight = sectionRef.current.offsetHeight;
      const progress = Math.max(0, Math.min(1, -rect.top / (sectionHeight - window.innerHeight)));
      setScrollProgress(progress);
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <section
      id="explore"
      ref={sectionRef}
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
    >
      <div className="max-w-7xl mx-auto">
        {/* Section header */}
        <div className="mb-20">
          <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.2em] mb-6">
            03 — THINGS I EXPLORE
          </div>
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-4xl sm:text-5xl md:text-6xl font-bold text-[#F2F0EA]"
          >
            INTERESTS
          </motion.h2>
          <p className="mt-4 text-base text-[#7A7874] max-w-xl font-sans leading-relaxed">
            Disciplines do not live in isolated silos. These are the intellectual currents that
            inform and cross-pollinate each other.
          </p>
        </div>

        {/* Spatial typographic landscape */}
        <div className="relative w-full h-[500px] md:h-[600px] overflow-hidden rounded-xl border border-[#F2F0EA]/[0.04] bg-[#0B0B0C]/50">
          {DISCIPLINES.map((word, index) => {
            const parallaxOffset = scrollProgress * word.depth * 80;
            const opacity = 0.15 + word.depth * 0.85;

            return (
              <motion.div
                key={word.name}
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 1.2, delay: index * 0.08 }}
                className={`absolute font-display font-bold tracking-wider select-none transition-opacity duration-300 hover:!opacity-100 cursor-default ${word.scale}`}
                style={{
                  left: `${word.x}%`,
                  top: `${word.y}%`,
                  color: word.color,
                  opacity: opacity * 0.6,
                  transform: `translateY(${-parallaxOffset}px)`,
                  textShadow: `0 0 60px ${word.color}15`,
                }}
              >
                {word.name}
              </motion.div>
            );
          })}

          {/* Depth gradient overlay */}
          <div className="absolute inset-0 bg-gradient-to-b from-[#050505]/60 via-transparent to-[#050505]/80 pointer-events-none" />
        </div>

        {/* Category breakdown */}
        <div className="mt-16 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-6">
          {[
            { label: "ENGINEERING", color: "#B8860B" },
            { label: "SOFTWARE & AI", color: "#5BB8D4" },
            { label: "CINEMA & ART", color: "#D4A753" },
            { label: "WRITING & STORY", color: "#B8B6AF" },
            { label: "PHILOSOPHY & SYSTEMS", color: "#7A7874" },
          ].map((cat) => (
            <div key={cat.label} className="space-y-2">
              <div className="flex items-center gap-2">
                <div
                  className="w-1.5 h-1.5 rounded-full"
                  style={{ backgroundColor: cat.color }}
                />
                <span
                  className="text-[9px] font-mono tracking-[0.2em]"
                  style={{ color: cat.color }}
                >
                  {cat.label}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
