"use client";

import { useEffect, useRef, useState, useCallback } from "react";

/*
 * LIMINAL HERO — "ORIGIN"
 *
 * Sequence:
 *   0-500ms:   Pure black
 *   500ms:     YASH fades in against darkness
 *   on scroll:  YASH lifts away and vanishes
 *   ~40%:      Veil lifts, video revealed and begins scrubbing
 *   68-100%:   Red portal transition → cream → About section
 */

const LETTERS = [
  { char: "Y", driftX: -0.5 },
  { char: "A", driftX: -0.15 },
  { char: "S", driftX: 0.15 },
  { char: "H", driftX: 0.5 },
];

/* Video only scrubs in the progress range [VIDEO_START, 1.0] */
const VIDEO_START = 0.08;

export function LiminalHeroSection() {
  const sectionRef = useRef<HTMLElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const viewportRef = useRef<HTMLDivElement>(null);

  const [progress, setProgress] = useState(0);
  const [isPinned, setIsPinned] = useState(false);
  const [videoReady, setVideoReady] = useState(false);
  const [reducedMotion, setReducedMotion] = useState(false);

  /* Startup */
  const [yashVisible, setYashVisible] = useState(false);
  const hasScrolled = useRef(false);
  const audioCtxRef = useRef<AudioContext | null>(null);

  /* Veil opacity */
  const veilRef = useRef<HTMLDivElement>(null);
  const veilOpacity = useRef(1);

  /* Mouse parallax */
  const mouseX = useRef(0);
  const mouseY = useRef(0);
  const smoothMouseX = useRef(0);
  const smoothMouseY = useRef(0);

  useEffect(() => {
    setReducedMotion(
      window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    );
  }, []);

  /* ── Startup: pure black → YASH appears ───────────────────────── */
  useEffect(() => {
    if (reducedMotion) {
      setYashVisible(true);
      return;
    }
    const t = setTimeout(() => setYashVisible(true), 500);
    return () => clearTimeout(t);
  }, [reducedMotion]);

  /* ── Fluorescent buzz SFX via Web Audio API ──────────────────── */
  const playFlickerSFX = useCallback(() => {
    if (audioCtxRef.current) return;
    try {
      const ctx = new AudioContext();
      audioCtxRef.current = ctx;
      const osc1 = ctx.createOscillator();
      osc1.type = "sine";
      osc1.frequency.value = 60;
      const osc2 = ctx.createOscillator();
      osc2.type = "sine";
      osc2.frequency.value = 120;
      const bufSize = ctx.sampleRate * 2;
      const buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
      const d = buf.getChannelData(0);
      for (let i = 0; i < bufSize; i++) d[i] = (Math.random() * 2 - 1) * 0.03;
      const noise = ctx.createBufferSource();
      noise.buffer = buf;
      noise.loop = true;
      const master = ctx.createGain();
      master.gain.value = 0;
      const oscG = ctx.createGain();
      oscG.gain.value = 0.12;
      const noiseG = ctx.createGain();
      noiseG.gain.value = 0.4;
      const lp = ctx.createBiquadFilter();
      lp.type = "lowpass";
      lp.frequency.value = 200;
      osc1.connect(oscG);
      osc2.connect(oscG);
      oscG.connect(lp);
      noise.connect(noiseG);
      noiseG.connect(lp);
      lp.connect(master);
      master.connect(ctx.destination);
      osc1.start();
      osc2.start();
      noise.start();
      master.gain.linearRampToValueAtTime(0.08, ctx.currentTime + 0.3);
      master.gain.linearRampToValueAtTime(0, ctx.currentTime + 4);
      setTimeout(() => {
        osc1.stop();
        osc2.stop();
        noise.stop();
        ctx.close();
        audioCtxRef.current = null;
      }, 4200);
    } catch {
      /* audio unavailable */
    }
  }, []);

  /* ── Mouse tracking ───────────────────────────────────────────── */
  useEffect(() => {
    if (reducedMotion) return;
    const vp = viewportRef.current;
    if (!vp) return;
    const onMove = (e: MouseEvent) => {
      const r = vp.getBoundingClientRect();
      mouseX.current = ((e.clientX - r.left) / r.width) * 2 - 1;
      mouseY.current = ((e.clientY - r.top) / r.height) * 2 - 1;
    };
    vp.addEventListener("mousemove", onMove, { passive: true });
    return () => vp.removeEventListener("mousemove", onMove);
  }, [reducedMotion]);

  /* ── Scroll + veil lift + delayed video scrub ─────────────────── */
  useEffect(() => {
    const section = sectionRef.current;
    const video = videoRef.current;
    if (!section) return;
    let frame = 0;
    let smoothProgress = 0;

    const sentinel = document.createElement("div");
    sentinel.style.cssText =
      "position:absolute;top:0;left:0;width:1px;height:1px;pointer-events:none;";
    section.prepend(sentinel);
    const observer = new IntersectionObserver(
      ([entry]) => setIsPinned(!entry.isIntersecting),
      { threshold: 0, rootMargin: "-1px 0px 0px 0px" },
    );
    observer.observe(sentinel);

    const update = () => {
      const bounds = section.getBoundingClientRect();
      const travel = Math.max(section.offsetHeight - window.innerHeight, 1);
      const target = Math.min(1, Math.max(0, -bounds.top / travel));
      smoothProgress +=
        (target - smoothProgress) * (reducedMotion ? 0.16 : 0.065);
      setProgress(smoothProgress);

      smoothMouseX.current += (mouseX.current - smoothMouseX.current) * 0.08;
      smoothMouseY.current += (mouseY.current - smoothMouseY.current) * 0.08;

      if (bounds.bottom <= window.innerHeight + 4) setIsPinned(false);

      /* First scroll: trigger SFX */
      if (smoothProgress > 0.005 && !hasScrolled.current) {
        hasScrolled.current = true;
        playFlickerSFX();
      }

      /*
       * Veil lifts from 1 → 0 between progress 0.05 and 0.22
       */
      if (hasScrolled.current) {
        const targetVeil = Math.max(
          0,
          1 - Math.max(0, (smoothProgress - 0.05) / 0.17),
        );
        veilOpacity.current +=
          (targetVeil - veilOpacity.current) * 0.04;
        if (veilRef.current) {
          veilRef.current.style.opacity = String(veilOpacity.current);
        }
      }

      /*
       * Video scrub: only after VIDEO_START progress
       * progress 0.4 → video frame 0
       * progress 1.0 → video frame end
       */
      if (video && video.readyState >= 2 && smoothProgress > VIDEO_START - 0.05) {
        const videoProgress = Math.min(
          1,
          Math.max(0, (smoothProgress - VIDEO_START) / (1 - VIDEO_START)),
        );
        video.currentTime = videoProgress * video.duration;
      }
      frame = requestAnimationFrame(update);
    };
    frame = requestAnimationFrame(update);
    return () => {
      cancelAnimationFrame(frame);
      observer.disconnect();
      sentinel.remove();
    };
  }, [reducedMotion, videoReady, playFlickerSFX]);

  /* ── Derived values ───────────────────────────────────────────── */
  const statusLabel =
    progress > 0.78
      ? "THRESHOLD"
      : progress > 0.2
        ? "ACCESSING..."
        : "01 / ORIGIN";
  const uiOpacity = Math.max(0, 1 - Math.max(0, progress - 0.55) * 2.2);
  const videoBrightness = 0.75 + Math.sin(progress * Math.PI) * 0.2;
  const videoContrast = 1.08 + progress * 0.08;

  const mx = smoothMouseX.current;
  const my = smoothMouseY.current;

  /* YASH lift-into-light */
  const getLetterStyle = (index: number) => {
    const L = LETTERS[index];
    const liftStart = 0.1 + index * 0.025;
    const liftEnd = 0.38 + index * 0.02;
    const t = Math.min(
      1,
      Math.max(0, (progress - liftStart) / (liftEnd - liftStart)),
    );
    const ease = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    return {
      display: "inline-block",
      transform: `translateX(calc(${L.driftX * ease * 5}vw + ${(1 - ease) * mx * 1.5}rem)) translateY(calc(${-55 * ease}vh + ${(1 - ease) * my * -1}rem)) scaleY(${1 - ease * 0.45})`,
      filter: `blur(${16 * ease}px)`,
      opacity: 1 - ease,
      willChange: "transform, filter, opacity",
    } as React.CSSProperties;
  };

  const cTX = mx * 3,
    cTY = my * -2,
    cPX = mx * -8,
    cPY = my * -5;
  const rGO = Math.min(1, Math.max(0, (progress - 0.68) * 5.5));
  const rEO = Math.min(1, Math.max(0, (progress - 0.8) * 8));
  const dO = Math.min(1, Math.max(0, (progress - 0.88) * 12));
  const crO = Math.min(1, Math.max(0, (progress - 0.92) * 14));
  const vPX = mx * 2,
    vPY = my * 1.5;

  return (
    <section
      ref={sectionRef}
      id="hero"
      className="liminal-hero"
      style={{ height: "400vh" }}
    >
      <div
        ref={viewportRef}
        className="liminal-viewport"
        style={{
          position: isPinned ? "fixed" : "relative",
          top: isPinned ? 0 : undefined,
          left: isPinned ? 0 : undefined,
          right: isPinned ? 0 : undefined,
          width: isPinned ? "100%" : undefined,
          zIndex: isPinned ? 50 : undefined,
        }}
      >
        {/* Video — hidden under the dark veil until ~40% scroll */}
        <video
          ref={videoRef}
          className="liminal-video"
          muted
          playsInline
          preload="auto"
          onLoadedData={() => setVideoReady(true)}
          style={{
            filter: `brightness(${videoBrightness}) contrast(${videoContrast})`,
            transform: `translate(${vPX}%, ${vPY}%) scale(1.5)`,
          }}
        >
          <source src="/liminal-bg.mp4" type="video/mp4" />
        </video>
        <div className="liminal-video-fallback" aria-hidden="true" />

        {/* DARK VEIL — stays solid until YASH vanishes, then lifts to reveal video */}
        <div
          ref={veilRef}
          className="archive-veil liminal-hero-veil"
          style={{ opacity: 1 }}
          aria-hidden="true"
        />

        {/* Overlays */}
        <div className="liminal-scanlines" aria-hidden="true" />

        {/* Red transition */}
        <div
          className="liminal-red-glow"
          style={{ opacity: rGO }}
          aria-hidden="true"
        />
        <div
          className="liminal-red-engulf"
          style={{ opacity: rEO }}
          aria-hidden="true"
        />
        <div
          className="liminal-desaturate"
          style={{ opacity: dO }}
          aria-hidden="true"
        />
        <div
          className="liminal-cream-reveal"
          style={{ opacity: crO }}
          aria-hidden="true"
        />

        {/* UI */}
        <div
          className="liminal-ui liminal-top-meta"
          style={{
            opacity: uiOpacity,
            transform: `translate(${mx * 2}px, ${my}px)`,
          }}
        >
          <span>{statusLabel}</span>
          <span className="liminal-rule" />
          <span>SCROLL / CAMERA CONTROL</span>
        </div>
        <div
          className="liminal-coordinate"
          style={{
            opacity: uiOpacity,
            transform: `translate(${mx * 4}px, ${my * 2}px)`,
          }}
        >
          <span>19.0760° N</span>
          <span>72.8777° E</span>
          <span className="liminal-separator">—</span>
          <span>MUMBAI,</span>
          <span>INDIA</span>
          <span className="liminal-origin-mark">＋ Y.05</span>
        </div>
        <div
          className="liminal-disciplines"
          style={{
            opacity: uiOpacity,
            transform: `translate(${mx * -3}px, ${my * 1.5}px)`,
          }}
          aria-label="Areas of practice"
        >
          {["MECHATRONICS", "SOFTWARE", "AI", "FILM", "3D", "WRITING"].map(
            (l) => (
              <span key={l}>/ {l}</span>
            ),
          )}
        </div>

        {/* YASH */}
        <div
          className="liminal-word-wrap"
          style={{
            transform: `translate(-50%, -50%) perspective(800px) rotateY(${cTX}deg) rotateX(${cTY}deg) translate(${cPX}px, ${cPY}px)`,
            opacity: yashVisible ? 1 : 0,
            transition: yashVisible ? "opacity 1.2s ease-out" : "none",
            zIndex: 6,
          }}
        >
          <h1 className="liminal-word" aria-label="YASH">
            {LETTERS.map((L, i) => (
              <span key={L.char} style={getLetterStyle(i)}>
                {L.char}
              </span>
            ))}
          </h1>
        </div>

        <div
          className="liminal-origin-code"
          style={{ opacity: uiOpacity }}
        >
          Y.05
          <div />
        </div>
      </div>
    </section>
  );
}
