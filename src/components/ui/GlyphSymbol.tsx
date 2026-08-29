"use client";

import React from "react";
import { getGlyph } from "@/lib/data/cipher";
import { sound } from "@/components/audio/SoundEngine";

interface GlyphSymbolProps {
  char: string;
  size?: number;
  className?: string;
  strokeWidth?: number;
  interactive?: boolean;
  color?: string;
  showTooltip?: boolean;
}

export function GlyphSymbol({
  char,
  size = 24,
  className = "",
  strokeWidth = 1.5,
  interactive = true,
  color = "currentColor",
}: GlyphSymbolProps) {
  const glyph = getGlyph(char);

  const handleMouseEnter = () => {
    if (interactive) {
      sound.playCipherChirp(0.8 + Math.random() * 0.4);
    }
  };

  return (
    <div
      className={`inline-flex items-center justify-center transition-transform group ${className}`}
      onMouseEnter={handleMouseEnter}
      data-cursor={interactive ? `GLYPH: ${glyph.char}` : undefined}
      title={`${glyph.char} — ${glyph.name}`}
    >
      <svg
        width={size}
        height={size}
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="transition-all duration-300 group-hover:scale-110 group-hover:drop-shadow-[0_0_8px_rgba(6,182,212,0.8)]"
      >
        <path
          d={glyph.path}
          stroke={color}
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeLinejoin="round"
          className="transition-colors duration-200 group-hover:stroke-cyan-300"
        />
      </svg>
    </div>
  );
}

export function GlyphWord({
  text,
  size = 20,
  className = "",
  spacing = "gap-1.5",
}: {
  text: string;
  size?: number;
  className?: string;
  spacing?: string;
}) {
  return (
    <div className={`inline-flex items-center flex-wrap ${spacing} ${className}`}>
      {text.split("").map((c, i) => (
        <GlyphSymbol key={`${c}-${i}`} char={c} size={size} />
      ))}
    </div>
  );
}
