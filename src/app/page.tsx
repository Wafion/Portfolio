"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { ArrowUpRight, Copy } from "lucide-react";
import { FilmGrain } from "@/components/animations/FilmGrain";
import { CustomCursor } from "@/components/animations/CustomCursor";
import { SystemNavigation } from "@/components/navigation/SystemNavigation";
import { TerminalDrawer } from "@/components/terminal/TerminalDrawer";
import { ProjectModal } from "@/components/sections/ProjectModal";
import { CipherLab } from "@/components/sections/CipherLabSection";
import { RoomForOneMoreSection } from "@/components/sections/RoomForOneMoreSection";
import { ChannelId, DualChannelSection } from "@/components/sections/DualChannelSection";
import { PageOSArchiveSection } from "@/components/sections/PageOSArchiveSection";
import { LiminalHeroSection } from "@/components/sections/LiminalHeroSection";
import { MobilePortfolioShell } from "@/components/mobile/MobilePortfolioShell";
import { useIsMobile } from "@/hooks/useIsMobile";
import { ThemeProvider, useTheme } from "@/lib/theme/ThemeProvider";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { EXHIBITION_PROJECTS, ExhibitionProject } from "@/lib/data/projects";

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

function HomeContent() {
  const [selectedProject, setSelectedProject] = useState<ExhibitionProject | null>(null);
  const [activeChannel, setActiveChannel] = useState<ChannelId>("page-os");
  const [activeSection, setActiveSection] = useState("hero");
  const [isTerminalOpen, setIsTerminalOpen] = useState(false);
  const isMobile = useIsMobile();
  const { resolvedTheme } = useTheme();
  const isLight = resolvedTheme === "light";

  useEffect(() => {
    const handleScroll = () => {
      const sectionIds = ["hero", "work", "channels", "archive", "intersections", "writing", "experiments", "contact"];
      const scrollY = window.scrollY;
      const nearBottom = scrollY + window.innerHeight >= document.documentElement.scrollHeight - 120;
      if (nearBottom) {
        setActiveSection("contact");
        return;
      }
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
    <main className={`${isLight ? "portfolio-light " : ""}relative min-h-screen overflow-x-hidden bg-background text-foreground`}>
      <FilmGrain />
      <CustomCursor />

      <SystemNavigation activeSection={activeSection} onOpenTerminal={() => setIsTerminalOpen(true)} />

      {isMobile === null ? (
        <div className="portfolio-mode-loading" aria-hidden="true" />
      ) : isMobile ? (
        <MobilePortfolioShell activeChannel={activeChannel} onChannelChange={setActiveChannel} onOpenProject={setSelectedProject} />
      ) : (
        <>

      <LiminalHeroSection />

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
                  className={`archive-card-item absolute rounded-[1.35rem] border border-white/8 p-4 text-left shadow-[0_28px_90px_rgba(0,0,0,0.45)] transition-transform ${item.className}`}
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

export default function Home() {
  return (
    <ThemeProvider>
      <HomeContent />
    </ThemeProvider>
  );
}
