"use client";

import React from "react";
import { motion } from "framer-motion";

export function BuildSection() {
  const domains = [
    {
      title: "ENGINEERING",
      subtitle: "MECHATRONICS · ROBOTICS · SYSTEMS",
      color: "#D4A753",
      description:
        "I study Mechatronics Engineering at MPSTME, Mumbai — combining mechanical dynamics, circuit design, and microcontroller software into physical systems.",
      skills: [
        { name: "Mechatronics Core", detail: "Kinematics, actuators, motor drivers, sensor acquisition" },
        { name: "Robotics & Automation", detail: "Feedback control loops, inverse kinematics, serial telemetry" },
        { name: "Systems Thinking", detail: "Modeling mechanical, electronic, and software interactions" },
        { name: "Electronics & Embedded", detail: "Circuit schematics, microcontrollers, signal conditioning" },
      ],
    },
    {
      title: "SOFTWARE",
      subtitle: "TYPESCRIPT · REACT · PYTHON · FIREBASE",
      color: "#4A90D9",
      description:
        "I write clean, type-safe code for full-stack web applications, distributed state, and creative interfaces.",
      skills: [
        { name: "TypeScript & JavaScript", detail: "Asynchronous architectures, strict typing, reactive states" },
        { name: "Next.js & React", detail: "App Router, server components, client-side streaming" },
        { name: "Python", detail: "ML pipelines, FastAPI microservices, automated data processing" },
        { name: "Firebase & Cloud", detail: "Cloud Firestore, real-time sync, auth, edge caching" },
      ],
    },
    {
      title: "AI",
      subtitle: "PYTORCH · LLMs · LOCAL AI · NLP",
      color: "#5BB8D4",
      description:
        "I explore local language models, transformer classification, narrative audio understanding, and agentic workflows.",
      skills: [
        { name: "PyTorch & Transformers", detail: "Fine-tuning multi-task models, embeddings, sequence classification" },
        { name: "Local AI & Ollama", detail: "Edge quantization, private local inference, prompt engineering" },
        { name: "Vector Search & Retrieval", detail: "Semantic search, cultural knowledge graphs, vector similarity" },
        { name: "NLP & Narrative Understanding", detail: "Pacing analysis, dialogue parsing, emotional scene classification" },
      ],
    },
  ];

  return (
    <section
      id="build"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#0A0A0A]"
    >
      <div className="max-w-7xl mx-auto">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
          THINGS I BUILD
        </div>

        {/* Giant heading */}
        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black text-[#F2F0EA] leading-[0.95] mb-20"
        >
          BUILD
        </motion.h2>

        <div className="space-y-24">
          {domains.map((domain, domainIndex) => (
            <motion.div
              key={domain.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.8, delay: domainIndex * 0.08 }}
            >
              {/* Domain header — large, asymmetric */}
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start mb-10">
                <div className="lg:col-span-7">
                  <div
                    className="text-[10px] font-mono tracking-[0.25em] mb-4"
                    style={{ color: domain.color }}
                  >
                    {domain.subtitle}
                  </div>
                  <h3 className="font-display text-3xl sm:text-4xl md:text-5xl font-bold text-[#F2F0EA]">
                    {domain.title}
                  </h3>
                </div>
                <div className="lg:col-span-5">
                  <p className="text-sm text-[#7A7874] font-sans leading-relaxed max-w-md">
                    {domain.description}
                  </p>
                </div>
              </div>

              {/* Skills — 2-column grid, each card with accent */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {domain.skills.map((skill, i) => (
                  <div
                    key={i}
                    className="p-5 rounded-lg border border-[#F2F0EA]/[0.04] bg-[#050505]/60 hover:border-[#F2F0EA]/[0.08] transition-colors duration-300"
                  >
                    <h4 className="text-sm font-heading font-medium text-[#F2F0EA] mb-1.5">
                      {skill.name}
                    </h4>
                    <p className="text-xs text-[#7A7874] font-sans leading-relaxed">
                      {skill.detail}
                    </p>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
