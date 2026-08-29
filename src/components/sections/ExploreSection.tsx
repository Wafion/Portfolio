"use client";

import React, { useRef, useState, useEffect } from "react";
import { motion } from "framer-motion";

/** Discipline collision equations */
const COLLISIONS = [
  { a: "LITERATURE", b: "SOFTWARE", result: "PAGE.OS", colorA: "#C8C0AE", colorB: "#4A90D9", resultColor: "#4A90D9" },
  { a: "AI", b: "AUDIO", result: "ANE", colorA: "#5BB8D4", colorB: "#D4A753", resultColor: "#D4A753" },
  { a: "FILM", b: "DESIGN", result: "RESIDUAL", colorA: "#E07A3A", colorB: "#8B5CF6", resultColor: "#E07A3A" },
  { a: "WRITING", b: "HORROR", result: "A ROOM FOR ONE MORE", colorA: "#C8C0AE", colorB: "#C4565A", resultColor: "#C4565A" },
  { a: "CODE", b: "LANGUAGE", result: "CIPHER", colorA: "#4ADE80", colorB: "#D4C87A", resultColor: "#D4C87A" },
  { a: "3D", b: "ENGINEERING", result: "PROCEDURAL ART", colorA: "#94A3B8", colorB: "#D4A753", resultColor: "#94A3B8" },
];

const INTERESTS = [
  { name: "FILM", x: 8, y: 12, scale: "text-4xl md:text-6xl", color: "#E07A3A", depth: 0.9 },
  { name: "AI", x: 52, y: 8, scale: "text-5xl md:text-7xl", color: "#5BB8D4", depth: 1 },
  { name: "MECHATRONICS", x: 28, y: 32, scale: "text-2xl md:text-4xl", color: "#D4A753", depth: 0.7 },
  { name: "HORROR", x: 62, y: 52, scale: "text-3xl md:text-5xl", color: "#C4565A", depth: 0.85 },
  { name: "WRITING", x: 5, y: 62, scale: "text-2xl md:text-3xl", color: "#C8C0AE", depth: 0.6 },
  { name: "ROBOTICS", x: 38, y: 68, scale: "text-xl md:text-2xl", color: "#D4A753", depth: 0.5 },
  { name: "PHILOSOPHY", x: 70, y: 25, scale: "text-lg md:text-xl", color: "#7A7874", depth: 0.4 },
  { name: "CRYPTOGRAPHY", x: 15, y: 82, scale: "text-base md:text-lg", color: "#D4C87A", depth: 0.35 },
  { name: "3D", x: 78, y: 70, scale: "text-4xl md:text-5xl", color: "#94A3B8", depth: 0.75 },
  { name: "SYSTEMS", x: 48, y: 85, scale: "text-base md:text-lg", color: "#7A7874", depth: 0.3 },
  { name: "TYPOGRAPHY", x: 32, y: 48, scale: "text-base md:text-lg", color: "#C8C0AE", depth: 0.4 },
  { name: "CREATIVE CODING", x: 55, y: 62, scale: "text-sm md:text-base", color: "#4ADE80", depth: 0.45 },
  { name: "ARCHITECTURE", x: 82, y: 40, scale: "text-sm md:text-base", color: "#7A7874", depth: 0.3 },
  { name: "SOFTWARE", x: 18, y: 42, scale: "text-xl md:text-3xl", color: "#4A90D9", depth: 0.65 },
];

function CollisionEquation({ collision, index }: { collision: typeof COLLISIONS[0]; index: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.7, delay: index * 0.08 }}
      className="flex flex-col sm:flex-row items-start sm:items-center gap-3 sm:gap-4 py-5 border-b border-[#F2F0EA]/[0.04] group"
    >
      <span className="font-heading text-lg md:text-xl font-bold" style={{ color: collision.colorA }}>
        {collision.a}
      </span>
      <span className="text-[#7A7874] font-mono text-lg">+</span>
      <span className="font-heading text-lg md:text-xl font-bold" style={{ color: collision.colorB }}>
        {collision.b}
      </span>
      <span className="text-[#7A7874] font-mono text-lg hidden sm:inline">=</span>
      <span className="text-[#7A7874] font-mono text-lg sm:hidden">→</span>
      <span
        className="font-display text-xl md:text-2xl font-bold tracking-wide group-hover:scale-105 transition-transform origin-left"
        style={{ color: collision.resultColor }}
      >
        {collision.result}
      </span>
    </motion.div>
  );
}

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
    <>
      {/* === COLLISION / CROSS-DISCIPLINE SECTION === */}
      <section className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]">
        <div className="max-w-5xl mx-auto">
          <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
            HOW I THINK
          </div>

          <motion.h2
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-4xl sm:text-5xl md:text-6xl font-black text-[#F2F0EA] mb-6 leading-[1.05]"
          >
            INTERSECTIONS
          </motion.h2>

          <p className="text-base text-[#7A7874] max-w-xl font-sans leading-relaxed mb-16">
            My projects emerge from collisions between disciplines. When two fields meet,
            something new appears.
          </p>

          {/* Collision equations */}
          <div className="mb-20">
            {COLLISIONS.map((collision, i) => (
              <CollisionEquation key={i} collision={collision} index={i} />
            ))}
          </div>
        </div>
      </section>

      {/* === SPATIAL INTERESTS FIELD === */}
      <section
        id="explore"
        ref={sectionRef}
        className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
      >
        <div className="max-w-7xl mx-auto">
          <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
            THINGS I EXPLORE
          </div>

          <motion.h2
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-4xl sm:text-5xl md:text-6xl font-black text-[#F2F0EA] mb-6 leading-[1.05]"
          >
            INTERESTS
          </motion.h2>

          <p className="text-base text-[#7A7874] max-w-xl font-sans leading-relaxed mb-16">
            Disciplines at different depths. Some are active projects.
            Some are curiosities. Some are experiments.
          </p>

          {/* Spatial typographic field */}
          <div className="relative w-full h-[450px] md:h-[550px] overflow-hidden rounded-xl border border-[#F2F0EA]/[0.04] bg-[#0A0A0A]/50 grid-overlay">
            {INTERESTS.map((word, index) => {
              const parallaxOffset = scrollProgress * word.depth * 60;
              const opacity = 0.1 + word.depth * 0.7;

              return (
                <motion.div
                  key={word.name}
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 1.2, delay: index * 0.06 }}
                  className={`absolute font-display font-bold tracking-wider select-none transition-opacity duration-300 hover:!opacity-100 cursor-default ${word.scale}`}
                  style={{
                    left: `${word.x}%`,
                    top: `${word.y}%`,
                    color: word.color,
                    opacity: opacity * 0.5,
                    transform: `translateY(${-parallaxOffset}px)`,
                    textShadow: `0 0 80px ${word.color}15`,
                  }}
                >
                  {word.name}
                </motion.div>
              );
            })}

            {/* Depth gradient */}
            <div className="absolute inset-0 bg-gradient-to-b from-[#050505]/50 via-transparent to-[#050505]/70 pointer-events-none" />
          </div>
        </div>
      </section>
    </>
  );
}
