"use client";

import React, { useState, useEffect, useRef } from "react";
import { sound } from "@/components/audio/SoundEngine";
import { Play, Pause } from "lucide-react";

type ExperimentMode = "FLOW_FIELD" | "CIPHER_MATRIX" | "LISSAJOUS";

export function CreativeCodingCanvas() {
  const [mode, setMode] = useState<ExperimentMode>("FLOW_FIELD");
  const [speed, setSpeed] = useState<number>(1.2);
  const [isPlaying, setIsPlaying] = useState<boolean>(true);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const mouseRef = useRef<{ x: number; y: number; active: boolean }>({
    x: 0,
    y: 0,
    active: false,
  });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number;
    let width = (canvas.width = canvas.parentElement?.clientWidth || 800);
    let height = (canvas.height = 380);

    const onResize = () => {
      width = canvas.width = canvas.parentElement?.clientWidth || 800;
      height = canvas.height = 380;
    };
    window.addEventListener("resize", onResize);

    interface Particle {
      x: number;
      y: number;
      vx: number;
      vy: number;
      life: number;
      maxLife: number;
      color: string;
    }
    const particles: Particle[] = [];
    const colors = ["#4A90D9", "#5BB8D4", "#B8B6AF", "#5BAA8A", "#D4C87A"];
    const density = 200;

    for (let i = 0; i < density; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2,
        life: Math.random() * 100,
        maxLife: 80 + Math.random() * 100,
        color: colors[Math.floor(Math.random() * colors.length)],
      });
    }

    const glyphChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".split("");
    const fontSize = 14;
    const columns = Math.floor(width / fontSize);
    const drops = Array.from({ length: columns }, () => Math.floor(Math.random() * -50));

    let phase = 0;
    let t = 0;

    const render = () => {
      if (!isPlaying) {
        animId = requestAnimationFrame(render);
        return;
      }

      t += 0.01 * speed;

      if (mode === "FLOW_FIELD") {
        ctx.fillStyle = "rgba(5, 5, 5, 0.12)";
        ctx.fillRect(0, 0, width, height);

        for (const p of particles) {
          const angle =
            Math.sin(p.x * 0.005 + t) * Math.cos(p.y * 0.005 + t) * Math.PI * 4;
          p.vx += Math.cos(angle) * 0.12 * speed;
          p.vy += Math.sin(angle) * 0.12 * speed;

          if (mouseRef.current.active) {
            const dx = mouseRef.current.x - p.x;
            const dy = mouseRef.current.y - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 120) {
              p.vx += (dx / dist) * 0.7;
              p.vy += (dy / dist) * 0.7;
            }
          }

          p.vx *= 0.95;
          p.vy *= 0.95;
          p.x += p.vx;
          p.y += p.vy;
          p.life++;

          ctx.beginPath();
          ctx.arc(p.x, p.y, 1.2, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();

          if (p.x < 0 || p.x > width || p.y < 0 || p.y > height || p.life > p.maxLife) {
            p.x = Math.random() * width;
            p.y = Math.random() * height;
            p.vx = 0;
            p.vy = 0;
            p.life = 0;
          }
        }
      } else if (mode === "CIPHER_MATRIX") {
        ctx.fillStyle = "rgba(5, 5, 5, 0.15)";
        ctx.fillRect(0, 0, width, height);
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
          const char = glyphChars[Math.floor(Math.random() * glyphChars.length)];
          const x = i * fontSize;
          const y = drops[i] * fontSize;

          ctx.fillStyle = "rgba(232, 229, 221, 0.7)";
          ctx.fillText(char, x, y);

          ctx.fillStyle = "#D4C87A";
          if (y > 0) {
            ctx.fillText(
              glyphChars[Math.floor(Math.random() * glyphChars.length)],
              x,
              y - fontSize
            );
          }

          if (y > height && Math.random() > 0.975) drops[i] = 0;
          drops[i] += 0.7 * speed;
        }
      } else if (mode === "LISSAJOUS") {
        ctx.fillStyle = "rgba(5, 5, 5, 0.07)";
        ctx.fillRect(0, 0, width, height);

        phase += 0.012 * speed;
        const centerX = width / 2;
        const centerY = height / 2;
        const scale = Math.min(width, height) * 0.36;

        ctx.beginPath();
        ctx.strokeStyle = "#B8B6AF";
        ctx.lineWidth = 1.5;

        for (let theta = 0; theta < Math.PI * 2; theta += 0.02) {
          const x = centerX + scale * Math.sin(3 * theta + phase);
          const y = centerY + scale * Math.sin(4 * theta);
          if (theta === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }

      animId = requestAnimationFrame(render);
    };

    render();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("resize", onResize);
    };
  }, [mode, speed, isPlaying]);

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const rect = canvasRef.current?.getBoundingClientRect();
    if (!rect) return;
    mouseRef.current = {
      x: e.clientX - rect.left,
      y: e.clientY - rect.top,
      active: true,
    };
  };

  return (
    <div className="rounded-xl border border-[#F2F0EA]/[0.04] bg-[#0B0B0C]/50 overflow-hidden">
      {/* Controls */}
      <div className="flex flex-wrap items-center justify-between gap-3 px-5 py-3 border-b border-[#F2F0EA]/[0.04]">
        <div className="flex items-center gap-2">
          {(["FLOW_FIELD", "CIPHER_MATRIX", "LISSAJOUS"] as const).map((m) => (
            <button
              key={m}
              onClick={() => {
                sound.playSoftClick(400);
                setMode(m);
              }}
              className={`px-3 py-1.5 rounded text-[10px] font-mono tracking-wider transition-all ${
                mode === m
                  ? "text-[#F2F0EA] bg-[#F2F0EA]/[0.06] border border-[#F2F0EA]/[0.12]"
                  : "text-[#7A7874] hover:text-[#B8B6AF] border border-transparent"
              }`}
            >
              {m === "FLOW_FIELD" ? "FLOW FIELD" : m === "CIPHER_MATRIX" ? "CIPHER RAIN" : "LISSAJOUS"}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2">
            <span className="text-[9px] font-mono text-[#7A7874]">SPEED</span>
            <input
              type="range"
              min="0.4"
              max="3.0"
              step="0.1"
              value={speed}
              onChange={(e) => setSpeed(parseFloat(e.target.value))}
              className="w-20 accent-[#7A7874]"
            />
          </div>
          <button
            onClick={() => {
              sound.playSoftClick(350);
              setIsPlaying(!isPlaying);
            }}
            className="p-1.5 rounded border border-[#F2F0EA]/[0.08] text-[#B8B6AF] hover:text-[#F2F0EA] transition-colors"
          >
            {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>

      {/* Canvas */}
      <canvas
        ref={canvasRef}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => (mouseRef.current.active = false)}
        className="w-full h-[380px] cursor-crosshair block bg-[#050505]"
      />
    </div>
  );
}
