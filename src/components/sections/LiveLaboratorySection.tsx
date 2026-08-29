"use client";

import React from "react";
import { motion } from "framer-motion";

export function MakeSection() {
  const disciplines = [
    {
      title: "FILM",
      subtitle: "UNDER THE RESIDUAL IDENTITY",
      color: "#E07A3A",
      description:
        "I direct short films and explore visual restraint, deep contrast, and atmospheric silence. Every frame should earn its place.",
      details: [
        "Directing & visual previs in Blender",
        "Low-key lighting & deep shadow falloff",
        "Anamorphic 2.39:1 framing",
        "ACES color management in DaVinci Resolve",
        "Binaural spatial sound design",
      ],
      /* Horizontal film-strip visual */
      visual: (
        <div className="relative w-full aspect-[21/9] rounded-xl overflow-hidden bg-[#0D0A08]">
          <div className="absolute inset-0 flex items-stretch">
            {/* Film strip frames */}
            {[1, 2, 3, 4].map((i) => (
              <div
                key={i}
                className="flex-1 relative border-r border-black/30"
                style={{
                  background: `linear-gradient(${135 + i * 30}deg, ${i % 2 === 0 ? "#1A1510" : "#0F0C08"}, ${i % 2 === 0 ? "#0F0C08" : "#1A1510"})`,
                }}
              >
                {/* Simulated film frame content */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="text-[1.5rem] md:text-[2rem] font-display italic text-[#E07A3A]/10 select-none">
                    {["RES", "IDU", "AL", "."][i - 1]}
                  </div>
                </div>
                {/* Sprocket holes */}
                <div className="absolute left-1 top-2 bottom-2 flex flex-col justify-evenly">
                  {Array.from({ length: 6 }).map((_, j) => (
                    <div key={j} className="w-1.5 h-2 rounded-sm bg-black/40" />
                  ))}
                </div>
                <div className="absolute right-1 top-2 bottom-2 flex flex-col justify-evenly">
                  {Array.from({ length: 6 }).map((_, j) => (
                    <div key={j} className="w-1.5 h-2 rounded-sm bg-black/40" />
                  ))}
                </div>
                {/* Frame number */}
                <div className="absolute bottom-2 right-3 text-[7px] font-mono text-[#E07A3A]/20">
                  {String(i + 23).padStart(2, "0")}
                </div>
              </div>
            ))}
          </div>
          {/* Film metadata overlay */}
          <div className="absolute bottom-3 left-4 right-4 flex items-center justify-between">
            <span className="text-[8px] font-mono text-[#E07A3A]/30 tracking-wider">KODAK VISION3 500T</span>
            <span className="text-[8px] font-mono text-[#E07A3A]/30">2.39:1 ANAMORPHIC</span>
          </div>
        </div>
      ),
    },
    {
      title: "3D",
      subtitle: "BLENDER · PROCEDURAL · CYCLES",
      color: "#94A3B8",
      description:
        "I use Blender as a spatial sketchbook — procedural shaders, brutalist forms, and volumetric light physics.",
      details: [
        "Procedural geometry nodes",
        "Cycles raytraced volumetric scattering",
        "Monolithic architectural forms",
        "Atmospheric fog & caustics",
        "Light studies & material experiments",
      ],
      visual: (
        <div className="relative w-full aspect-[16/9] rounded-xl overflow-hidden bg-[#080A10]">
          {/* 3D wireframe composition */}
          <div className="absolute inset-0 flex items-center justify-center">
            <svg className="w-64 h-64 md:w-80 md:h-80 opacity-15" viewBox="0 0 300 300">
              {/* Large octahedron */}
              <polygon points="150,20 280,150 150,280 20,150" fill="none" stroke="#94A3B8" strokeWidth="0.6" />
              <line x1="150" y1="20" x2="150" y2="280" stroke="#94A3B8" strokeWidth="0.3" />
              <line x1="20" y1="150" x2="280" y2="150" stroke="#94A3B8" strokeWidth="0.3" />
              {/* Inner octahedron */}
              <polygon points="150,60 240,150 150,240 60,150" fill="none" stroke="#94A3B8" strokeWidth="0.4" />
              {/* Circles */}
              <circle cx="150" cy="150" r="60" fill="none" stroke="#94A3B8" strokeWidth="0.2" />
              <circle cx="150" cy="150" r="90" fill="none" stroke="#94A3B8" strokeWidth="0.15" />
              {/* Connecting lines */}
              <line x1="150" y1="20" x2="240" y2="150" stroke="#94A3B8" strokeWidth="0.15" />
              <line x1="150" y1="20" x2="60" y2="150" stroke="#94A3B8" strokeWidth="0.15" />
              <line x1="280" y1="150" x2="150" y2="240" stroke="#94A3B8" strokeWidth="0.15" />
              <line x1="20" y1="150" x2="150" y2="240" stroke="#94A3B8" strokeWidth="0.15" />
            </svg>
          </div>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-[3rem] md:text-[4rem] font-display font-bold text-[#94A3B8]/10 select-none">
              GEOMETRY
            </div>
          </div>
          <div className="absolute bottom-4 left-4 text-[9px] font-mono text-[#94A3B8]/30 tracking-wider">
            BLENDER CYCLES — PROCEDURAL NODES
          </div>
        </div>
      ),
    },
  ];

  return (
    <section
      id="make"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
    >
      <div className="max-w-7xl mx-auto">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
          THINGS I MAKE
        </div>

        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black text-[#F2F0EA] leading-[0.95] mb-6"
        >
          MAKE
        </motion.h2>

        <p className="text-base text-[#7A7874] max-w-xl font-sans leading-relaxed mb-20">
          Film, 3D, motion, and visual storytelling. More cinematic, larger imagery,
          more negative space.
        </p>

        {/* Discipline blocks — large, cinematic */}
        <div className="space-y-24">
          {disciplines.map((d, i) => (
            <motion.div
              key={d.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.8, delay: i * 0.1 }}
            >
              {/* Visual — full width, cinematic */}
              <div className="mb-10">{d.visual}</div>

              {/* Content — asymmetric */}
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                <div className="lg:col-span-5">
                  <div
                    className="text-[10px] font-mono tracking-[0.25em] mb-3"
                    style={{ color: d.color }}
                  >
                    {d.subtitle}
                  </div>
                  <h3 className="font-display text-3xl sm:text-4xl font-bold text-[#F2F0EA]">
                    {d.title}
                  </h3>
                </div>
                <div className="lg:col-span-7 space-y-4">
                  <p className="text-base text-[#B8B6AF] font-sans leading-relaxed max-w-lg">
                    {d.description}
                  </p>
                  <ul className="space-y-2">
                    {d.details.map((detail, j) => (
                      <li key={j} className="flex items-start gap-3 text-sm text-[#7A7874] font-sans">
                        <span className="mt-1.5 w-1 h-1 rounded-full flex-shrink-0" style={{ backgroundColor: d.color }} />
                        {detail}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
