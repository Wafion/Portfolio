"use client";

import { ArrowUpRight, BookOpen, ChevronRight, Github, Linkedin, Mail } from "lucide-react";
import { CipherLab } from "@/components/sections/CipherLabSection";
import { DualChannelSection, ChannelId } from "@/components/sections/DualChannelSection";
import { RoomForOneMoreSection } from "@/components/sections/RoomForOneMoreSection";
import { ExhibitionProject, EXHIBITION_PROJECTS } from "@/lib/data/projects";

function MobileProjectCard({ project, onOpen }: { project: ExhibitionProject; onOpen: (project: ExhibitionProject) => void }) {
  return (
    <button className="mobile-project-card" onClick={() => onOpen(project)}>
      <div className="mobile-project-card-top"><span>{project.number} / {project.domain}</span><ArrowUpRight size={15} /></div>
      <h3>{project.title}</h3>
      <p>{project.tagline}</p>
      <div className="mobile-project-card-bottom"><span>{project.year}</span><span>{project.status}</span></div>
    </button>
  );
}

function MobileArchiveCard({ project, onOpen }: { project: ExhibitionProject; onOpen: (project: ExhibitionProject) => void }) {
  return (
    <section id="archive" className="mobile-archive-card-section">
      <div className="mobile-section-kicker">PAGE.OS / ARCHIVE ENTRY</div>
      <div className="mobile-archive-card">
        <div className="mobile-archive-card-mark"><span>01</span><strong>PAGE<span>.</span>OS</strong><small>OPEN KNOWLEDGE / READING SYSTEM</small></div>
        <div className="mobile-archive-card-copy">
          <p className="mobile-section-kicker">A QUIET WAY INTO THE ARCHIVE</p>
          <h2>Discover the system behind the shelves.</h2>
          <p>{project.summary}</p>
          <div className="mobile-archive-concepts"><span>SEARCH</span><span>LIBRARY</span><span>READER</span><span>INFINITE</span></div>
          <div className="mobile-archive-actions"><button onClick={() => onOpen(project)}>OPEN CASE STUDY <ChevronRight size={15} /></button><a href="https://pageos.vercel.app" target="_blank" rel="noreferrer">VISIT PAGE.OS <ArrowUpRight size={15} /></a></div>
        </div>
      </div>
    </section>
  );
}

export function MobilePortfolioShell({ activeChannel, onChannelChange, onOpenProject }: { activeChannel: ChannelId; onChannelChange: (channel: ChannelId) => void; onOpenProject: (project: ExhibitionProject) => void }) {
  const pageOS = EXHIBITION_PROJECTS.find((project) => project.id === "page-os");

  return (
    <div className="mobile-portfolio-shell">
      <section id="hero" className="mobile-hero-section">
        <div className="mobile-hero-eyebrow"><span className="status-dot" /> MUMBAI / MECHATRONICS & CREATIVE TECH <span>2024 - PRESENT</span></div>
        <p className="mobile-hero-index">01 / PERSONAL EXHIBITION</p>
        <h1>HEY, THIS<br /><em>IS YASH.</em></h1>
        <p className="mobile-hero-intro">I build things across engineering, software, film, and art. Some become projects. Some become experiments. Some become stories.</p>
        <div className="mobile-hero-actions"><a href="#work">ENTER THE WORK <ArrowUpRight size={15} /></a><a href="#writing">OPEN MANUSCRIPTS <ArrowUpRight size={15} /></a></div>
        <div className="mobile-hero-seal"><span>Y</span><small>BUILD / MAKE / EXPERIMENT</small></div>
      </section>

      <section id="work" className="mobile-work-section">
        <div className="mobile-section-heading"><span className="mobile-section-kicker">SELECTED WORK</span><h2>Different tools.<br /><em>Same instinct.</em></h2><p>Projects, systems, and stories built where disciplines overlap.</p></div>
        <div className="mobile-project-list">{EXHIBITION_PROJECTS.slice(0, 6).map((project) => <MobileProjectCard key={project.id} project={project} onOpen={onOpenProject} />)}</div>
      </section>

      <DualChannelSection onOpenProject={onOpenProject} onChannelChange={onChannelChange} />
      {pageOS && <MobileArchiveCard project={pageOS} onOpen={onOpenProject} />}

      <RoomForOneMoreSection />

      <section id="intersections" className="mobile-intersections-section">
        <div className="mobile-section-heading"><span className="mobile-section-kicker">INTEREST FIELD</span><h2>Where things<br /><em>collide.</em></h2></div>
        <div className="mobile-intersection-list"><span>LITERATURE <b>+</b> SOFTWARE <strong>PAGE.OS</strong></span><span>AI <b>+</b> AUDIO <strong>ANE</strong></span><span>FILM <b>+</b> DESIGN <strong>RESIDUAL</strong></span><span>CODE <b>+</b> LANGUAGE <strong>CIPHER</strong></span></div>
      </section>

      <section id="experiments" className="mobile-lab-section">
        <div className="mobile-section-heading"><span className="mobile-section-kicker">EXPERIMENTS / CIPHER INSTALLATION</span><h2>Language,<br /><em>made physical.</em></h2><p>The glyph system is a live instrument. Change the key and watch the language move.</p></div>
        <CipherLab />
      </section>

      <footer id="contact" className="mobile-contact-section">
        <span className="mobile-section-kicker">CONTACT / 07</span><h2>Still<br /><em>building.</em></h2><p>If you want to talk about reading systems, AI, horror, interfaces, 3D, filmmaking, or strange combinations of all of them, reach out.</p>
        <div className="mobile-contact-links"><a href="mailto:contact@yash.dev"><Mail size={16} /> contact@yash.dev</a><a href="https://github.com/Wafion" target="_blank" rel="noreferrer"><Github size={16} /> GITHUB</a><a href="https://www.linkedin.com/in/yash-sawant-1776a7399/" target="_blank" rel="noreferrer"><Linkedin size={16} /> LINKEDIN</a></div>
      </footer>
    </div>
  );
}
