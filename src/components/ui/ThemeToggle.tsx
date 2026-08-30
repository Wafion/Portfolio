"use client";

import { useTheme } from "@/lib/theme/ThemeProvider";
import { Monitor, Moon, Sun } from "lucide-react";
import { useCallback, useEffect, useRef, useState } from "react";

/**
 * DECISION: 3D canvases (IntersectionHeroCanvas, ArchiveCoreCanvas, etc.)
 * are intentionally kept dark & atmospheric in BOTH themes.
 * The canvases serve as "exhibition windows" — they represent immersive
 * digital artifacts that maintain their own lighting environment regardless
 * of the page theme. Re-skinning them would break the atmospheric integrity
 * and require rewriting Three.js materials, lights, fog, and clearColor.
 */

const THEME_OPTIONS = [
  { value: "light" as const, label: "Light", Icon: Sun },
  { value: "dark" as const, label: "Dark", Icon: Moon },
  { value: "system" as const, label: "System", Icon: Monitor },
];

export function ThemeToggle({ className = "" }: { className?: string }) {
  const { theme, setTheme } = useTheme();
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const buttonRef = useRef<HTMLButtonElement>(null);

  const handleToggle = useCallback(() => setIsOpen((prev) => !prev), []);

  const handleSelect = useCallback(
    (value: "light" | "dark" | "system") => {
      setTheme(value);
      setIsOpen(false);
      buttonRef.current?.focus();
    },
    [setTheme],
  );

  // Close on outside click
  useEffect(() => {
    if (!isOpen) return;
    const handler = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, [isOpen]);

  // Close on Escape
  useEffect(() => {
    if (!isOpen) return;
    const handler = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setIsOpen(false);
        buttonRef.current?.focus();
      }
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [isOpen]);

  const currentOption = THEME_OPTIONS.find((o) => o.value === theme) ?? THEME_OPTIONS[2];
  const CurrentIcon = currentOption.Icon;

  const ariaLabel =
    theme === "system"
      ? "Theme: system preference (currently dark). Click to change."
      : `Theme: ${theme}. Click to change.`;

  return (
    <div className={`relative ${className}`} ref={menuRef}>
      <button
        ref={buttonRef}
        onClick={handleToggle}
        className="system-control"
        data-cursor="CHANGE THEME"
        aria-label={ariaLabel}
        aria-expanded={isOpen}
        aria-haspopup="menu"
      >
        <CurrentIcon className="h-3.5 w-3.5" />
        <span className="hidden sm:inline">
          {currentOption.label.toUpperCase()}
        </span>
      </button>

      {isOpen && (
        <div
          role="menu"
          aria-label="Theme selection"
          className="theme-toggle-menu absolute right-0 top-full z-50 mt-2 min-w-[9rem] overflow-hidden rounded-lg border p-1 shadow-2xl backdrop-blur-xl"
        >
          {THEME_OPTIONS.map((option) => {
            const isActive = theme === option.value;
            return (
              <button
                key={option.value}
                role="menuitem"
                onClick={() => handleSelect(option.value)}
                className={`theme-toggle-item flex w-full items-center gap-2.5 rounded-md px-3 py-2 text-left text-[9px] tracking-[0.14em] transition-colors ${
                  isActive ? "font-medium" : ""
                }`}
              >
                <option.Icon className="h-3.5 w-3.5" />
                <span>{option.label.toUpperCase()}</span>
                {isActive && (
                  <span className="ml-auto text-[8px] opacity-50">✓</span>
                )}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}
