"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { EXHIBITION_PROJECTS, ExhibitionProject } from "@/lib/data/projects";
import { sound } from "@/components/audio/SoundEngine";

interface WorkSectionProps {
  onSelectProject: (project: ExhibitionProject) => void;
}

/** Each project gets a completely different visual treatment */
const PROJECT_WORLDS: Record<
  string,
  {
    bg: string;
    accent: string;
    visualStyle: "contained" | "waveform" | "cinematic" | "corridor" | "manuscript" | "sculptural" | "glyph" | "generative";
  }
> = {
  "page-os": {
    bg: "from-[#0B1020] to-[#060810]",
    accent: "#4A90D9",
    visualStyle: "contained",
  },
  ane: {
    bg: "from-[#100D05] to-[#0A0804]",
    accent: "#D4A753",
    visualStyle: "waveform",
  },
  residual: {
    bg: "from-[#0D0A08] to-[#080605]",
    accent: "#E07A3A",
    visualStyle: "cinematic",
  },
  "the-fifth-exit": {
    bg: "from-[#12080A] to-[#080405]",
    accent: "#C4565A",
    visualStyle: "corridor",
  },
  "a-room-for-one-more": {
    bg: "from-[#12100C] to-[#0C0A08]",
    accent: "#C8C0AE",
    visualStyle: "manuscript",
  },
  "blender-3d": {
    bg: "from-[#080A10] to-[#040608]",
    accent: "#94A3B8",
    visualStyle: "sculptural",
  },
  "cipher-system": {
    bg: "from-[#100E06] to-[#0A0904]",
    accent: "#D4C87A",
    visualStyle: "glyph",
  },
  "creative-coding": {
    bg: "from-[#060E0A] to-[#040A06]",
    accent: "#4ADE80",
    visualStyle: "generative",
  },
};

/** Visual elements unique to each project style */
function ProjectVisual({ project, world }: { project: ExhibitionProject; world: typeof PROJECT_WORLDS[string] }) {
  switch (world.visualStyle) {
    case "contained":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl border border-[#4A90D9]/20 overflow-hidden bg-[#0B1020]">
          {/* Browser chrome lines */}
          <div className="flex items-center gap-2 px-4 py-3 border-b border-[#4A90D9]/10">
            <div className="flex gap-1.5">
              <div className="w-2.5 h-2.5 rounded-full bg-[#4A90D9]/30" />
              <div className="w-2.5 h-2.5 rounded-full bg-[#4A90D9]/20" />
              <div className="w-2.5 h-2.5 rounded-full bg-[#4A90D9]/15" />
            </div>
            <div className="flex-1 mx-4 h-5 rounded bg-[#4A90D9]/5 border border-[#4A90D9]/10 flex items-center px-3">
              <span className="text-[8px] font-mono text-[#4A90D9]/40">page-os.app</span>
            </div>
          </div>
          {/* Interface preview */}
          <div className="p-6 space-y-4">
            <div className="h-4 w-1/3 rounded bg-[#4A90D9]/10" />
            <div className="grid grid-cols-3 gap-3">
              {[1, 2, 3].map((i) => (
                <div key={i} className="aspect-[3/4] rounded bg-[#4A90D9]/[0.04] border border-[#4A90D9]/10 p-3">
                  <div className="h-2 w-2/3 rounded bg-[#4A90D9]/10 mb-2" />
                  <div className="h-1 w-full rounded bg-[#4A90D9]/5 mb-1" />
                  <div className="h-1 w-4/5 rounded bg-[#4A90D9]/5" />
                </div>
              ))}
            </div>
            <div className="h-24 rounded bg-[#4A90D9]/[0.03] border border-[#4A90D9]/8 flex items-center justify-center">
              <span className="text-[10px] font-mono text-[#4A90D9]/20">READING INTERFACE</span>
            </div>
          </div>
        </div>
      );

    case "waveform":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl border border-[#D4A753]/20 overflow-hidden bg-[#100D05]">
          <div className="absolute inset-0 flex items-center justify-center">
            {/* Waveform visualization */}
            <svg className="w-full h-full opacity-30" viewBox="0 0 800 200">
              {Array.from({ length: 80 }).map((_, i) => {
                const h = Math.sin(i * 0.3) * 40 + Math.random() * 30 + 20;
                return (
                  <rect
                    key={i}
                    x={i * 10}
                    y={100 - h / 2}
                    width={6}
                    height={h}
                    fill="#D4A753"
                    opacity={0.3 + Math.sin(i * 0.2) * 0.3}
                    rx={1}
                  />
                );
              })}
            </svg>
          </div>
          <div className="absolute inset-0 flex flex-col items-center justify-center z-10">
            <div className="text-[4rem] md:text-[5rem] font-display font-black text-[#D4A753]/15 select-none">
              ANE
            </div>
            <div className="text-[10px] font-mono text-[#D4A753]/40 tracking-widest mt-2">
              AUDIO NARRATIVE ENGINE
            </div>
          </div>
          {/* Neural structure overlay */}
          <div className="absolute top-4 right-4 w-20 h-20 border border-[#D4A753]/10 rounded-full" />
          <div className="absolute top-6 right-6 w-16 h-16 border border-[#D4A753]/8 rounded-full" />
          <div className="absolute top-8 right-8 w-12 h-12 border border-[#D4A753]/5 rounded-full" />
        </div>
      );

    case "cinematic":
      return (
        <div className="relative w-full aspect-[21/9] rounded-xl overflow-hidden bg-[#0D0A08]">
          {/* Cinematic letterbox frame */}
          <div className="absolute inset-0 flex flex-col">
            <div className="h-[15%] bg-black" />
            <div className="flex-1 relative">
              <div className="absolute inset-0 bg-gradient-to-r from-[#E07A3A]/10 via-transparent to-[#E07A3A]/5" />
              {/* Film frame lines */}
              <div className="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-[#E07A3A]/10 to-transparent" />
              <div className="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-[#E07A3A]/10 to-transparent" />
              {/* Sprocket holes */}
              <div className="absolute left-1 top-0 bottom-0 flex flex-col justify-evenly">
                {Array.from({ length: 8 }).map((_, i) => (
                  <div key={i} className="w-2 h-3 rounded-sm bg-black/50" />
                ))}
              </div>
              {/* Center composition */}
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-[3rem] md:text-[4rem] font-display italic text-[#E07A3A]/20 select-none">
                  RESIDUAL
                </div>
              </div>
            </div>
            <div className="h-[15%] bg-black" />
          </div>
          {/* Frame number */}
          <div className="absolute bottom-[16%] right-6 text-[8px] font-mono text-[#E07A3A]/30">
            24A — 2.39:1
          </div>
        </div>
      );

    case "corridor":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl overflow-hidden bg-[#12080A]">
          {/* Corridor perspective lines */}
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="relative w-full h-full">
              {/* Perspective lines converging to center */}
              <div className="absolute left-0 top-0 w-full h-full">
                <div className="absolute left-[20%] top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-[#C4565A]/15 to-transparent transform -skew-x-[5deg]" />
                <div className="absolute right-[20%] top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-[#C4565A]/15 to-transparent transform skew-x-[5deg]" />
                <div className="absolute left-[35%] top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-[#C4565A]/10 to-transparent transform -skew-x-[3deg]" />
                <div className="absolute right-[35%] top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-[#C4565A]/10 to-transparent transform skew-x-[3deg]" />
              </div>
              {/* Vanishing point */}
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-px h-32 bg-gradient-to-b from-transparent via-[#C4565A]/25 to-transparent" />
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 h-px w-32 bg-gradient-to-r from-transparent via-[#C4565A]/25 to-transparent" />
              {/* Door frames */}
              <div className="absolute top-[20%] left-[25%] right-[25%] bottom-[20%] border border-[#C4565A]/8 rounded-sm" />
              <div className="absolute top-[30%] left-[30%] right-[30%] bottom-[30%] border border-[#C4565A]/12 rounded-sm" />
              <div className="absolute top-[38%] left-[37%] right-[37%] bottom-[38%] border border-[#C4565A]/18 rounded-sm" />
            </div>
          </div>
          <div className="absolute bottom-6 left-6 text-[10px] font-mono text-[#C4565A]/40 tracking-wider">
            THE FIFTH EXIT — FIVE ROOMS
          </div>
        </div>
      );

    case "manuscript":
      return (
        <div className="relative w-full aspect-[3/4] md:aspect-[4/5] rounded-xl overflow-hidden bg-[#1A1816] border border-[#C8C0AE]/10">
          {/* Paper texture */}
          <div className="absolute inset-0 bg-gradient-to-b from-[#1A1816] via-[#16140E] to-[#12100C]" />
          {/* Page content */}
          <div className="relative p-8 md:p-12 space-y-6">
            {/* Title */}
            <div className="text-center">
              <p className="text-[8px] font-mono text-[#C8C0AE]/30 tracking-[0.3em] mb-4">MANUSCRIPT</p>
              <h3 className="font-serif text-3xl md:text-4xl text-[#C8C0AE]/80 italic leading-tight">
                A Room for One More
              </h3>
            </div>
            {/* Protagonist */}
            <p className="text-center text-[9px] font-mono text-[#C8C0AE]/25 tracking-wider">
              IRA ELOWEN MIREILLE
            </p>
            {/* Simulated manuscript lines */}
            <div className="space-y-3 mt-8">
              {Array.from({ length: 12 }).map((_, i) => (
                <div
                  key={i}
                  className="h-px bg-[#C8C0AE]/[0.06]"
                  style={{ width: `${60 + Math.sin(i) * 20}%`, marginLeft: i % 3 === 0 ? "0" : "5%" }}
                />
              ))}
            </div>
            {/* Marginal note */}
            <div className="absolute top-16 right-6 text-[7px] font-serif italic text-[#C8C0AE]/15 transform rotate-90 origin-right">
              unreliable narrator
            </div>
            {/* Page edge shadow */}
            <div className="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-black/20 to-transparent" />
          </div>
        </div>
      );

    case "sculptural":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl border border-[#94A3B8]/10 overflow-hidden bg-[#080A10]">
          {/* Wireframe geometric forms */}
          <div className="absolute inset-0 flex items-center justify-center">
            <svg className="w-48 h-48 md:w-64 md:h-64 opacity-20" viewBox="0 0 200 200">
              {/* Octahedron wireframe */}
              <polygon points="100,10 190,100 100,190 10,100" fill="none" stroke="#94A3B8" strokeWidth="0.5" />
              <line x1="100" y1="10" x2="100" y2="190" stroke="#94A3B8" strokeWidth="0.3" />
              <line x1="10" y1="100" x2="190" y2="100" stroke="#94A3B8" strokeWidth="0.3" />
              {/* Inner forms */}
              <polygon points="100,40 160,100 100,160 40,100" fill="none" stroke="#94A3B8" strokeWidth="0.3" />
              <circle cx="100" cy="100" r="30" fill="none" stroke="#94A3B8" strokeWidth="0.2" />
            </svg>
          </div>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-[3rem] md:text-[4rem] font-display font-bold text-[#94A3B8]/10 select-none">
              3D
            </div>
          </div>
          <div className="absolute bottom-4 left-4 text-[9px] font-mono text-[#94A3B8]/30 tracking-wider">
            PROCEDURAL GEOMETRY — BLENDER
          </div>
        </div>
      );

    case "glyph":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl border border-[#D4C87A]/10 overflow-hidden bg-[#100E06]">
          {/* Glyph grid */}
          <div className="absolute inset-0 p-6 grid grid-cols-6 md:grid-cols-8 gap-2 place-items-center opacity-30">
            {Array.from({ length: 26 }).map((_, i) => {
              const char = String.fromCharCode(65 + i);
              return (
                <div
                  key={char}
                  className="w-6 h-6 md:w-8 md:h-8 border border-[#D4C87A]/15 rounded flex items-center justify-center"
                >
                  <span className="text-[8px] font-mono text-[#D4C87A]/40">{char}</span>
                </div>
              );
            })}
          </div>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
              <div className="text-[2.5rem] md:text-[3.5rem] font-display font-black text-[#D4C87A]/15 select-none">
                CIPHER
              </div>
              <div className="text-[8px] font-mono text-[#D4C87A]/25 tracking-[0.3em] mt-2">
                24 × 24 ORTHOGONAL GRID
              </div>
            </div>
          </div>
        </div>
      );

    case "generative":
      return (
        <div className="relative w-full aspect-[16/10] rounded-xl border border-[#4ADE80]/10 overflow-hidden bg-[#060E0A]">
          {/* Particle field */}
          <div className="absolute inset-0">
            {Array.from({ length: 40 }).map((_, i) => (
              <div
                key={i}
                className="absolute w-1 h-1 rounded-full bg-[#4ADE80]/30"
                style={{
                  left: `${10 + Math.random() * 80}%`,
                  top: `${10 + Math.random() * 80}%`,
                  animationDelay: `${i * 0.1}s`,
                }}
              />
            ))}
          </div>
          {/* Flow field lines */}
          <svg className="absolute inset-0 w-full h-full opacity-15" viewBox="0 0 400 250">
            {Array.from({ length: 20 }).map((_, i) => {
              const x1 = Math.random() * 400;
              const y1 = Math.random() * 250;
              const x2 = x1 + (Math.random() - 0.5) * 100;
              const y2 = y1 + (Math.random() - 0.5) * 100;
              return (
                <line
                  key={i}
                  x1={x1} y1={y1} x2={x2} y2={y2}
                  stroke="#4ADE80"
                  strokeWidth="0.5"
                  opacity={0.3 + Math.random() * 0.4}
                />
              );
            })}
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-[2.5rem] md:text-[3.5rem] font-display font-bold text-[#4ADE80]/10 select-none">
              CODE
            </div>
          </div>
        </div>
      );
  }
}

export function WorkSection({ onSelectProject }: WorkSectionProps) {
  const [hoveredProject, setHoveredProject] = useState<string | null>(null);

  return (
    <section
      id="work"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
    >
      <div className="max-w-7xl mx-auto">
        {/* Section header — large, editorial */}
        <div className="mb-20">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.8 }}
            className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8"
          >
            WORK — SELECTED PROJECTS
          </motion.div>

          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8">
            <motion.h2
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-100px" }}
              transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
              className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black text-[#F2F0EA] leading-[0.95]"
            >
              THE
              <br />
              WORK.
            </motion.h2>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-80px" }}
              transition={{ duration: 0.8, delay: 0.1 }}
              className="text-base text-[#7A7874] max-w-md font-sans leading-relaxed lg:text-right"
            >
              Each project is its own world. Software, AI, film, horror, writing,
              3D, cryptography, generative systems — all emerging from the intersections.
            </motion.p>
          </div>
        </div>

        {/* === PROJECT WORLDS — each project gets unique visual composition === */}
        <div className="space-y-12 md:space-y-20">
          {EXHIBITION_PROJECTS.map((project, index) => {
            const world = PROJECT_WORLDS[project.id] || PROJECT_WORLDS["page-os"];
            const isEven = index % 2 === 0;
            const isLarge = project.id === "page-os" || project.id === "the-fifth-exit";

            return (
              <motion.div
                key={project.id}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-60px" }}
                transition={{ duration: 0.8, delay: 0.1 }}
                onMouseEnter={() => {
                  setHoveredProject(project.id);
                  sound.playSoftClick(500);
                }}
                onMouseLeave={() => setHoveredProject(null)}
                onClick={() => onSelectProject(project)}
                className={`cursor-pointer group ${isLarge ? "grid grid-cols-1 lg:grid-cols-12 gap-8" : ""}`}
              >
                {isLarge ? (
                  <>
                    {/* Large layout: visual takes 7 cols, info takes 5 */}
                    <div className={`${isEven ? "lg:col-span-7" : "lg:col-span-5 lg:order-2"}`}>
                      <ProjectVisual project={project} world={world} />
                    </div>
                    <div className={`lg:col-span-5 flex flex-col justify-center ${isEven ? "" : "lg:order-1"}`}>
                      <div className="space-y-4">
                        <div className="flex items-center gap-3">
                          <span
                            className="w-2 h-2 rounded-full"
                            style={{ backgroundColor: world.accent }}
                          />
                          <span
                            className="text-[10px] font-mono tracking-[0.2em]"
                            style={{ color: world.accent }}
                          >
                            {project.material}
                          </span>
                          <span className="text-[9px] font-mono text-[#7A7874]">#{project.number}</span>
                        </div>
                        <h3 className="font-display text-3xl sm:text-4xl md:text-5xl font-bold text-[#F2F0EA] leading-tight group-hover:text-[#8B5CF6] transition-colors duration-500">
                          {project.title}
                        </h3>
                        <p className="text-xs font-mono text-[#7A7874] tracking-wider uppercase">
                          {project.subtitle}
                        </p>
                        <p className="text-sm text-[#B8B6AF] font-sans leading-relaxed">
                          {project.summary}
                        </p>
                        <div className="p-4 rounded-lg bg-[#0A0A0A] border border-[#F2F0EA]/[0.04]">
                          <p className="text-xs italic text-[#7A7874] font-serif leading-relaxed">
                            &ldquo;{project.tagline}&rdquo;
                          </p>
                        </div>
                        <div className="flex items-center gap-2 pt-2">
                          <span className="text-[9px] font-mono text-[#7A7874]">{project.status}</span>
                          <span className="text-[#7A7874]">·</span>
                          <span className="text-[9px] font-mono text-[#7A7874]">{project.year}</span>
                        </div>
                        <div className="flex flex-wrap gap-1.5 pt-1">
                          {project.technologies.slice(0, 4).map((t, i) => (
                            <span
                              key={i}
                              className="px-2 py-0.5 rounded text-[8px] font-mono border"
                              style={{
                                color: `${world.accent}90`,
                                borderColor: `${world.accent}20`,
                                backgroundColor: `${world.accent}08`,
                              }}
                            >
                              {t}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </>
                ) : (
                  /* Compact layout: visual + info side by side */
                  <div className={`grid grid-cols-1 md:grid-cols-12 gap-6 items-center ${isEven ? "" : "md:flex md:flex-row-reverse"}`}>
                    <div className={`md:col-span-7 ${!isEven ? "md:order-2" : ""}`}>
                      <ProjectVisual project={project} world={world} />
                    </div>
                    <div className={`md:col-span-5 ${!isEven ? "md:order-1" : ""}`}>
                      <div className="space-y-3">
                        <div className="flex items-center gap-3">
                          <span
                            className="w-1.5 h-1.5 rounded-full"
                            style={{ backgroundColor: world.accent }}
                          />
                          <span
                            className="text-[9px] font-mono tracking-[0.2em]"
                            style={{ color: world.accent }}
                          >
                            {project.material}
                          </span>
                        </div>
                        <h3 className="font-display text-2xl sm:text-3xl font-bold text-[#F2F0EA] group-hover:text-[#8B5CF6] transition-colors duration-500">
                          {project.title}
                        </h3>
                        <p className="text-xs text-[#7A7874] font-sans leading-relaxed">
                          {project.summary}
                        </p>
                        <div className="flex items-center gap-2 pt-1">
                          <span className="text-[8px] font-mono text-[#7A7874]">{project.status}</span>
                          <span className="text-[8px] font-mono text-[#7A7874]">·</span>
                          <span className="text-[8px] font-mono text-[#7A7874]">{project.year}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                )}
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
