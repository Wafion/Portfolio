"use client";

import React, { useEffect, useRef } from "react";

export function FilmGrain() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number;
    let width = (canvas.width = Math.floor(window.innerWidth / 4));
    let height = (canvas.height = Math.floor(window.innerHeight / 4));

    const onResize = () => {
      width = canvas.width = Math.floor(window.innerWidth / 4);
      height = canvas.height = Math.floor(window.innerHeight / 4);
    };

    window.addEventListener("resize", onResize);

    const renderNoise = () => {
      const imgData = ctx.createImageData(width, height);
      const buffer32 = new Uint32Array(imgData.data.buffer);
      const len = buffer32.length;

      for (let i = 0; i < len; i++) {
        // Very sparse, subtle film grain — no harshness
        if (Math.random() < 0.04) {
          const val = Math.floor(Math.random() * 200);
          buffer32[i] = (12 << 24) | (val << 16) | (val << 8) | val;
        }
      }

      ctx.putImageData(imgData, 0, 0);
      animId = requestAnimationFrame(renderNoise);
    };

    renderNoise();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("resize", onResize);
    };
  }, []);

  return (
    <div className="pointer-events-none fixed inset-0 z-40 overflow-hidden select-none">
      {/* Subtle noise canvas */}
      <canvas
        ref={canvasRef}
        className="absolute inset-0 h-full w-full opacity-30 mix-blend-overlay"
      />
      {/* Deep vignette — cinematic, dark gallery edges */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_0%,rgba(5,5,5,0.6)_100%)] pointer-events-none" />
    </div>
  );
}
