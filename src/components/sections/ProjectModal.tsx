"use client";

import React, { useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";
import { ExhibitionProject } from "@/lib/data/projects";

interface ProjectModalProps {
  project: ExhibitionProject | null;
  onClose: () => void;
}

export function ProjectModal({ project, onClose }: ProjectModalProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    if (project) {
      window.addEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "hidden";
    }
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "auto";
    };
  }, [project, onClose]);

  if (!project) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-8 overflow-y-auto">
        {/* Backdrop */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 bg-[#050505]/90 backdrop-blur-2xl"
        />

        {/* Case study window */}
        <motion.div
          initial={{ opacity: 0, scale: 0.97, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.97, y: 20 }}
          transition={{ type: "spring", damping: 30, stiffness: 250 }}
          className="relative w-full max-w-4xl max-h-[88vh] overflow-y-auto rounded-xl border border-[#F2F0EA]/[0.06] bg-[#0B0B0C] z-10"
        >
          {/* Header */}
          <div className="sticky top-0 z-20 flex items-center justify-between px-6 md:px-10 py-5 bg-[#0B0B0C]/95 backdrop-blur-xl border-b border-[#F2F0EA]/[0.04]">
            <div className="flex items-center gap-3">
              <div
                className="w-2 h-2 rounded-full"
                style={{ backgroundColor: project.accentColor }}
              />
              <span className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874]">
                #{project.number} — {project.title}
              </span>
            </div>

            <button
              onClick={onClose}
              className="p-2 rounded border border-[#F2F0EA]/[0.08] hover:border-[#F2F0EA]/[0.15] text-[#7A7874] hover:text-[#F2F0EA] transition-colors"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Content */}
          <div className="p-6 md:p-10 space-y-10">
            {/* Title & metadata */}
            <div>
              <div className="flex items-center gap-3 text-[10px] font-mono text-[#7A7874] tracking-wider mb-4">
                <span>{project.domain}</span>
                <span>·</span>
                <span>{project.year}</span>
                <span>·</span>
                <span className="px-2 py-0.5 rounded border border-[#F2F0EA]/[0.06] text-[#B8B6AF]">
                  {project.status}
                </span>
              </div>
              <h2 className="font-display text-4xl sm:text-5xl font-bold text-[#F2F0EA] mb-4">
                {project.title}
              </h2>
              <p className="text-lg font-serif italic text-[#B8B6AF] leading-relaxed">
                &ldquo;{project.tagline}&rdquo;
              </p>
            </div>

            {/* WHAT I WANTED TO MAKE */}
            <div className="space-y-3 p-6 md:p-8 rounded-xl bg-[#050505]/60 border border-[#F2F0EA]/[0.04]">
              <h3 className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] uppercase">
                01 — WHAT I WANTED TO MAKE
              </h3>
              <p className="text-base text-[#B8B6AF] leading-relaxed font-sans">
                {project.caseStudy.whatIWantedToMake}
              </p>
            </div>

            {/* WHY */}
            <div className="space-y-3">
              <h3 className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] uppercase">
                02 — WHY
              </h3>
              <p className="text-base text-[#B8B6AF] leading-relaxed font-sans">
                {project.caseStudy.why}
              </p>
            </div>

            {/* HOW */}
            <div className="space-y-3">
              <h3 className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] uppercase">
                03 — HOW I BUILT IT
              </h3>
              <p className="text-base text-[#B8B6AF] leading-relaxed font-sans">
                {project.caseStudy.how}
              </p>
            </div>

            {/* WHAT WORKED & WHAT DIDN'T */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="p-6 rounded-xl bg-[#0B0B0C]/40 border border-[#5BAA8A]/10 space-y-3">
                <h4 className="text-[10px] font-mono tracking-[0.2em] text-[#5BAA8A] uppercase">
                  WHAT WORKED
                </h4>
                <p className="text-sm text-[#B8B6AF] leading-relaxed font-sans">
                  {project.caseStudy.whatWorked}
                </p>
              </div>

              <div className="p-6 rounded-xl bg-[#0B0B0C]/40 border border-[#C4565A]/10 space-y-3">
                <h4 className="text-[10px] font-mono tracking-[0.2em] text-[#C4565A] uppercase">
                  WHAT DIDN&apos;T
                </h4>
                <p className="text-sm text-[#B8B6AF] leading-relaxed font-sans">
                  {project.caseStudy.whatDidnt}
                </p>
              </div>
            </div>

            {/* WHAT I LEARNED */}
            <div className="space-y-3">
              <h3 className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] uppercase">
                05 — WHAT I LEARNED
              </h3>
              <p className="text-base text-[#B8B6AF] leading-relaxed font-sans">
                {project.caseStudy.whatILearned}
              </p>
            </div>

            {/* Quote */}
            {project.caseStudy.quote && (
              <div className="p-6 border-l border-[#F2F0EA]/10">
                <p className="text-lg font-serif italic text-[#7A7874] leading-relaxed">
                  &ldquo;{project.caseStudy.quote}&rdquo;
                </p>
              </div>
            )}

            {/* Specifications */}
            <div className="space-y-4 pt-6 border-t border-[#F2F0EA]/[0.04]">
              <h3 className="text-[10px] font-mono tracking-[0.2em] text-[#7A7874] uppercase">
                06 — SPECIFICATIONS
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {project.caseStudy.specifications.map((spec, i) => (
                  <div
                    key={i}
                    className="flex items-center justify-between p-3 rounded bg-[#050505]/60 border border-[#F2F0EA]/[0.04]"
                  >
                    <span className="text-[10px] font-mono text-[#7A7874]">{spec.label}</span>
                    <span className="text-xs text-[#F2F0EA] font-medium text-right">
                      {spec.value}
                    </span>
                  </div>
                ))}
              </div>

              <div className="flex flex-wrap gap-2 pt-2">
                {project.technologies.map((tech, i) => (
                  <span
                    key={i}
                    className="px-3 py-1.5 rounded text-[10px] font-mono text-[#B8B6AF] bg-[#F2F0EA]/[0.04] border border-[#F2F0EA]/[0.06]"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}
