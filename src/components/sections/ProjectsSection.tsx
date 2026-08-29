"use client";

import React from "react";
import { motion } from "framer-motion";

export function CurrentlySection() {
  const items = [
    { title: "PAGE.OS", status: "BUILDING", note: "Refining semantic passage clustering and offline EPUB parsing. The Infinity discovery mode is the current focus.", color: "#4A90D9" },
    { title: "ANE", status: "EXPLORING", note: "Fine-tuning the narrative classifier and experimenting with local inference pipelines.", color: "#D4A753" },
    { title: "AI EXPERIMENTS", status: "EXPLORING", note: "Working with local language models, agentic workflows, and understanding how small models reason.", color: "#5BB8D4" },
    { title: "3D ART", status: "EXPERIMENTING", note: "Procedural geometry nodes in Blender. Exploring how micro-displacement and volumetric scattering create weight.", color: "#94A3B8" },
    { title: "FILM", status: "DEVELOPING", note: "Previs work for The Fifth Exit. Architecting brutalist corridor layouts and binaural audio treatment.", color: "#C4565A" },
    { title: "WRITING", status: "WRITING", note: "A Room for One More manuscript. Working through the middle chapters where Ira's perception begins to fracture.", color: "#C8C0AE" },
  ];

  return (
    <section
      id="currently"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#0A0A0A]"
    >
      <div className="max-w-5xl mx-auto">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
          CURRENTLY
        </div>

        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black text-[#F2F0EA] leading-[0.95] mb-6"
        >
          NOW.
        </motion.h2>

        <p className="text-base text-[#7A7874] max-w-xl font-sans leading-relaxed mb-16">
          What I am actively working on or exploring right now.
        </p>

        {/* Active items — compact, visual */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {items.map((item, i) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-40px" }}
              transition={{ duration: 0.6, delay: i * 0.05 }}
              className="p-6 rounded-xl bg-[#050505]/60 border border-[#F2F0EA]/[0.04] hover:border-[#F2F0EA]/[0.08] transition-colors duration-300"
            >
              <div className="flex items-center gap-3 mb-3">
                <div className="w-2 h-2 rounded-full" style={{ backgroundColor: item.color }} />
                <h3 className="font-display text-lg font-bold text-[#F2F0EA]">{item.title}</h3>
              </div>
              <span className="text-[9px] font-mono tracking-[0.2em] uppercase mb-2 inline-block" style={{ color: item.color }}>
                {item.status}
              </span>
              <p className="text-sm text-[#7A7874] font-sans leading-relaxed">
                {item.note}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
