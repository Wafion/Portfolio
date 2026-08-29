"use client";

import React from "react";
import { ArrowLeft } from "lucide-react";

export default function NotFound() {
  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center p-6 bg-[#050505] text-[#F2F0EA] text-center">
      <div className="max-w-md space-y-8">
        <div className="text-[10px] font-mono text-[#7A7874] tracking-[0.2em]">
          404
        </div>

        <h1 className="font-display text-4xl sm:text-5xl font-bold text-[#F2F0EA]">
          NOT FOUND
        </h1>

        <p className="text-sm text-[#7A7874] font-sans leading-relaxed">
          This page does not exist in the exhibition. It may have been removed or never existed at
          all.
        </p>

        <a
          href="/"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded border border-[#F2F0EA]/[0.08] hover:border-[#F2F0EA]/[0.15] text-xs font-mono text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>RETURN</span>
        </a>
      </div>
    </div>
  );
}
