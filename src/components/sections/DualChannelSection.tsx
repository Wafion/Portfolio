"use client";

import { useState } from "react";
import type { CSSProperties } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { ArrowUpRight, Film, Layers3, Terminal } from "lucide-react";
import { EXHIBITION_PROJECTS, ExhibitionProject } from "@/lib/data/projects";

export type ChannelId = "page-os" | "residual";

const CHANNELS: Array<{
  id: ChannelId;
  number: string;
  label: string;
  eyebrow: string;
  accent: string;
}> = [
  { id: "page-os", number: "01", label: "PAGE.OS", eyebrow: "READING SYSTEM", accent: "#65c9e8" },
  { id: "residual", number: "02", label: "THE RESIDUAL", eyebrow: "PRODUCTION CHANNEL", accent: "#d6a05b" },
];

const PAGE_OS_TRAIL = ["OPEN / CLASSIC MODE", "FOLLOW / SEMANTIC TRAIL", "INDEX / FIELD NOTES", "SAVE / LIBRARY"];
const RESIDUAL_SHOTS = ["03 / THE ROOM", "07 / AFTERIMAGE", "11 / THE RETURN"];

function PageOSInstrument() {
  return (
    <div className="channel-instrument-page h-full">
      <div className="channel-instrument-top">
        <span>PAGE.OS / READING TRAIL</span>
        <span>SYNC 04.27</span>
      </div>
      <div className="channel-terminal-window">
        <div className="channel-terminal-bar">
          <span className="channel-terminal-dot" />
          <span className="channel-terminal-dot" />
          <span className="channel-terminal-dot" />
          <span className="ml-auto">LOCAL INDEX / ONLINE</span>
        </div>
        <div className="channel-terminal-copy">
          <p className="text-[#65c9e8]">&gt; open page.os</p>
          <p className="text-white/55">A reading environment for interconnected thought.</p>
          <p className="mt-5 text-white/80">&gt; follow trail <span className="text-[#65c9e8]">literature / systems</span></p>
        </div>
        <div className="channel-trail">
          {PAGE_OS_TRAIL.map((step, index) => (
            <motion.div
              key={step}
              initial={{ opacity: 0, x: -10 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1, duration: 0.45 }}
              className="channel-trail-step"
            >
              <span className="channel-trail-node" />
              <span>{step}</span>
            </motion.div>
          ))}
        </div>
        <div className="channel-mode-row">
          {[
            ["CLASSIC", "books"],
            ["LOUNGE", "context"],
            ["INFINITY", "discovery"],
          ].map(([mode, detail], index) => (
            <div key={mode} className={index === 0 ? "channel-mode active" : "channel-mode"}>
              <span>{mode}</span>
              <small>{detail}</small>
            </div>
          ))}
        </div>
      </div>
      <div className="channel-instrument-footer">
        <span><Terminal className="h-3 w-3" /> KNOWLEDGE / IN MOTION</span>
        <span>VECTOR 01.03</span>
      </div>
    </div>
  );
}

function ResidualInstrument() {
  return (
    <div className="channel-instrument-residual h-full">
      <div className="channel-instrument-top">
        <span>RESIDUAL / PRODUCTION CHANNEL</span>
        <span>ROLLING 02.39</span>
      </div>
      <div className="channel-film-stage">
        <div className="channel-film-frame">
          <div className="channel-frame-crosshair" />
          <div className="channel-frame-caption">THE RESIDUAL</div>
          <div className="channel-frame-meta">LOW-KEY / 24 FPS / ACES</div>
          <div className="channel-film-subject" />
          <div className="channel-frame-line" />
        </div>
        <div className="channel-film-readout">
          <span>SHOT 07</span>
          <span>FADE IN / HOLD / CUT</span>
        </div>
        <div className="channel-shot-list">
          {RESIDUAL_SHOTS.map((shot, index) => (
            <div key={shot} className={index === 1 ? "channel-shot active" : "channel-shot"}>
              <span>{shot}</span>
              <span>{index === 1 ? "LIVE" : "ARCHIVE"}</span>
            </div>
          ))}
        </div>
        <div className="channel-timeline">
          <span className="channel-timeline-playhead" />
          {Array.from({ length: 22 }, (_, index) => <i key={index} style={{ height: `${18 + ((index * 17) % 42)}%` }} />)}
        </div>
      </div>
      <div className="channel-instrument-footer">
        <span><Film className="h-3 w-3" /> IMAGE / SOUND / RHYTHM</span>
        <span>TAKE 014</span>
      </div>
    </div>
  );
}

export function DualChannelSection({ onOpenProject, onChannelChange }: { onOpenProject: (project: ExhibitionProject) => void; onChannelChange?: (channel: ChannelId) => void }) {
  const [activeChannel, setActiveChannel] = useState<ChannelId>("page-os");
  const pageOS = EXHIBITION_PROJECTS.find((project) => project.id === "page-os");
  const residual = EXHIBITION_PROJECTS.find((project) => project.id === "residual");

  if (!pageOS || !residual) return null;

  const project = activeChannel === "page-os" ? pageOS : residual;
  const channel = CHANNELS.find((item) => item.id === activeChannel) ?? CHANNELS[0];
  const isPageOS = activeChannel === "page-os";

  return (
    <section id="channels" className="channel-section relative overflow-hidden px-4 py-20 md:px-8 md:py-32">
      <div className="channel-section-orbit" />
      <div className="mx-auto max-w-[1440px]">
        <div className="flex flex-col gap-8 border-b border-[#f2f0ea]/12 pb-8 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <p className="text-[10px] font-mono tracking-[0.3em] text-[#8f8b84]">CONNECTED PRACTICES / 02 CHANNELS</p>
            <h2 className="mt-4 max-w-3xl font-display text-[3.8rem] leading-[0.88] text-[#f2f0ea] sm:text-[5.4rem] md:text-[7.5rem]">
              TWO CHANNELS.
              <br />
              <em>ONE PRACTICE.</em>
            </h2>
          </div>
          <p className="max-w-md text-base leading-relaxed text-[#aaa39a] md:text-lg">
            One channel follows thought through text. The other follows attention through image and sound. Both are built from the same instinct: make the medium part of the meaning.
          </p>
        </div>

        <div className="channel-switcher" role="tablist" aria-label="Choose a practice channel">
          {CHANNELS.map((item) => (
            <button
              key={item.id}
              role="tab"
              aria-selected={activeChannel === item.id}
              onClick={() => {
                setActiveChannel(item.id);
                onChannelChange?.(item.id);
              }}
              className={activeChannel === item.id ? "channel-tab active" : "channel-tab"}
              style={{ "--channel-accent": item.accent } as CSSProperties}
              data-cursor={`OPEN ${item.label}`}
            >
              <span>{item.number}</span>
              <strong>{item.label}</strong>
              <small>{item.eyebrow}</small>
            </button>
          ))}
        </div>

        <div className="channel-layout">
          <div className="channel-instrument-wrap" data-cursor={`${channel.label} / LIVE`}>
            <AnimatePresence mode="wait" initial={false}>
              <motion.div
                key={activeChannel}
                initial={{ opacity: 0, y: 14, filter: "blur(5px)" }}
                animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                exit={{ opacity: 0, y: -14, filter: "blur(5px)" }}
                transition={{ duration: 0.4 }}
                className="h-full"
              >
                {isPageOS ? <PageOSInstrument /> : <ResidualInstrument />}
              </motion.div>
            </AnimatePresence>
          </div>

          <div className="channel-copy">
            <AnimatePresence mode="wait" initial={false}>
              <motion.div key={activeChannel} initial={{ opacity: 0, x: 16 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -16 }} transition={{ duration: 0.35 }}>
                <div className="flex items-center gap-3 text-[10px] font-mono tracking-[0.28em]" style={{ color: channel.accent }}>
                  {isPageOS ? <Layers3 className="h-4 w-4" /> : <Film className="h-4 w-4" />}
                  {channel.eyebrow}
                </div>
                <h3 className="mt-6 font-display text-5xl leading-[0.92] text-[#f2f0ea] md:text-7xl">{project.title}</h3>
                <p className="mt-5 max-w-xl text-xl leading-relaxed text-[#ded8ce]">{project.tagline}</p>
                <p className="mt-6 max-w-xl text-sm leading-relaxed text-[#989189] md:text-base">{project.summary}</p>
                <div className="mt-8 flex flex-wrap gap-2">
                  {project.technologies.slice(0, 5).map((technology) => <span key={technology} className="channel-tag">{technology}</span>)}
                </div>
                <div className="mt-10 flex flex-wrap items-center gap-5 border-t border-[#f2f0ea]/12 pt-5">
                  <button onClick={() => onOpenProject(project)} className="channel-open-button" data-cursor="OPEN CASE STUDY">
                    OPEN CASE STUDY <ArrowUpRight className="h-4 w-4" />
                  </button>
                  <span className="text-[10px] font-mono tracking-[0.2em] text-[#77736d]">{project.year} / {project.status}</span>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}
