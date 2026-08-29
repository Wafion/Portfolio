"use client";

import { useEffect, useState } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";

type CursorVariant = "idle" | "interactive" | "glyph" | "navigation" | "hidden";

function getVariant(label: string, target: HTMLElement | null): CursorVariant {
  if (!target) return "idle";
  if (label.startsWith("GLYPH")) return "glyph";
  if (label.startsWith("GO TO")) return "navigation";
  if (target.closest("a, button, input, textarea, select, [role='button']")) return "interactive";
  return "idle";
}

export function CustomCursor() {
  const [isTouchDevice, setIsTouchDevice] = useState(true);
  const [cursor, setCursor] = useState<{ label: string; variant: CursorVariant }>({ label: "", variant: "idle" });
  const x = useMotionValue(-100);
  const y = useMotionValue(-100);
  const springX = useSpring(x, { stiffness: 800, damping: 42, mass: 0.18 });
  const springY = useSpring(y, { stiffness: 800, damping: 42, mass: 0.18 });
  const trailX = useSpring(x, { stiffness: 150, damping: 24, mass: 0.35 });
  const trailY = useSpring(y, { stiffness: 150, damping: 24, mass: 0.35 });

  useEffect(() => {
    const isTouch = window.matchMedia("(pointer: coarse)").matches;
    setIsTouchDevice(isTouch);
    if (isTouch) return;

    document.body.classList.add("has-custom-cursor");
    let lastTarget: HTMLElement | null = null;
    const onMouseMove = (event: MouseEvent) => {
      x.set(event.clientX);
      y.set(event.clientY);

      const target = (event.target as HTMLElement)?.closest("[data-cursor]") as HTMLElement | null;
      if (target !== lastTarget) {
        lastTarget = target;
        const label = target?.getAttribute("data-cursor") ?? "";
        setCursor({ label, variant: getVariant(label, target) });
      }
      if (!target && lastTarget === null) {
        const interactive = (event.target as HTMLElement)?.closest("a, button, input, textarea, select, [role='button']") as HTMLElement | null;
        const nextVariant: CursorVariant = interactive ? "interactive" : "idle";
        setCursor((current) => current.variant === nextVariant && !current.label ? current : { label: "", variant: nextVariant });
      }
    };
    const onMouseLeave = () => setCursor((current) => ({ ...current, variant: "hidden" }));
    const onMouseEnter = () => setCursor((current) => ({ ...current, variant: current.label ? getVariant(current.label, lastTarget) : "idle" }));

    window.addEventListener("mousemove", onMouseMove, { passive: true });
    document.addEventListener("mouseleave", onMouseLeave);
    document.addEventListener("mouseenter", onMouseEnter);
    return () => {
      document.body.classList.remove("has-custom-cursor");
      window.removeEventListener("mousemove", onMouseMove);
      document.removeEventListener("mouseleave", onMouseLeave);
      document.removeEventListener("mouseenter", onMouseEnter);
    };
  }, [trailX, trailY, x, y]);

  if (isTouchDevice) return null;

  const isHidden = cursor.variant === "hidden";
  const isExpanded = cursor.variant !== "idle" && !isHidden;
  const label = cursor.variant === "glyph" ? cursor.label.replace("GLYPH: ", "GLYPH // ") : cursor.variant === "navigation" ? cursor.label.replace("GO TO ", "NAV // ") : cursor.label;

  return (
    <div className="pointer-events-none fixed inset-0 z-[100] overflow-hidden" aria-hidden="true">
      <motion.div className="fixed left-0 top-0" style={{ x: trailX, y: trailY }} animate={{ opacity: isHidden ? 0 : 0.24 }}>
        <div className="cursor-trail" />
      </motion.div>

      <motion.div
        className={`fixed left-0 top-0 flex items-center justify-center rounded-full border ${cursor.variant === "glyph" ? "border-[#d5bb76]" : cursor.variant === "navigation" ? "border-[#75d4bd]" : "border-[#f2f0ea]"}`}
        style={{ x: springX, y: springY, translateX: "-50%", translateY: "-50%" }}
        animate={{ width: isExpanded ? 68 : 34, height: isExpanded ? 68 : 34, opacity: isHidden ? 0 : 1, rotate: isExpanded ? 180 : 0 }}
        transition={{ type: "spring", stiffness: 260, damping: 24, mass: 0.42 }}
      >
        <span className="cursor-orbit" />
        <span className="cursor-crosshair cursor-crosshair-horizontal" />
        <span className="cursor-crosshair cursor-crosshair-vertical" />
        <span className="cursor-core" />
      </motion.div>

      <motion.div
        className="fixed left-0 top-0 flex items-center gap-2"
        style={{ x: springX, y: springY, translateX: 22, translateY: 22 }}
        animate={{ opacity: label && !isHidden ? 1 : 0, scale: label && !isHidden ? 1 : 0.86 }}
        transition={{ duration: 0.18 }}
      >
        <span className="cursor-label-line" />
        <span className="cursor-label">{label}</span>
      </motion.div>

      <motion.div className="fixed left-0 top-0" style={{ x: springX, y: springY }} animate={{ opacity: isHidden ? 0 : 1 }}>
        <span className="cursor-coordinate">{cursor.variant === "glyph" ? "CIPHER" : cursor.variant === "navigation" ? "SYSTEM" : "Y.OS"}</span>
      </motion.div>
    </div>
  );
}
