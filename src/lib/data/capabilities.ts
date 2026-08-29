/**
 * Things I Build & Things I Make
 * First-person overview of technical capabilities, toolchains, and craft.
 */

export interface DomainCapability {
  id: string;
  title: string;
  category: "ENGINEERING" | "SOFTWARE" | "AI" | "FILM & CINEMA" | "3D & VISUAL" | "WRITING & DESIGN";
  summary: string;
  skills: {
    name: string;
    note: string;
  }[];
  accentColor: string;
}

export const TECHNICAL_DOMAINS: DomainCapability[] = [
  {
    id: "engineering",
    title: "ENGINEERING",
    category: "ENGINEERING",
    summary: "I study Mechatronics Engineering at MPSTME, Mumbai — combining mechanical dynamics, circuit design, and microcontroller software.",
    skills: [
      { name: "Mechatronics Core", note: "Kinematics, actuators, motor drivers, sensor acquisition" },
      { name: "Robotics & Automation", note: "Feedback control loops, inverse kinematics, serial telemetry" },
      { name: "Systems Thinking", note: "Modeling holistic mechanical, electronic, and software interactions" },
      { name: "Electronics & Embedded", note: "Circuit schematics, microcontrollers, signal conditioning" },
    ],
    accentColor: "#fbbf24",
  },
  {
    id: "software",
    title: "SOFTWARE",
    category: "SOFTWARE",
    summary: "I write clean, type-safe code for full-stack web applications, distributed state, and creative interfaces.",
    skills: [
      { name: "TypeScript & JavaScript", note: "Asynchronous architectures, strict typing, reactive states" },
      { name: "Next.js & React", note: "App Router, server components, client-side streaming, performance" },
      { name: "Python", note: "ML pipelines, FastAPI microservices, automated data processing" },
      { name: "Firebase & Cloud", note: "Cloud Firestore, real-time sync, auth, edge caching" },
      { name: "Git & Version Control", note: "Branching strategies, CI workflows, modular architectures" },
    ],
    accentColor: "#38bdf8",
  },
  {
    id: "ai",
    title: "ARTIFICIAL INTELLIGENCE",
    category: "AI",
    summary: "I explore local language models, transformer classification, narrative audio understanding, and agentic workflows.",
    skills: [
      { name: "PyTorch & Transformers", note: "Fine-tuning multi-task models (MiniLM), embeddings, sequence classification" },
      { name: "Local AI & Ollama", note: "Edge quantization, private local inference, prompt engineering pipelines" },
      { name: "Vector Search & Retrieval", note: "Semantic search, cultural knowledge graphs, vector similarity" },
      { name: "NLP & Narrative Understanding", note: "Pacing analysis, dialogue parsing, emotional scene classification" },
    ],
    accentColor: "#c084fc",
  },
];

export const CREATIVE_DOMAINS: DomainCapability[] = [
  {
    id: "film-cinema",
    title: "FILM & CINEMATOGRAPHY",
    category: "FILM & CINEMA",
    summary: "Under the Residual identity, I direct short films and explore visual restraint, darkroom tones, and deliberate pacing.",
    skills: [
      { name: "Directing & Visual Previs", note: "Scene blocking, script development, Blender 3D camera previs" },
      { name: "Cinematography & Lighting", note: "Low-key lighting, deep shadow falloff, anamorphic 2.39:1 framing" },
      { name: "DaVinci Resolve Studio", note: "ACES color management, film emulation curves, editorial pacing" },
      { name: "Spatial Sound Design", note: "Binaural audio textures, ambient drone synthesis, environmental Foley" },
    ],
    accentColor: "#94a3b8",
  },
  {
    id: "3d-visual",
    title: "3D ART & BLENDER",
    category: "3D & VISUAL",
    summary: "I sculpt monolithic forms, procedural geometry shaders, and volumetric lighting studies in Blender.",
    skills: [
      { name: "Blender 4.x & Cycles", note: "Raytraced volumetric scattering, realistic caustics, architectural renders" },
      { name: "Procedural Geometry Nodes", note: "Algorithmic deformation, micro-displacement, procedural concrete" },
      { name: "Creative Coding & WebGL", note: "Three.js scenes, Canvas 2D particle physics, Lissajous curves" },
      { name: "Web Audio API", note: "Real-time procedural synthesizer drones and acoustic resonance" },
    ],
    accentColor: "#60a5fa",
  },
  {
    id: "writing-design",
    title: "WRITING & TYPOGRAPHY",
    category: "WRITING & DESIGN",
    summary: "I author psychological horror stories and design experimental typography and custom glyph writing systems.",
    skills: [
      { name: "Psychological Horror", note: "Unreliable narrators, architectural dread, character psychology" },
      { name: "Worldbuilding", note: "Archival field manuscripts, non-Euclidean spaces, atmospheric lore" },
      { name: "Experimental Ciphers", note: "Custom 26-glyph geometric alphabet constructed on 24x24 grid" },
      { name: "Editorial Typography", note: "Spatial kinetic type treatments, editorial serifs, technical monospace" },
    ],
    accentColor: "#facc15",
  },
];
