"use client";

import { useEffect, useRef, useState } from "react";
import type { CSSProperties, PointerEvent as ReactPointerEvent, RefObject } from "react";
import { ArrowUpRight, BookOpen, ChevronDown, Radio } from "lucide-react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { sound } from "@/components/audio/SoundEngine";
import { EXHIBITION_PROJECTS, ExhibitionProject } from "@/lib/data/projects";

type ArchivePageId = "cover" | "index" | "library" | "reader" | "infinite";
type FragmentId = "catalogue" | "mode" | "artwork";

type ArchivePage = {
  id: ArchivePageId;
  number: string;
  title: string;
  subtitle: string;
  body: string;
  marker: string;
  accent: string;
};

type CatalogueFragment = {
  id: FragmentId;
  page: ArchivePageId;
  number: string;
  left: number;
  top: number;
  width: number;
  height: number;
  text: string;
  accent: string;
};

const ARCHIVE_PAGES: ArchivePage[] = [
  { id: "cover", number: "00", title: "THE OPEN ARCHIVE", subtitle: "A book that has not yet decided who is reading it.", body: "PAGE.OS / PRIVATE CATALOGUE / UNSEALED", marker: "VALOMBRE COLLECTION", accent: "#c9b98b" },
  { id: "index", number: "01", title: "INDEX OF OPEN THINGS", subtitle: "The drawer is full of places that no longer appear on maps.", body: "GUTENBERG\nINTERNET ARCHIVE\nOPEN CULTURE", marker: "CARD DRAWER 7 / UNRETURNED", accent: "#65c9e8" },
  { id: "library", number: "02", title: "THE BOOK LEFT OPEN", subtitle: "A saved trace, held at the exact page where someone stopped.", body: "AUTHOR / UNKNOWN\nSTATUS / STILL READING\nLAST MARK / HERE", marker: "LOCAL SHELF / NIGHT REGISTER", accent: "#d6a05b" },
  { id: "reader", number: "03", title: "TWO TEMPERATURES", subtitle: "One reader is clear. The other knows the room is listening.", body: "CLASSIC MODE / TEXT\nLOUNGE MODE / ATMOSPHERE\nFOCUS / PRESERVED", marker: "READER TERMINAL / 02.39", accent: "#b8a7e8" },
  { id: "infinite", number: "04", title: "PAST THE EDGE", subtitle: "The image continues after the catalogue ends.", body: "PUBLIC DOMAIN\nCC0 COLLECTIONS\nWANDER WITHOUT END", marker: "INFINITE GALLERY / SIGNAL LOST", accent: "#9dc8a8" },
];

const FRAGMENTS: CatalogueFragment[] = [
  { id: "catalogue", page: "library", number: "A", left: 67, top: 30, width: 19, height: 19, text: "OPEN", accent: "#d6a05b" },
  { id: "mode", page: "reader", number: "B", left: 20, top: 59, width: 20, height: 18, text: "READ", accent: "#b8a7e8" },
  { id: "artwork", page: "infinite", number: "C", left: 64, top: 63, width: 18, height: 18, text: "WANDER", accent: "#9dc8a8" },
];

const DUST_PARTICLES = Array.from({ length: 78 }, (_, index) => ({
  left: `${(index * 47) % 101}%`,
  top: `${(index * 29) % 101}%`,
  driftX: ((index % 7) - 3) * 1.7,
  driftY: -1.5 - (index % 6) * 0.7,
  rotate: (index % 2 === 0 ? 1 : -1) * (18 + (index % 9) * 13),
  size: 1 + (index % 3) * 0.8,
}));

function pageTransform(index: number, progress: number) {
  const position = progress * (ARCHIVE_PAGES.length - 1) - index;
  const depth = Math.max(-80, 75 - Math.abs(position) * 100);
  const angle = position > 0 ? -Math.min(116, position * 118) : Math.max(-12, position * 12);
  return `translateZ(${depth}px) rotateY(${angle}deg) translateX(${position > 0 ? -position * 4 : 0}px)`;
}

function isElementLit(element: HTMLButtonElement, scene: HTMLDivElement, light: { x: number; y: number }) {
  const sceneRect = scene.getBoundingClientRect();
  const elementRect = element.getBoundingClientRect();
  const targetX = ((elementRect.left + elementRect.width / 2 - sceneRect.left) / sceneRect.width) * 100;
  const targetY = ((elementRect.top + elementRect.height / 2 - sceneRect.top) / sceneRect.height) * 100;
  return Math.hypot(light.x - targetX, light.y - targetY) < 24;
}

function ArchiveDust({ progress }: { progress: number }) {
  return <div className="archive-dust-burst" aria-hidden="true">{DUST_PARTICLES.map((particle, index) => {
    const appear = Math.min(1, Math.max(0, (progress - 0.06) / 0.12));
    const disappear = Math.min(1, Math.max(0, (progress - 0.17) / 0.15));
    const opacity = appear * (1 - disappear);
    return <i key={index} style={{ left: particle.left, top: particle.top, width: `${particle.size}px`, height: `${particle.size}px`, opacity, transform: `translate3d(${particle.driftX * disappear}rem, ${particle.driftY * disappear}rem, 0) rotate(${particle.rotate * disappear}deg)` }} />;
  })}</div>;
}

function ArchivePageLayer({ page, index, progress, collected, onCollect, onNearFragment, reducedMotion }: { page: ArchivePage; index: number; progress: number; collected: Set<FragmentId>; onCollect: (fragment: CatalogueFragment, force: boolean, element: HTMLButtonElement) => void; onNearFragment: (fragment: CatalogueFragment, element: HTMLButtonElement) => void; reducedMotion: boolean }) {
  const fragment = FRAGMENTS.find((item) => item.page === page.id);
  const pagePosition = progress * (ARCHIVE_PAGES.length - 1) - index;
  const isActive = reducedMotion || Math.abs(pagePosition) < 0.65;
  return (
    <article className={`archive-page-layer archive-page-${page.id} ${isActive ? "is-active" : ""}`} style={{ "--page-accent": page.accent, transform: reducedMotion ? "none" : pageTransform(index, progress), zIndex: ARCHIVE_PAGES.length - index } as CSSProperties} aria-label={`${page.number} ${page.title}`}>
      <div className="archive-page-edge" />
      <div className="archive-page-meta"><span>{page.number} / {page.id.toUpperCase()}</span><span>{page.marker}</span></div>
      <div className="archive-page-content"><div className="archive-page-rule" /><h3>{page.title}</h3><p>{page.subtitle}</p><pre>{page.body}</pre></div>
      <div className="archive-page-stamp" style={{ color: page.accent }}>{page.id === "cover" ? "SEALED" : "ARCHIVE"}</div>
      {fragment && isActive && <button type="button" className={`archive-fragment ${collected.has(fragment.id) ? "is-collected" : ""}`} style={{ left: `${fragment.left}%`, top: `${fragment.top}%`, width: `${fragment.width}%`, height: `${fragment.height}%`, "--fragment-accent": fragment.accent } as CSSProperties} onPointerEnter={(event) => onNearFragment(fragment, event.currentTarget)} onPointerDown={(event) => { if (event.pointerType !== "mouse") onCollect(fragment, false, event.currentTarget); }} onClick={(event) => onCollect(fragment, event.detail === 0, event.currentTarget)} aria-label={`${collected.has(fragment.id) ? "Collected" : "Inspect"} catalogue fragment ${fragment.number}`} data-cursor={collected.has(fragment.id) ? "CATALOGUED" : "INSPECT"}><span>{collected.has(fragment.id) ? fragment.text : ""}</span><small>{collected.has(fragment.id) ? `FRAGMENT ${fragment.number}` : ""}</small></button>}
    </article>
  );
}

export function PageOSArchiveSection({ onOpenProject }: { onOpenProject: (project: ExhibitionProject) => void }) {
  const sectionRef = useRef<HTMLElement>(null);
  const sceneRef = useRef<HTMLDivElement>(null);
  const lightRef = useRef({ x: 50, y: 50 });
  const frameRef = useRef<number | null>(null);
  const lastStaticRef = useRef(0);
  const collectedRef = useRef<Set<FragmentId>>(new Set());
  const [progress, setProgress] = useState(0);
  const [collected, setCollected] = useState<Set<FragmentId>>(new Set());
  const [reducedMotion, setReducedMotion] = useState(false);
  const pageOS = EXHIBITION_PROJECTS.find((project) => project.id === "page-os");

  useEffect(() => {
    const section = sectionRef.current;
    const scene = sceneRef.current;
    if (!section || !scene) return;
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
    const updatePreference = () => setReducedMotion(reduced.matches);
    const updateLight = (event: PointerEvent) => {
      const rect = scene.getBoundingClientRect();
      lightRef.current = { x: Math.min(100, Math.max(0, ((event.clientX - rect.left) / rect.width) * 100)), y: Math.min(100, Math.max(0, ((event.clientY - rect.top) / rect.height) * 100)) };
      if (frameRef.current === null) frameRef.current = requestAnimationFrame(() => { scene.style.setProperty("--archive-light-x", `${lightRef.current.x}%`); scene.style.setProperty("--archive-light-y", `${lightRef.current.y}%`); frameRef.current = null; });
    };
    const updateProgress = (next: number) => setProgress(Math.min(1, Math.max(0, next)));
    updatePreference();
    reduced.addEventListener("change", updatePreference);
    const media = gsap.matchMedia();
    media.add("(prefers-reduced-motion: no-preference)", () => {
      gsap.registerPlugin(ScrollTrigger);
      const playhead = { progress: 0 };
      const tween = gsap.to(playhead, { progress: 1, duration: 1, paused: true, ease: "none", onUpdate: () => updateProgress(playhead.progress) });
      const trigger = ScrollTrigger.create({ trigger: section, animation: tween, pin: true, pinSpacing: true, start: "top top", end: () => `+=${window.innerHeight * 2.8}`, scrub: 2.4, anticipatePin: 1, invalidateOnRefresh: true, onEnter: () => sound.playSectionTone(58) });
      scene.addEventListener("pointermove", updateLight);
      return () => { trigger.kill(); tween.kill(); scene.removeEventListener("pointermove", updateLight); };
    });
    media.add("(prefers-reduced-motion: reduce)", () => {
      const onScroll = () => { const rect = section.getBoundingClientRect(); updateProgress(-rect.top / Math.max(section.offsetHeight - window.innerHeight, 1)); };
      onScroll(); window.addEventListener("scroll", onScroll, { passive: true }); scene.addEventListener("pointermove", updateLight);
      return () => { window.removeEventListener("scroll", onScroll); scene.removeEventListener("pointermove", updateLight); };
    });
    return () => { media.revert(); reduced.removeEventListener("change", updatePreference); if (frameRef.current !== null) cancelAnimationFrame(frameRef.current); };
  }, []);

  const collectFragment = (fragment: CatalogueFragment, force: boolean, element: HTMLButtonElement) => {
    if (collectedRef.current.has(fragment.id)) return;
    const expected = FRAGMENTS[collectedRef.current.size];
    if (!expected || expected.id !== fragment.id || (!force && !sceneRef.current) || (!force && !isElementLit(element, sceneRef.current!, lightRef.current))) return;
    const next = new Set(collectedRef.current); next.add(fragment.id); collectedRef.current = next; setCollected(next);
    sound.playArchiveCard();
    if (next.size === FRAGMENTS.length) sound.playArchiveReveal();
  };
  const nearFragment = (fragment: CatalogueFragment, element: HTMLButtonElement) => {
    if (collectedRef.current.has(fragment.id) || !sceneRef.current || !isElementLit(element, sceneRef.current, lightRef.current)) return;
    const now = performance.now();
    if (now - lastStaticRef.current > 850) { sound.playArchiveStatic(); lastStaticRef.current = now; }
  };
  const introProgress = reducedMotion ? 1 : Math.min(1, progress / 0.2);
  const gameProgress = reducedMotion ? 1 : Math.min(1, Math.max(0, (progress - 0.2) / 0.8));
  const allCollected = collected.size === FRAGMENTS.length;
  const finalReveal = allCollected && (reducedMotion || gameProgress > 0.88);
  if (!pageOS) return null;

  return (
    <section ref={sectionRef} id="archive" className={`archive-section ${allCollected ? "has-all-fragments" : ""}`}>
      <div ref={sceneRef} className="archive-scene" onPointerDown={(event) => { if (event.pointerType !== "mouse") updateTouchLight(event, sceneRef); }}>
        <div className="archive-ambient" aria-hidden="true" /><div className="archive-veil" aria-hidden="true" />
        <header className={`archive-heading ${introProgress >= 1 ? "is-dismissed" : ""}`} style={{ "--archive-intro": introProgress } as CSSProperties}><p>ARCHIVE / PAGE.OS / FIELD ENTRY 01</p><h2>THE MISSING<br /><em>CATALOGUE.</em></h2><span>SCROLL TO TURN THE PAGE</span><ArchiveDust progress={introProgress} /></header>
        <div className="archive-status"><span className="archive-status-dot" /> {collected.size} / 03 CARDS RECOVERED</div><div className="archive-light" aria-hidden="true" />
        <div className="archive-book-world" aria-label="PAGE.OS archive book">
          <div className="archive-shelf" aria-hidden="true"><span /><span /><span /><span /></div>
          <div className="archive-book-stack">{ARCHIVE_PAGES.map((page, index) => <ArchivePageLayer key={page.id} page={page} index={index} progress={gameProgress} collected={collected} onCollect={collectFragment} onNearFragment={nearFragment} reducedMotion={reducedMotion} />)}</div>
          <div className={`archive-radio ${collected.size > 0 ? "is-awake" : ""}`}><Radio /><span>{collected.size > 1 ? "...THE SHELF REMEMBERS..." : "NO CARRIER / 88.4"}</span></div>
          <div className={`archive-door ${finalReveal ? "is-open" : ""}`} aria-live="polite"><div className="archive-door-frame" /><div className="archive-door-leaf" /><div className="archive-door-screen"><small>CATALOGUE ENTRY RECOVERED</small><strong>PAGE<span>.</span>OS</strong><p>A GATEWAY TO OPEN KNOWLEDGE</p>{finalReveal && <div className="archive-door-actions"><a href="https://pageos.vercel.app" target="_blank" rel="noreferrer" data-cursor="ENTER PAGE.OS">ENTER LIVE PAGE.OS <ArrowUpRight className="h-3.5 w-3.5" /></a><button type="button" onClick={() => onOpenProject(pageOS)} data-cursor="READ BUILD NOTES">READ THE BUILD NOTES <BookOpen className="h-3.5 w-3.5" /></button></div>}</div></div>
        </div>
        <div className={`archive-instructions ${introProgress >= 1 ? "is-game-ready" : ""}`}><ChevronDown className="h-4 w-4" /> {introProgress >= 1 ? "MOVE THE LIGHT / FIND WHAT WAS LEFT BEHIND" : "SCROLL DOWN / THE CATALOGUE IS COMING APART"}</div>
        <div className="archive-reaction" aria-live="polite">{collected.size === 0 ? "THE DRAWER IS LOCKED" : collected.size === 1 ? "THE PAPER HAS MOVED" : collected.size === 2 ? "SOMETHING IS ON THE FREQUENCY" : "THE ARCHIVE HAS AN ADDRESS"}</div>
      </div>
    </section>
  );
}

function updateTouchLight(event: ReactPointerEvent<HTMLDivElement>, sceneRef: RefObject<HTMLDivElement>) {
  const scene = sceneRef.current; if (!scene) return;
  const rect = scene.getBoundingClientRect();
  scene.style.setProperty("--archive-light-x", `${Math.min(100, Math.max(0, ((event.clientX - rect.left) / rect.width) * 100))}%`);
  scene.style.setProperty("--archive-light-y", `${Math.min(100, Math.max(0, ((event.clientY - rect.top) / rect.height) * 100))}%`);
}
