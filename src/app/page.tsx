"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { ArrowUpRight, Copy, MoveRight } from "lucide-react";
import { FilmGrain } from "@/components/animations/FilmGrain";
import { CustomCursor } from "@/components/animations/CustomCursor";
import dynamic from "next/dynamic";
import { SystemNavigation } from "@/components/navigation/SystemNavigation";
import { TerminalDrawer } from "@/components/terminal/TerminalDrawer";
import { ProjectModal } from "@/components/sections/ProjectModal";
import { CipherLab } from "@/components/sections/CipherLabSection";
import { RoomForOneMoreSection } from "@/components/sections/RoomForOneMoreSection";
import { ChannelId, DualChannelSection } from "@/components/sections/DualChannelSection";
import { PageOSArchiveSection } from "@/components/sections/PageOSArchiveSection";
import { MobilePortfolioShell } from "@/components/mobile/MobilePortfolioShell";
import { useIsMobile } from "@/hooks/useIsMobile";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { EXHIBITION_PROJECTS, ExhibitionProject } from "@/lib/data/projects";

const IntersectionHeroCanvas = dynamic(
  () => import("@/components/3d/IntersectionHeroCanvas").then((mod) => mod.IntersectionHeroCanvas),
  { ssr: false, loading: () => <div className="h-full w-full animate-pulse bg-[#10151e]/30" /> },
);

const HERO_WORDS = [
  { text: "ENGINEERING", x: "73%", y: "18%", size: "text-[0.72rem] md:text-[1.05rem]", color: "#f97316" },
  { text: "FILM", x: "12%", y: "74%", size: "text-3xl md:text-5xl", color: "#fb923c" },
  { text: "AI", x: "84%", y: "34%", size: "text-5xl md:text-7xl", color: "#38bdf8" },
  { text: "WRITING", x: "14%", y: "22%", size: "text-sm md:text-xl", color: "#f2f0ea" },
  { text: "3D", x: "78%", y: "68%", size: "text-6xl md:text-8xl", color: "#8b5cf6" },
  { text: "SYSTEMS", x: "51%", y: "84%", size: "text-xs md:text-base", color: "#84cc16" },
  { text: "CIPHER", x: "4%", y: "48%", size: "text-xs md:text-sm", color: "#a78bfa" },
];

const VISUAL_ARCHIVE = [
  { title: "PAGE.OS", type: "knowledge discovery / reading systems", slug: "page-os", className: "top-[8%] left-[4%] w-[34vw] max-w-[360px] rotate-[-6deg]", gradient: "radial-gradient(circle at 28% 20%, rgba(56,189,248,0.18), transparent 25%), linear-gradient(180deg, #152033, #090d15)" },
  { title: "ANE", type: "audio / ml / narrative inference", slug: "ane", className: "top-[18%] right-[12%] w-[24vw] max-w-[270px] rotate-[7deg]", gradient: "radial-gradient(circle at 60% 20%, rgba(34,211,238,0.16), transparent 20%), linear-gradient(180deg, #101a20, #06090d)" },
  { title: "RESIDUAL", type: "film / visual storytelling", slug: "residual", className: "bottom-[18%] left-[10%] w-[26vw] max-w-[300px] rotate-[9deg]", gradient: "radial-gradient(circle at 50% 30%, rgba(249,115,22,0.15), transparent 26%), linear-gradient(180deg, #221712, #090707)" },
  { title: "THE FIFTH EXIT", type: "horror / architecture / liminal spaces", slug: "the-fifth-exit", className: "bottom-[10%] right-[18%] w-[28vw] max-w-[320px] rotate-[-8deg]", gradient: "radial-gradient(circle at 50% 25%, rgba(220,38,38,0.16), transparent 24%), linear-gradient(180deg, #190c0d, #060405)" },
  { title: "CIPHER", type: "glyph system / encoded language", slug: "cipher-system", className: "top-[54%] right-[3%] w-[18vw] max-w-[210px] rotate-[4deg]", gradient: "radial-gradient(circle at 50% 35%, rgba(139,92,246,0.18), transparent 24%), linear-gradient(180deg, #17120d, #070603)" },
];

const INTEREST_WORDS = [
  "FILM",
  "AI",
  "MECHATRONICS",
  "ROBOTICS",
  "3D",
  "WRITING",
  "HORROR",
  "PHILOSOPHY",
  "CRYPTOGRAPHY",
  "TYPOGRAPHY",
  "SYSTEMS",
  "CREATIVE CODING",
  "ARCHITECTURE",
  "SOFTWARE",
  "MOTION",
  "WORLD BUILDING",
];

const CURRENTLY_ITEMS = [
  ["BUILDING", "PAGE.OS"],
  ["EXPLORING", "AI / local models / creative systems"],
  ["MAKING", "film / 3d / visual experiments"],
  ["WRITING", "psychological horror"],
  ["LEARNING", "mechatronics / robotics / engineering"],
];

const INTERSECTIONS = [
  { left: "LITERATURE", right: "SOFTWARE", result: "PAGE.OS", accent: "#38bdf8" },
  { left: "AI", right: "AUDIO", result: "ANE", accent: "#22d3ee" },
  { left: "FILM", right: "DESIGN", result: "RESIDUAL", accent: "#fb923c" },
  { left: "WRITING", right: "HORROR", result: "A ROOM FOR ONE MORE", accent: "#f2f0ea" },
  { left: "CODE", right: "LANGUAGE", result: "CIPHER", accent: "#8b5cf6" },
  { left: "3D", right: "ENGINEERING", result: "EXPERIMENTS", accent: "#93c5fd" },
];

function ProjectPlate({
  project,
  onOpen,
  className,
}: {
  project: ExhibitionProject;
  onOpen: (project: ExhibitionProject) => void;
  className?: string;
}) {
  return (
    <motion.button
      whileHover={{ y: -8, rotate: 0 }}
      transition={{ type: "spring", stiffness: 180, damping: 22 }}
      onClick={() => onOpen(project)}
      className={`group project-plate text-left ${className ?? ""}`}
    >
      <div
        className="project-plate-surface"
        style={{
          background: `radial-gradient(circle at 25% 25%, ${project.accentColor}30, transparent 32%), linear-gradient(180deg, rgba(14,14,16,0.98), rgba(8,8,9,0.98))`,
        }}
      >
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-[10px] uppercase tracking-[0.28em] text-[#8f8b84]">{project.domain}</p>
            <h3 className="mt-3 font-display text-3xl leading-none text-[#f4f0e8] md:text-4xl">
              {project.title}
            </h3>
          </div>
          <span
            className="rounded-full border px-3 py-1 text-[10px] font-mono tracking-[0.22em]"
            style={{ borderColor: `${project.accentColor}55`, color: project.accentColor }}
          >
            {project.status}
          </span>
        </div>

        <p className="mt-5 max-w-md text-sm leading-relaxed text-[#b7b0a5] md:text-[0.95rem]">
          {project.summary}
        </p>

        <div className="mt-8 flex flex-wrap gap-2">
          {project.technologies.slice(0, 4).map((tech) => (
            <span
              key={tech}
              className="rounded-full border px-3 py-1 text-[10px] font-mono tracking-[0.14em] text-[#c9c2b8]"
              style={{ borderColor: `${project.accentColor}22` }}
            >
              {tech}
            </span>
          ))}
        </div>

        <div className="mt-10 flex items-center justify-between border-t border-white/5 pt-4">
          <span className="text-[10px] font-mono tracking-[0.22em] text-[#817c74]">{project.year}</span>
          <span className="flex items-center gap-2 text-[11px] tracking-[0.18em] text-[#f4f0e8]">
            OPEN CASE STUDY <ArrowUpRight className="h-3.5 w-3.5 transition-transform duration-300 group-hover:translate-x-1 group-hover:-translate-y-1" />
          </span>
        </div>
      </div>
    </motion.button>
  );
}

export default function Home() {
  const [selectedProject, setSelectedProject] = useState<ExhibitionProject | null>(null);
  const [activeChannel, setActiveChannel] = useState<ChannelId>("page-os");
  const [activeSection, setActiveSection] = useState("hero");
  const [heroMouse, setHeroMouse] = useState({ x: 0, y: 0 });
  const [isTerminalOpen, setIsTerminalOpen] = useState(false);
  const isMobile = useIsMobile();

  useEffect(() => {
    const handleScroll = () => {
      const sectionIds = ["hero", "work", "channels", "archive", "intersections", "writing", "experiments", "contact"];
      for (const id of [...sectionIds].reverse()) {
        const element = document.getElementById(id);
        if (element && element.getBoundingClientRect().top < window.innerHeight * 0.33) {
          setActiveSection(id);
          break;
        }
      }
    };

    handleScroll();
    window.addEventListener("scroll", handleScroll, { passive: true });
    const handleSlash = (event: KeyboardEvent) => {
      if (event.key === "/" && document.activeElement?.tagName !== "INPUT") {
        event.preventDefault();
        setIsTerminalOpen(true);
      }
    };
    window.addEventListener("keydown", handleSlash);
    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("keydown", handleSlash);
    };
  }, []);

  useEffect(() => {
    let firstFrame = 0;
    let secondFrame = 0;
    firstFrame = window.requestAnimationFrame(() => {
      secondFrame = window.requestAnimationFrame(() => ScrollTrigger.refresh());
    });
    return () => {
      window.cancelAnimationFrame(firstFrame);
      window.cancelAnimationFrame(secondFrame);
    };
  }, [activeChannel]);

  return (
    <main className="relative min-h-screen overflow-x-hidden bg-[#050505] text-[#f2f0ea]">
      <FilmGrain />
      <CustomCursor />

      <SystemNavigation activeSection={activeSection} onOpenTerminal={() => setIsTerminalOpen(true)} />

      {isMobile === null ? (
        <div className="portfolio-mode-loading" aria-hidden="true" />
      ) : isMobile ? (
        <MobilePortfolioShell activeChannel={activeChannel} onChannelChange={setActiveChannel} onOpenProject={setSelectedProject} />
      ) : (
        <>

      <section
        id="hero"
        className="relative min-h-screen overflow-hidden px-4 pb-10 pt-24 md:px-8 md:pb-14 md:pt-28"
        onMouseMove={(event) => {
          const { innerWidth, innerHeight } = window;
          setHeroMouse({
            x: (event.clientX / innerWidth - 0.5) * 2,
            y: (event.clientY / innerHeight - 0.5) * 2,
          });
        }}
      >
        <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_50%_42%,rgba(107,33,168,0.34),transparent_32%),radial-gradient(circle_at_78%_20%,rgba(34,211,238,0.14),transparent_20%),radial-gradient(circle_at_25%_75%,rgba(249,115,22,0.12),transparent_24%)]" />
        <div className="pointer-events-none absolute inset-0 grid-overlay opacity-35" />

        <div className="hero-shell mx-auto grid min-h-[calc(100vh-7rem)] max-w-[1440px] grid-cols-1 gap-6 overflow-hidden rounded-[2rem] border border-white/8 bg-[#090909]/96 px-5 py-6 shadow-[0_40px_140px_rgba(0,0,0,0.5)] md:px-8 md:py-8 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="relative min-h-[540px] overflow-hidden rounded-[1.5rem] bg-[radial-gradient(circle_at_50%_45%,#273a4b_0%,#10151e_35%,#080a0f_78%)]">
            <div
              className="absolute inset-0"
              style={{ transform: `translate(${heroMouse.x * -12}px, ${heroMouse.y * -10}px)` }}
            >
              <IntersectionHeroCanvas />
            </div>
            <div className="absolute inset-0 grid-overlay opacity-30" />
            <div className="absolute left-4 top-4 flex items-center gap-2 text-[10px] font-mono tracking-[0.16em] text-white/60 md:left-6 md:top-6">
              <span className="status-dot" />
              <span>CORE / SUSPENDED</span>
            </div>
            <div className="absolute bottom-5 left-5 max-w-xs text-white/88 md:bottom-8 md:left-8">
              <p className="text-[10px] font-mono tracking-[0.26em] text-[#9ccfd0]/70">ARCHIVE CORE / NAVIGATION OBJECT</p>
              <p className="mt-3 text-sm leading-relaxed md:text-base">
                A small machine for holding objects, systems, interfaces, and stories that keep leaking into each other.
              </p>
            </div>
            <div className="absolute right-4 top-4 text-right text-[9px] font-mono leading-relaxed tracking-[0.12em] text-white/40 md:right-6 md:top-6">
              <p>ROTATE / POINTER</p>
              <p>READ / SCROLL</p>
            </div>
          </div>

          <div className="relative flex min-h-[540px] flex-col justify-between overflow-hidden rounded-[1.5rem] bg-[#0c0c0d] p-5 md:p-8">
            <div className="space-y-6">
              <p className="text-[10px] font-mono tracking-[0.26em] text-[#8f8b84]">
                MECHATRONICS / SOFTWARE / AI / FILM / 3D / WRITING
              </p>

              <div
                style={{ transform: `translate(${heroMouse.x * 9}px, ${heroMouse.y * 7}px)` }}
                className="relative z-10"
              >
                <h1 className="font-heading text-[18vw] font-semibold uppercase leading-[0.82] tracking-[0.16em] text-[#f3efe6] sm:text-[7rem] md:text-[9rem] lg:text-[10rem]">
                  HEY
                  <br />
                  THIS
                  <br />
                  IS
                </h1>
                <div className="mt-4 flex items-end gap-3">
                  <span className="font-display text-[3.8rem] italic leading-none text-transparent [-webkit-text-stroke:1px_rgba(242,240,234,0.8)] md:text-[5.5rem]">
                    YASH
                  </span>
                  <span className="pb-3 text-sm tracking-[0.04em] text-[#b8b1a7] md:text-base">
                    I build. I make. I experiment.
                  </span>
                </div>
              </div>

              <p className="max-w-[26rem] text-base leading-relaxed text-[#b8b1a7] md:text-lg">
                I am a mechatronics engineering student in Mumbai working across robotics, AI, software, 3D, filmmaking, typography, horror, and interactive systems.
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-4 pt-8">
              <a href="#work" className="magnetic-pill bg-[#f2f0ea] text-[#050505]">
                ENTER THE WORK
              </a>
              <a href="#writing" className="magnetic-pill border border-white/12 text-[#f2f0ea]">
                OPEN MANUSCRIPTS
              </a>
            </div>

            {HERO_WORDS.map((word) => (
              <span
                key={word.text}
                className={`pointer-events-none absolute font-heading font-semibold uppercase ${word.size}`}
                style={{
                  left: word.x,
                  top: word.y,
                  color: word.color,
                  opacity: 0.14,
                  transform: `translate(${heroMouse.x * 10}px, ${heroMouse.y * 6}px)`,
                }}
              >
                {word.text}
              </span>
            ))}

            <div className="absolute bottom-5 right-5 flex items-center gap-3 text-[10px] font-mono tracking-[0.24em] text-[#8f8b84] md:bottom-8 md:right-8">
              <span>SCROLL</span>
              <MoveRight className="h-3.5 w-3.5" />
            </div>
          </div>
        </div>
      </section>

      <section className="relative px-4 py-20 md:px-8 md:py-28">
        <div className="mx-auto grid max-w-[1440px] gap-10 lg:grid-cols-[1.1fr_0.9fr]">
          <div>
            <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">ABOUT ME</p>
            <h2 className="mt-5 font-display text-[4rem] leading-[0.88] text-[#f2f0ea] sm:text-[5.5rem] md:text-[7rem] lg:text-[8.5rem]">
              I LIKE TAKING
              <br />
              THINGS
              <span className="text-[#a78bfa]"> APART</span>
              <br />
              TO SEE WHAT
              <br />
              ELSE THEY CAN
              <br />
              BECOME.
            </h2>
          </div>

          <div className="space-y-8">
            <div className="rounded-[1.75rem] border border-white/7 bg-[#0c0c0d] p-6 md:p-8">
              <p className="text-lg leading-relaxed text-[#c7c0b5] md:text-xl">
                I study mechatronics, but I do not stay in one lane for long. I build reading systems, train narrative AI, direct films, sketch procedural geometry in Blender, write psychological horror, and design my own glyph alphabet because language itself feels like an interface problem.
              </p>
              <p className="mt-5 text-base leading-relaxed text-[#8f8b84]">
                I am interested in the collisions between disciplines more than the labels around them. Most of my work starts with the same question: what happens when one medium borrows the logic of another?
              </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-2">
              {["machines", "software", "interfaces", "stories", "systems", "visual language"].map((item, index) => (
                <motion.div
                  key={item}
                  initial={{ opacity: 0, y: 18 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true, margin: "-80px" }}
                  transition={{ duration: 0.55, delay: index * 0.05 }}
                  className="rounded-[1.25rem] border border-white/7 bg-[#090909] px-4 py-5"
                >
                  <p className="text-[10px] font-mono tracking-[0.25em] text-[#8f8b84]">I TAKE APART</p>
                  <p className="mt-2 font-display text-3xl text-[#f2f0ea] md:text-4xl">{item}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="work" className="relative overflow-hidden px-4 py-20 md:px-8 md:py-28">
        <div className="mx-auto max-w-[1440px]">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">SELECTED WORK</p>
              <h2 className="mt-4 font-display text-[4.2rem] leading-[0.9] text-[#f2f0ea] sm:text-[5.6rem] md:text-[7rem]">
                NOT ONE
                <br />
                DISCIPLINE.
              </h2>
            </div>
            <p className="max-w-xl text-base leading-relaxed text-[#b8b1a7] md:text-lg">
              I did not want this to turn into a wall of identical cards, so every project sits inside a different atmosphere. The goal is to make the portfolio feel like moving through separate worlds that still belong to the same person.
            </p>
          </div>

          <div className="relative mt-14 hidden h-[760px] overflow-hidden rounded-[2rem] border border-white/7 bg-[#090909] lg:block">
            <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(124,58,237,0.22),transparent_26%),radial-gradient(circle_at_18%_26%,rgba(251,146,60,0.12),transparent_18%)]" />
            <div className="pointer-events-none absolute inset-0 grid-overlay opacity-25" />
            <div className="pointer-events-none absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 text-center">
              <p className="font-display text-[8rem] leading-none text-[#8b5cf6] opacity-75">WORK</p>
              <p className="mt-2 text-sm tracking-[0.35em] text-[#8f8b84]">VISUAL ARCHIVE / ACTIVE WORLDS</p>
            </div>

            {VISUAL_ARCHIVE.map((item) => {
              const project = EXHIBITION_PROJECTS.find((entry) => entry.id === item.slug);
              if (!project) return null;

              return (
                <motion.button
                  key={item.slug}
                  whileHover={{ y: -10, scale: 1.02 }}
                  onClick={() => setSelectedProject(project)}
                  className={`absolute rounded-[1.35rem] border border-white/8 p-4 text-left shadow-[0_28px_90px_rgba(0,0,0,0.45)] transition-transform ${item.className}`}
                  style={{ background: item.gradient }}
                >
                  <div className="aspect-[1.15/1] overflow-hidden rounded-[1rem] border border-white/8 bg-black/30 p-4">
                    <div className="flex h-full flex-col justify-between">
                      <p className="text-[10px] font-mono tracking-[0.28em] text-white/56">{item.type}</p>
                      <div>
                        <p className="font-heading text-2xl font-semibold tracking-[0.08em] text-white md:text-3xl">{item.title}</p>
                        <p className="mt-2 text-sm leading-relaxed text-white/72">{project.tagline}</p>
                      </div>
                    </div>
                  </div>
                </motion.button>
              );
            })}
          </div>

          <div className="mt-10 grid gap-5 lg:mt-14 lg:grid-cols-2">
            {EXHIBITION_PROJECTS.map((project, index) => (
              <ProjectPlate
                key={project.id}
                project={project}
                onOpen={setSelectedProject}
                className={index === 0 || index === 3 || index === 5 ? "lg:translate-y-10" : ""}
              />
            ))}
          </div>
        </div>
      </section>

      <DualChannelSection onOpenProject={setSelectedProject} onChannelChange={setActiveChannel} />

      <PageOSArchiveSection onOpenProject={setSelectedProject} enabled={activeChannel === "page-os"} />

      <section id="intersections" className="relative overflow-hidden px-4 py-20 md:px-8 md:py-28">
        <div className="mx-auto max-w-[1440px] rounded-[2rem] border border-white/7 bg-[#0b0b0d] p-6 md:p-10">
          <div className="grid gap-10 lg:grid-cols-[0.92fr_1.08fr]">
            <div>
              <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">INTEREST FIELD</p>
              <div className="mt-6 flex flex-wrap gap-x-5 gap-y-4">
                {INTEREST_WORDS.map((word, index) => (
                  <span
                    key={word}
                    className="font-display leading-none text-[#f2f0ea]"
                    style={{
                      fontSize: index % 5 === 0 ? "4.8rem" : index % 3 === 0 ? "2.6rem" : "1.5rem",
                      opacity: index % 4 === 0 ? 1 : 0.72,
                    }}
                  >
                    {word}
                  </span>
                ))}
              </div>
            </div>

            <div>
              <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">COLLISION SYSTEM</p>
              <div className="mt-6 space-y-3">
                {INTERSECTIONS.map((item, index) => (
                  <motion.div
                    key={item.result}
                    initial={{ opacity: 0, x: 24 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true, margin: "-80px" }}
                    transition={{ duration: 0.55, delay: index * 0.05 }}
                    className="grid items-center gap-3 rounded-[1.25rem] border border-white/7 bg-[#080809] px-4 py-4 md:grid-cols-[1fr_auto_1fr_auto_1.3fr]"
                  >
                    <span className="font-heading text-lg tracking-[0.1em] text-[#d8d1c7]">{item.left}</span>
                    <span className="text-[#817c74]">+</span>
                    <span className="font-heading text-lg tracking-[0.1em] text-[#d8d1c7]">{item.right}</span>
                    <span className="text-[#817c74]">=</span>
                    <span className="font-display text-3xl leading-none" style={{ color: item.accent }}>
                      {item.result}
                    </span>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      <RoomForOneMoreSection />

      <section id="experiments" className="relative overflow-hidden px-4 py-20 md:px-8 md:py-28">
        <div className="mx-auto max-w-[1440px] space-y-10">
          <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">EXPERIMENTS</p>
              <h2 className="mt-4 font-display text-[4.2rem] leading-[0.9] text-[#f2f0ea] sm:text-[5.5rem] md:text-[7rem]">
                LANGUAGE,
                <br />
                CODE,
                <br />
                MOTION.
              </h2>
            </div>
            <p className="max-w-xl text-base leading-relaxed text-[#b8b1a7] md:text-lg">
              This is where the portfolio becomes more instrument-like. The glyph system is live, the generative sketches are interactive, and the interface starts behaving less like a catalog and more like a lab.
            </p>
          </div>

          <div>
            <div className="cipher-installation-frame rounded-[1.8rem] border border-white/7 bg-[#080809]/90 p-5 md:p-7">
              <div className="mb-5 flex items-center gap-2 text-[10px] font-mono tracking-[0.28em] text-[#8f8b84]">
                <Copy className="h-3.5 w-3.5" />
                CIPHER INSTALLATION
              </div>
              <CipherLab />
            </div>
          </div>
        </div>
      </section>

      <section className="relative px-4 py-20 md:px-8 md:py-24">
        <div className="mx-auto max-w-[1440px] rounded-[2rem] border border-white/7 bg-[#0a0a0b] p-6 md:p-10">
          <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">CURRENTLY</p>
          <div className="mt-8 grid gap-3 md:grid-cols-2 xl:grid-cols-5">
            {CURRENTLY_ITEMS.map(([label, value]) => (
              <div key={label} className="rounded-[1.2rem] border border-white/7 bg-[#050505] p-4">
                <p className="text-[10px] font-mono tracking-[0.26em] text-[#8f8b84]">{label}</p>
                <p className="mt-3 text-sm leading-relaxed text-[#f2f0ea]">{value}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer id="contact" className="relative px-4 pb-16 pt-8 md:px-8 md:pb-20">
        <div className="mx-auto max-w-[1440px] border-t border-white/8 pt-10">
          <div className="grid gap-10 lg:grid-cols-[1fr_auto] lg:items-end">
            <div>
              <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">CONTACT</p>
              <h2 className="mt-5 font-display text-[4.4rem] leading-[0.86] text-[#f2f0ea] sm:text-[5.8rem] md:text-[8rem]">
                I AM STILL
                <br />
                BUILDING.
              </h2>
              <p className="mt-6 max-w-xl text-lg leading-relaxed text-[#b8b1a7]">
                If you want to talk about reading systems, AI, horror, interfaces, 3D, filmmaking, or strange combinations of all of them, reach out.
              </p>
            </div>

            <div className="space-y-3 text-left lg:text-right">
              <a href="mailto:contact@yash.dev" className="block text-xl tracking-[0.08em] text-[#f2f0ea]">
                contact@yash.dev
              </a>
              <a href="https://github.com/Wafion" target="_blank" rel="noreferrer" className="block text-sm tracking-[0.24em] text-[#8f8b84] hover:text-[#f2f0ea]">
                GITHUB
              </a>
              <a href="https://www.linkedin.com/in/yash-sawant-1776a7399/" target="_blank" rel="noreferrer" className="block text-sm tracking-[0.24em] text-[#8f8b84] hover:text-[#f2f0ea]">
                LINKEDIN
              </a>
              <button
                onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
                className="mt-4 inline-flex items-center gap-2 rounded-full border border-white/10 px-4 py-2 text-[10px] font-mono tracking-[0.24em] text-[#f2f0ea]"
              >
                BACK TO TOP <ArrowUpRight className="h-3.5 w-3.5" />
              </button>
            </div>
          </div>
        </div>
      </footer>
        </>
      )}

      <ProjectModal project={selectedProject} onClose={() => setSelectedProject(null)} />
      <TerminalDrawer
        isOpen={isTerminalOpen}
        onClose={() => setIsTerminalOpen(false)}
        onSelectProject={(slug) => {
          setSelectedProject(EXHIBITION_PROJECTS.find((project) => project.slug === slug) ?? null);
        }}
      />
    </main>
  );
}
