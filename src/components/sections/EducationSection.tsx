"use client";

import React from "react";
import { motion } from "framer-motion";

export function WriteSection() {
  const works = [
    {
      title: "A ROOM FOR ONE MORE",
      status: "IN DEVELOPMENT",
      protagonist: "Ira Elowen Mireille",
      description:
        "I have always been interested in stories where reality isn't completely trustworthy. This is a psychological horror manuscript examining grief, unreliable perception, and the terrifying architecture of memory.",
      structure: "Fragmented archival manuscript and diary entries, with marginal notes and cipher inscriptions embedded in the text.",
      accent: "#C8C0AE",
      bgAccent: "#C8C0AE",
    },
    {
      title: "THE FIFTH EXIT",
      status: "IN DEVELOPMENT",
      protagonist: null,
      description:
        "A narrative trapped within non-Euclidean brutalist corridors. Five rooms representing internal limitations. The threat is not a monster — it is the horrifying realization that the space reflects your own psychological isolation.",
      structure: "Experimental short film concept with binaural audio treatment and Blender spatial previs.",
      accent: "#C4565A",
      bgAccent: "#C4565A",
    },
  ];

  return (
    <section
      id="write"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 section-paper"
    >
      <div className="max-w-6xl mx-auto">
        {/* Section index */}
        <div className="text-[10px] font-mono text-[#C8C0AE]/40 tracking-[0.25em] mb-8">
          THINGS I WRITE
        </div>

        {/* Giant serif heading — manuscript feeling */}
        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
          className="font-serif text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold text-[#C8C0AE] leading-[0.95] mb-6 italic"
        >
          Write
        </motion.h2>

        <p className="text-base text-[#C8C0AE]/50 max-w-xl font-sans leading-relaxed mb-20">
          Quiet archival work. Stories where reality isn&apos;t quite trustworthy.
        </p>

        {/* Manuscript works */}
        <div className="space-y-16">
          {works.map((work, i) => (
            <motion.div
              key={work.title}
              initial={{ opacity: 0, y: 25 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.9, delay: i * 0.1 }}
              className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start"
            >
              {/* Left: manuscript-style visual */}
              <div className={`lg:col-span-5 ${i % 2 === 1 ? "lg:order-2" : ""}`}>
                <div className="relative p-8 md:p-10 rounded-xl bg-[#12100C]/60 border border-[#C8C0AE]/[0.06]">
                  {/* Page simulation */}
                  <div className="text-center mb-8">
                    <p className="text-[8px] font-mono text-[#C8C0AE]/25 tracking-[0.3em] mb-4">MANUSCRIPT</p>
                    <h3 className="font-serif text-2xl md:text-3xl text-[#C8C0AE]/80 italic leading-tight">
                      {work.title}
                    </h3>
                  </div>
                  {work.protagonist && (
                    <p className="text-center text-[9px] font-mono text-[#C8C0AE]/20 tracking-wider mb-6">
                      PROTAGONIST: {work.protagonist}
                    </p>
                  )}
                  {/* Simulated page lines */}
                  <div className="space-y-3 mt-6">
                    {Array.from({ length: 8 }).map((_, j) => (
                      <div
                        key={j}
                        className="h-px bg-[#C8C0AE]/[0.05]"
                        style={{ width: `${55 + Math.sin(j * 1.5) * 25}%`, marginLeft: j % 3 === 0 ? "0" : "8%" }}
                      />
                    ))}
                  </div>
                  {/* Marginal annotation */}
                  <div className="absolute top-8 right-4 text-[7px] font-serif italic text-[#C8C0AE]/15 transform rotate-90 origin-right">
                    {work.accent === "#C4565A" ? "liminal space" : "unreliable narrator"}
                  </div>
                  {/* Page edge */}
                  <div className="absolute right-0 top-0 bottom-0 w-6 bg-gradient-to-l from-black/15 to-transparent rounded-r-xl" />
                </div>
              </div>

              {/* Right: content */}
              <div className={`lg:col-span-7 ${i % 2 === 1 ? "lg:order-1" : ""} space-y-6`}>
                <div className="flex items-center gap-3">
                  <div className="w-1.5 h-1.5 rounded-full" style={{ backgroundColor: work.accent }} />
                  <span className="text-[10px] font-mono tracking-[0.2em]" style={{ color: work.accent }}>
                    {work.status}
                  </span>
                </div>

                <h3 className="font-display text-3xl sm:text-4xl font-bold text-[#F2F0EA]">
                  {work.title}
                </h3>

                <p className="text-base sm:text-lg text-[#C8C0AE]/80 font-serif italic leading-relaxed max-w-lg">
                  {work.description}
                </p>

                <div className="pt-4 border-t border-[#C8C0AE]/[0.06]">
                  <p className="text-sm text-[#C8C0AE]/40 font-sans leading-relaxed">
                    {work.structure}
                  </p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Atmospheric quote */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 1.2, delay: 0.3 }}
          className="mt-24 p-8 md:p-12 text-center border-t border-b border-[#C8C0AE]/[0.06]"
        >
          <p className="text-xl sm:text-2xl md:text-3xl font-serif italic text-[#C8C0AE]/50 leading-relaxed">
            &ldquo;If the mirror remembers what stood before it yesterday, who is the stranger
            looking back today?&rdquo;
          </p>
        </motion.div>
      </div>
    </section>
  );
}
