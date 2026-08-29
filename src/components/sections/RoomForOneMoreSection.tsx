"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { ArrowLeft, ArrowRight, ChevronDown } from "lucide-react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { sound } from "@/components/audio/SoundEngine";
import { GlyphWord } from "@/components/ui/GlyphSymbol";

const PAGES = [
  {
    tab: "01 / LOSS",
    title: "The Weight of Loss",
    text: "Room For One More is a psychological horror novel about Ira Elowen Mireille, a young artist rebuilding a life after loss. When ordinary shelter becomes impossible, grief leaves her open to a house that promises a way forward.",
    note: "ira / grief / an opening",
  },
  {
    tab: "02 / HOUSE",
    title: "A Room in Valombre",
    text: "In Valombre, a remote French town, Ira finds a Victorian house with an impossible rent. Its quiet, careful hospitality feels like rescue, but the building seems to keep its own account of who enters.",
    note: "valombre / shelter / the house",
  },
  {
    tab: "03 / SHIFTS",
    title: "The First Shifts",
    text: "The novel follows Ira as the house stops behaving like a stable place. Art, memory, and routine become unreliable, turning domestic space into a shifting psychological maze.",
    note: "art / memory / unstable rooms",
  },
  {
    tab: "04 / PATTERNS",
    title: "Names in the Margin",
    text: "As isolation deepens, Ira begins to trace the history beneath the house. Room For One More is interested in identity, possession, and the fear that a home can know more about you than you know about yourself.",
    note: "identity / possession / hidden history",
  },
];

function wrapForPaper(text: string, maxChars = 42) {
  const lines: string[] = [];
  let line = "";
  text.split(" ").forEach((word) => {
    const next = line ? `${line} ${word}` : word;
    if (line && next.length > maxChars) {
      lines.push(line);
      line = word;
    } else {
      line = next;
    }
  });
  if (line) lines.push(line);
  return lines.join("\n");
}

export function RoomForOneMoreSection() {
  const sectionRef = useRef<HTMLElement>(null);
  const [pageIndex, setPageIndex] = useState(0);
  const [progress, setProgress] = useState(0);
  const [isActive, setIsActive] = useState(false);
  const page = PAGES[pageIndex];
  const typedText = useMemo(() => page.text.slice(0, Math.max(0, Math.floor(progress * page.text.length))), [page.text, progress]);
  const paperText = useMemo(() => wrapForPaper(typedText), [typedText]);
  const paperHeight = Math.min(14.3, Math.max(11.2, 6.7 + Math.max(1, paperText.split("\n").length) * 1.28));

  useEffect(() => {
    const section = sectionRef.current;
    if (!section) return;
    gsap.registerPlugin(ScrollTrigger);
    let lastCount = 0;
    let lastSoundAt = 0;
    let raf = 0;
    const update = () => {
      const rect = section.getBoundingClientRect();
      const range = Math.max(section.offsetHeight - window.innerHeight, 1);
      const nextProgress = Math.min(1, Math.max(0, -rect.top / range));
      setProgress(nextProgress);
      setIsActive(rect.top < window.innerHeight * 0.72 && rect.bottom > window.innerHeight * 0.25);
      const count = Math.floor(nextProgress * page.text.length);
      if (count > lastCount && Math.floor(count / 2) !== Math.floor(lastCount / 2)) {
        if (page.text[count - 1] !== " ") sound.playTypewriterKey();
      }
      lastCount = count;
      raf = 0;
    };
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update);
    };

    const media = gsap.matchMedia();
    media.add("(min-width: 769px)", () => {
      const playhead = { progress: 0 };
      const typing = gsap.to(playhead, {
        progress: 1,
        duration: 1,
        ease: "none",
        paused: true,
        onUpdate: () => {
          setProgress(playhead.progress);
          const count = Math.floor(playhead.progress * page.text.length);
          const now = performance.now();
          if (count > lastCount && now - lastSoundAt > 85) {
            if (page.text[count - 1] !== " ") sound.playTypewriterKey();
            lastSoundAt = now;
          }
          lastCount = count;
        },
      });
      const trigger = ScrollTrigger.create({
        trigger: section,
        animation: typing,
        pin: true,
        start: "top top",
        end: () => `+=${window.innerHeight * 1.4}`,
        scrub: 3.5,
        pinSpacing: true,
        anticipatePin: 1,
        invalidateOnRefresh: true,
        refreshPriority: -1,
        onToggle: (self) => setIsActive(self.isActive),
      });
      return () => {
        trigger.kill();
        typing.kill();
      };
    });

    media.add("(max-width: 768px)", () => {
      update();
      window.addEventListener("scroll", onScroll, { passive: true });
      return () => window.removeEventListener("scroll", onScroll);
    });

    return () => {
      media.revert();
      if (raf) cancelAnimationFrame(raf);
    };
  }, [page.text]);

  const changePage = (index: number) => {
    setPageIndex(index);
    setProgress(0);
    sound.playTypewriterReturn();
  };

  return (
    <section ref={sectionRef} id="writing" className="room-section relative bg-[#e7dfd1] px-4 py-0 text-[#171513] md:px-8">
      <div className="paper-noise pointer-events-none absolute inset-0 opacity-40" />
      <div className="room-pin relative mx-auto flex min-h-screen w-full max-w-[1440px] flex-col justify-center">
        <div className="mb-7 flex flex-col gap-5 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="text-[10px] font-mono tracking-[0.3em] text-[#756c60]">WRITING / ARCHIVAL INSTALLATION / 04 PAGES</p>
            <h2 className="mt-5 max-w-3xl font-display text-[4.4rem] leading-[0.84] sm:text-[6rem] md:text-[6.3rem] lg:text-[7rem]">A ROOM<br />FOR ONE<br /><em>MORE.</em></h2>
          </div>
          <p className="max-w-sm text-sm leading-relaxed text-[#5d554b]">Scroll through the manuscript. The machine will keep writing until the page remembers enough.</p>
        </div>

        <div className="grid gap-8 lg:grid-cols-[0.82fr_1.18fr] lg:gap-14">
          <div className={`typewriter-stage ${isActive ? "is-active" : ""}`}>
            <div className="typewriter-status"><span className="typewriter-light" /> {isActive ? "WRITING / LIVE" : "IDLE / SCROLL TO WRITE"}</div>
            <div className="typewriter">
              <div className="typewriter-top"><span /><span /><span /></div>
              <div className="typewriter-roller"><div className="roller-line" /></div>
              <div className="typewriter-paper-shadow" style={{ height: `${paperHeight}rem` }} />
              <div className="typewriter-paper" style={{ height: `${paperHeight}rem` }}><span className="paper-corner" /><div className="paper-glyph"><GlyphWord text="VALOMBRE" size={19} spacing="gap-0.5" /></div><p className="typed-paper-copy">{paperText}<span className="type-caret" aria-hidden="true" /></p><div className="paper-lines" /></div>
              <div className="typewriter-body"><div className="typewriter-slot" /><div className="typewriter-brand">VALOMBRE<br /><small>NO. 04</small></div><div className="typewriter-keys">{Array.from({ length: 30 }).map((_, i) => <span key={i} />)}</div></div>
            </div>
            <div className="mt-5 flex items-center justify-between text-[9px] font-mono tracking-[0.18em] text-[#756c60]"><span>MECHANISM / READY</span><span>{String(Math.round(progress * 100)).padStart(3, "0")} %</span></div>
          </div>

          <div className="manuscript-panel">
            <div className="manuscript-tabs" role="tablist" aria-label="Room for One More chapters">
              {PAGES.map((item, index) => <button key={item.tab} role="tab" aria-selected={index === pageIndex} onClick={() => changePage(index)} className={index === pageIndex ? "active" : ""}>{item.tab}</button>)}
            </div>
            <div className="manuscript-paper">
              <div className="manuscript-meta"><span>IRA ELOWEN MIREILLE / FIELD NOTES</span><span>PAGE {String(pageIndex + 1).padStart(2, "0")} / 04</span></div>
              <h3>{page.title}</h3>
              <p className="typed-copy">{typedText}<span className="type-caret" aria-hidden="true" /></p>
              <div className="manuscript-footer"><span>{page.note}</span><span>VALOMBRE ARCHIVE</span></div>
            </div>
            <div className="flex items-center justify-between pt-5">
              <button onClick={() => changePage(Math.max(0, pageIndex - 1))} disabled={pageIndex === 0} className="page-control"><ArrowLeft className="h-3.5 w-3.5" /> PREVIOUS</button>
              <span className="flex items-center gap-2 text-[9px] font-mono tracking-[0.18em] text-[#756c60]"><ChevronDown className="h-3.5 w-3.5" /> SCROLL TO TYPE</span>
              <button onClick={() => changePage(Math.min(PAGES.length - 1, pageIndex + 1))} disabled={pageIndex === PAGES.length - 1} className="page-control">NEXT <ArrowRight className="h-3.5 w-3.5" /></button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
