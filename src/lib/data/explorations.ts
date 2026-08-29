/**
 * Spatial Typographic Landscape: Things I Explore
 * Disciplines that cross-pollinate Yash's work across technology, engineering,
 * filmmaking, writing, and philosophy.
 */

export interface ExplorationDiscipline {
  id: string;
  name: string;
  category: "ENGINEERING" | "SOFTWARE & AI" | "CINEMA & ART" | "WRITING & STORY" | "PHILOSOPHY & SYSTEMS";
  depth: "FOREGROUND" | "MIDGROUND" | "BACKGROUND";
  scale: string; // Tailwind text scale class
  description: string;
  accentColor: string;
  coordinates: { x: number; y: number }; // Relative percentage position on canvas
}

export const EXPLORATIONS: ExplorationDiscipline[] = [
  // Major Foreground Pillars
  {
    id: "mechatronics",
    name: "MECHATRONICS",
    category: "ENGINEERING",
    depth: "FOREGROUND",
    scale: "text-3xl md:text-5xl",
    description: "My undergraduate core at MPSTME: synthesizing physical mechanics, electronics, and software into moving systems.",
    accentColor: "#fbbf24",
    coordinates: { x: 12, y: 18 },
  },
  {
    id: "ai-systems",
    name: "ARTIFICIAL INTELLIGENCE",
    category: "SOFTWARE & AI",
    depth: "FOREGROUND",
    scale: "text-3xl md:text-5xl",
    description: "I build with transformers, local quantized LLMs, narrative classifiers, and multimodal reasoning.",
    accentColor: "#38bdf8",
    coordinates: { x: 52, y: 28 },
  },
  {
    id: "filmmaking",
    name: "FILMMAKING",
    category: "CINEMA & ART",
    depth: "FOREGROUND",
    scale: "text-3xl md:text-5xl",
    description: "Visual restraint, low-key lighting, anamorphic framing, and tactile sound design under the Residual identity.",
    accentColor: "#94a3b8",
    coordinates: { x: 22, y: 55 },
  },
  {
    id: "psychological-horror",
    name: "PSYCHOLOGICAL HORROR",
    category: "WRITING & STORY",
    depth: "FOREGROUND",
    scale: "text-2xl md:text-4xl",
    description: "Exploring grief, dissociation, unreliable memory, and impossible non-Euclidean architectures.",
    accentColor: "#fb7185",
    coordinates: { x: 58, y: 68 },
  },

  // Midground Connectors
  {
    id: "3d-blender",
    name: "3D & BLENDER",
    category: "CINEMA & ART",
    depth: "MIDGROUND",
    scale: "text-2xl md:text-3xl",
    description: "Procedural geometry nodes, cycles rendering, monoliths, and atmospheric fog physics.",
    accentColor: "#60a5fa",
    coordinates: { x: 74, y: 15 },
  },
  {
    id: "robotics",
    name: "ROBOTICS & KINEMATICS",
    category: "ENGINEERING",
    depth: "MIDGROUND",
    scale: "text-xl md:text-3xl",
    description: "Kinematic chains, actuator controllers, telemetry feedback, and physical computing.",
    accentColor: "#f59e0b",
    coordinates: { x: 34, y: 38 },
  },
  {
    id: "writing-manuscripts",
    name: "WRITING",
    category: "WRITING & STORY",
    depth: "MIDGROUND",
    scale: "text-2xl md:text-3xl",
    description: "I've always been interested in stories where reality isn't quite trustworthy.",
    accentColor: "#c084fc",
    coordinates: { x: 76, y: 48 },
  },
  {
    id: "cryptography",
    name: "CRYPTOGRAPHY & CIPHERS",
    category: "PHILOSOPHY & SYSTEMS",
    depth: "MIDGROUND",
    scale: "text-xl md:text-2xl",
    description: "Inventing geometric glyph alphabets, coordinate typography, and visual language systems.",
    accentColor: "#facc15",
    coordinates: { x: 10, y: 78 },
  },
  {
    id: "creative-coding",
    name: "CREATIVE CODING",
    category: "SOFTWARE & AI",
    depth: "MIDGROUND",
    scale: "text-xl md:text-2xl",
    description: "WebGL shaders, particle flow fields, Lissajous curves, and procedural math on canvas.",
    accentColor: "#34d399",
    coordinates: { x: 42, y: 82 },
  },

  // Background Nuances & Systems
  {
    id: "systems-thinking",
    name: "SYSTEMS THINKING",
    category: "PHILOSOPHY & SYSTEMS",
    depth: "BACKGROUND",
    scale: "text-base md:text-xl",
    description: "Viewing machines, stories, software, and human behavior as interconnected feedback loops.",
    accentColor: "#cbd5e1",
    coordinates: { x: 8, y: 42 },
  },
  {
    id: "local-ai",
    name: "LOCAL AI & OLLAMA",
    category: "SOFTWARE & AI",
    depth: "BACKGROUND",
    scale: "text-base md:text-xl",
    description: "Quantized edge models, small language models, and private local inference pipelines.",
    accentColor: "#7dd3fc",
    coordinates: { x: 40, y: 10 },
  },
  {
    id: "audio-tech",
    name: "AUDIO TECHNOLOGY",
    category: "SOFTWARE & AI",
    depth: "BACKGROUND",
    scale: "text-base md:text-xl",
    description: "Binaural spatial sound, procedural synthesis, granular delay, and the Audio Narrative Engine.",
    accentColor: "#fcd34d",
    coordinates: { x: 72, y: 85 },
  },
  {
    id: "liminal-spaces",
    name: "LIMINAL SPACES",
    category: "WRITING & STORY",
    depth: "BACKGROUND",
    scale: "text-base md:text-xl",
    description: "Deserted brutalist corridors, non-Euclidean geometry, and atmospheric quietude.",
    accentColor: "#fda4af",
    coordinates: { x: 82, y: 35 },
  },
  {
    id: "philosophy-physics",
    name: "PHYSICS & PHILOSOPHY",
    category: "PHILOSOPHY & SYSTEMS",
    depth: "BACKGROUND",
    scale: "text-sm md:text-lg",
    description: "Entropy, cybernetics, mechanics, and the nature of perception.",
    accentColor: "#e2e8f0",
    coordinates: { x: 30, y: 92 },
  },
];
