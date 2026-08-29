"use client";

import React from "react";
import { motion } from "framer-motion";
import { Github, Linkedin, Mail, ArrowUp } from "lucide-react";

export function FooterSection() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <footer
      id="contact"
      className="relative w-full py-32 md:py-40 px-6 md:px-12 lg:px-20 bg-[#050505] border-t border-[#F2F0EA]/[0.04]"
    >
      <div className="max-w-6xl mx-auto">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.25em] mb-8">
          CONTACT
        </div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="space-y-16"
        >
          {/* Giant closing */}
          <h2 className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-9xl font-black text-[#F2F0EA] leading-[0.9]">
            STILL
            <br />
            <span className="text-[#8B5CF6]">BUILDING.</span>
          </h2>

          <div className="max-w-lg space-y-4">
            <p className="text-lg text-[#B8B6AF] font-sans leading-relaxed">
              There is a lot going on inside this head, and somehow it all connects.
            </p>
            <p className="text-base text-[#7A7874] font-sans leading-relaxed">
              If you want to see what I make next, reach out.
            </p>
          </div>

          {/* Contact links — horizontal */}
          <div className="flex flex-col sm:flex-row items-start gap-8 pt-8 border-t border-[#F2F0EA]/[0.04]">
            <a
              href="https://github.com/Wafion"
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-3 text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors group"
            >
              <Github className="w-4 h-4 text-[#7A7874] group-hover:text-[#8B5CF6] transition-colors" />
              <span className="text-xs font-heading font-medium tracking-wider">GITHUB</span>
            </a>
            <a
              href="https://www.linkedin.com/in/yash-sawant-1776a7399/"
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-3 text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors group"
            >
              <Linkedin className="w-4 h-4 text-[#7A7874] group-hover:text-[#8B5CF6] transition-colors" />
              <span className="text-xs font-heading font-medium tracking-wider">LINKEDIN</span>
            </a>
            <a
              href="mailto:contact@yash.dev"
              className="flex items-center gap-3 text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors group"
            >
              <Mail className="w-4 h-4 text-[#7A7874] group-hover:text-[#8B5CF6] transition-colors" />
              <span className="text-xs font-heading font-medium tracking-wider">EMAIL</span>
            </a>
          </div>

          {/* Bottom bar */}
          <div className="flex items-center justify-between pt-8 border-t border-[#F2F0EA]/[0.04]">
            <span className="text-[10px] font-mono text-[#7A7874] tracking-wider">
              DESIGNED & BUILT BY YASH © 2026
            </span>
            <button
              onClick={scrollToTop}
              className="p-2.5 rounded-full border border-[#F2F0EA]/[0.08] hover:border-[#8B5CF6]/30 text-[#7A7874] hover:text-[#8B5CF6] transition-all"
              title="Back to top"
            >
              <ArrowUp className="w-4 h-4" />
            </button>
          </div>
        </motion.div>
      </div>
    </footer>
  );
}
