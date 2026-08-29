"use client";

import React from "react";
import { motion } from "framer-motion";

export function AboutMeSection() {
  return (
    <section
      id="me"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505]"
    >
      <div className="max-w-7xl mx-auto">
        {/* Section index */}
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-16">
          ABOUT
        </div>

        {/* Giant editorial headline — the visual IS the typography */}
        <motion.h2
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
          className="font-display text-[3.5rem] sm:text-[5rem] md:text-[6.5rem] lg:text-[8rem] font-black text-[#F2F0EA] leading-[0.92] tracking-tight mb-16"
        >
          I LIKE
          <br />
          TAKING
          <br />
          <span className="text-[#8B5CF6]">THINGS</span>
          <br />
          APART.
        </motion.h2>

        {/* Content grid — asymmetric, two columns */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20">
          {/* Left — list of deconstructed things */}
          <motion.div
            initial={{ opacity: 0, y: 25 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.8, delay: 0.15 }}
            className="lg:col-span-4"
          >
            <div className="space-y-4 pl-6 border-l-2 border-[#8B5CF6]/30">
              {["Machines.", "Software.", "Interfaces.", "Stories.", "Systems."].map((item, i) => (
                <motion.p
                  key={item}
                  initial={{ opacity: 0, x: -15 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: 0.2 + i * 0.08 }}
                  className="text-2xl sm:text-3xl md:text-4xl font-serif text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors cursor-default"
                >
                  {item}
                </motion.p>
              ))}
            </div>

            <motion.p
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, delay: 0.5 }}
              className="mt-8 text-lg sm:text-xl italic text-[#7A7874] font-serif leading-relaxed"
            >
              Sometimes because I want to understand them.
              <br />
              Sometimes because I want to make something different from them.
            </motion.p>
          </motion.div>

          {/* Right — personal narrative */}
          <motion.div
            initial={{ opacity: 0, y: 25 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="lg:col-span-8 space-y-6"
          >
            <div className="space-y-5 text-base sm:text-lg text-[#B8B6AF] font-sans leading-relaxed max-w-2xl">
              <p>
                I am studying{" "}
                <span className="text-[#F2F0EA] font-medium">
                  Mechatronics Engineering at MPSTME in Mumbai
                </span>
                , but my curiosity rarely stays inside one discipline for very long.
              </p>
              <p>
                When I am not writing code for language models or building reading systems like{" "}
                <span className="text-[#4A90D9] font-medium">PAGE.OS</span>, I am directing
                experimental short films under the{" "}
                <span className="text-[#E07A3A] font-medium">Residual</span> identity, sculpting
                procedural monoliths in Blender, authoring psychological horror manuscripts, or
                designing geometric glyph alphabets.
              </p>
              <p>
                I am interested in artificial intelligence, filmmaking, systems, and the strange
                places where they overlap.
              </p>
            </div>

            {/* Quote block */}
            <div className="mt-8 p-6 md:p-8 rounded-xl bg-[#0A0A0A] border border-[#F2F0EA]/[0.04] relative">
              <div className="absolute top-4 left-4 text-4xl font-serif text-[#8B5CF6]/20">&ldquo;</div>
              <p className="text-base sm:text-lg italic text-[#B8B6AF] font-serif leading-relaxed pl-6">
                I don&apos;t treat technology as a corporate job. I treat technology as a
                creative medium — the same way a filmmaker treats light, or a writer treats words.
              </p>
            </div>

            {/* Three tenets — compact, inline */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-12 pt-8 border-t border-[#F2F0EA]/[0.04]">
              {[
                {
                  label: "CURIOSITY FIRST",
                  title: "Understand from the Core",
                  desc: "If I use a model or a mechanism, I want to write the training loop or calculate the physics myself.",
                },
                {
                  label: "VISUAL RESTRAINT",
                  title: "Make Space for the Mind",
                  desc: "Restraint and tactile shadow create far deeper emotional impact than flashiness.",
                },
                {
                  label: "CONTINUOUS ASSEMBLY",
                  title: "I Am Still Being Built",
                  desc: "Every project is an experiment in progress. I treat my skills as an evolving artifact.",
                },
              ].map((tenet) => (
                <div key={tenet.label} className="space-y-3">
                  <span className="text-[10px] font-mono text-[#8B5CF6] tracking-[0.2em]">
                    {tenet.label}
                  </span>
                  <h3 className="font-display text-base font-bold text-[#F2F0EA]">
                    {tenet.title}
                  </h3>
                  <p className="text-sm text-[#7A7874] font-sans leading-relaxed">
                    {tenet.desc}
                  </p>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
