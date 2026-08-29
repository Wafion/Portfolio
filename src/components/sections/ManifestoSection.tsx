"use client";

import React from "react";
import { motion } from "framer-motion";
import { CipherLab } from "@/components/sections/CipherLabSection";
import { CreativeCodingCanvas } from "@/components/sections/CreativeCodingSection";

export function ExperimentsSection() {
  return (
    <section
      id="experiments"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
    >
      <div className="max-w-7xl mx-auto">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
          EXPERIMENTS
        </div>

        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black text-[#F2F0EA] leading-[0.95] mb-6"
        >
          LAB
        </motion.h2>

        <p className="text-base text-[#7A7874] max-w-xl font-sans leading-relaxed mb-20">
          Playful, experimental work — where mathematics becomes visual and language becomes geometry.
        </p>

        {/* Cipher Lab */}
        <motion.div
          initial={{ opacity: 0, y: 25 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.8 }}
          className="mb-24"
        >
          <div className="mb-8">
            <div className="text-[10px] font-mono text-[#D4C87A] tracking-[0.25em] mb-3">
              CIPHER LAB
            </div>
            <h3 className="font-display text-2xl sm:text-3xl md:text-4xl font-bold text-[#F2F0EA] mb-2">
              THE CIPHER
            </h3>
            <p className="text-sm text-[#7A7874] font-sans max-w-xl leading-relaxed">
              An experimental visual cipher and custom glyph system. A proprietary 26-character
              geometric alphabet designed on a 24×24 orthogonal grid.
            </p>
          </div>
          <CipherLab />
        </motion.div>

        {/* Creative Coding */}
        <motion.div
          initial={{ opacity: 0, y: 25 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.8 }}
        >
          <div className="mb-8">
            <div className="text-[10px] font-mono text-[#4ADE80] tracking-[0.25em] mb-3">
              GENERATIVE SKETCHES
            </div>
            <h3 className="font-display text-2xl sm:text-3xl md:text-4xl font-bold text-[#F2F0EA] mb-2">
              CREATIVE CODING
            </h3>
            <p className="text-sm text-[#7A7874] font-sans max-w-xl leading-relaxed">
              Mathematical simulations, vector flow fields, and audio harmonic curves on canvas.
              Move your cursor to disturb the force vectors.
            </p>
          </div>
          <CreativeCodingCanvas />
        </motion.div>
      </div>
    </section>
  );
}
