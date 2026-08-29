/**
 * Yash's Work & Artifact Exhibition
 * First-person case studies and project records exploring thought process,
 * motivations, engineering, and retrospectives.
 */

export interface ExhibitionProject {
  id: string;
  slug: string;
  number: string;
  title: string;
  subtitle: string;
  domain: "Software & AI" | "Audio & ML" | "Cinema & Direction" | "Psychological Horror" | "Writing & Literature" | "3D & Art" | "Typography & Cipher" | "Creative Coding";
  material: "GLASS" | "WAVEFORM" | "STONE" | "CORRIDOR" | "PAPER" | "GEOMETRY" | "GLYPH" | "PARTICLES";
  year: string;
  status: "BUILDING" | "ACTIVE" | "IN DEVELOPMENT" | "EXPERIMENTAL";
  tagline: string;
  summary: string;
  technologies: string[];
  accentColor: string;
  caseStudy: {
    whatIWantedToMake: string;
    why: string;
    how: string;
    whatWorked: string;
    whatDidnt: string;
    whatILearned: string;
    quote?: string;
    specifications: { label: string; value: string }[];
  };
}

export const EXHIBITION_PROJECTS: ExhibitionProject[] = [
  {
    id: "page-os",
    slug: "page-os",
    number: "01",
    title: "PAGE.OS",
    subtitle: "A reading environment where literature meets the terminal",
    domain: "Software & AI",
    material: "GLASS",
    year: "2024–PRESENT",
    status: "BUILDING",
    tagline: "I wanted to build a reading environment that treats books as an interconnected landscape rather than flat digital rectangles.",
    summary:
      "A personal knowledge discovery and reading environment that brings classical literature, non-linear reading trails, and AI search into a distraction-free space.",
    technologies: ["Next.js", "TypeScript", "Tailwind CSS", "Firebase", "Vector Search / AI Retrieval", "EPUB/PDF Engine", "Project Gutenberg API"],
    accentColor: "#38bdf8",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to build a reading environment that treats books as an interconnected landscape rather than flat digital rectangles. Most e-readers mimic physical paper turn-by-turn, but software can do something physical paper cannot: trace thematic connections across thousands of texts in real time.",
      why:
        "When I read philosophy or classical literature, my thoughts don't move in straight vertical lines. One paragraph in Dostoevsky connects to an idea in Marcus Aurelius or a concept in cybernetics. I needed an environment that supported non-linear exploration, dynamic note trails, and immersive ambient focus.",
      how:
        "I built PAGE.OS around three distinct modes: Classic Mode for pure typography, Lounge Mode for atmospheric focus paired with ambient soundscapes, and Infinity Mode for traversing associative semantic trails. I integrated Project Gutenberg's catalog and built client-side stream parsers for high-speed EPUB rendering.",
      whatWorked:
        "The minimal typography and distraction-free spatial navigation make reading long texts genuinely enjoyable. The non-linear trail system turns casual reading into a personal knowledge archive.",
      whatDidnt:
        "Initial attempts at complex 3D bookshelves felt gimmicky and slowed down text rendering. I discarded the skeuomorphic 3D book metaphors in favor of pure typography and clean spatial indexing.",
      whatILearned:
        "Software designed for the mind must respect cognitive focus above all else. Adding features is easy; stripping away interface clutter until only the text and your thoughts remain is the actual engineering challenge.",
      quote: "Where literature ceases to be a flat page and becomes a searchable, navigable architecture.",
      specifications: [
        { label: "Core Paradigms", value: "Classic Mode, Lounge Mode, Infinity Mode" },
        { label: "Graph Engine", value: "Non-linear Reading Trails & Semantic Links" },
        { label: "Formats Supported", value: "EPUB, PDF, Raw Text Archives" },
        { label: "Storage Architecture", value: "Firebase Cloud Sync + IndexedDB Local" },
      ],
    },
  },
  {
    id: "ane",
    slug: "ane",
    number: "02",
    title: "ANE — AUDIO NARRATIVE ENGINE",
    subtitle: "Context-aware acoustic environments for long-form literature",
    domain: "Audio & ML",
    material: "WAVEFORM",
    year: "2024",
    status: "IN DEVELOPMENT",
    tagline: "I wanted to create a 'Netflix for ears' that listens to the text as attentively as the human hearing it.",
    summary:
      "A machine learning pipeline that parses scene context, emotional valence, and dialogue in literature to generate adaptive real-time soundscapes.",
    technologies: ["PyTorch", "MiniLM-L6-v2", "FastAPI", "Pydantic", "Ollama", "Hugging Face", "Python", "Web Audio API"],
    accentColor: "#fbbf24",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to build an intelligent audiobook engine that understands what is happening inside a story and adapts the acoustic atmosphere accordingly.",
      why:
        "Conventional audiobooks are static voice tracks. If a scene moves from a sunlit field into a claustrophobic subterranean tunnel, the listener hears the exact same acoustic background. I wanted the audio stage to breathe with the narrative's tension, location, and dialogue density.",
      how:
        "I fine-tuned a MiniLM-L6-v2 transformer model as a multi-task narrative classifier trained on 67,556 annotated passages across 54 complete books. The model predicts setting categories, dialogue tension, and pacing in sub-24ms inference chunks, orchestrating procedural ambient sound layers via a FastAPI service.",
      whatWorked:
        "Fine-tuning a lightweight distilled model achieved high classification accuracy for literary tones without requiring massive cloud GPUs.",
      whatDidnt:
        "Full generative sound synthesis in real time introduced perceptible latency during rapid scene shifts. I solved this by pre-caching modular procedural Foley stems and crossfading based on predictive sentence buffers.",
      whatILearned:
        "AI in creative tools works best when it acts as an intelligent orchestrator rather than trying to brute-force generate every raw sound wave from scratch.",
      quote: "Audio that understands the story with the same nuance as the listener.",
      specifications: [
        { label: "Backbone Architecture", value: "Fine-tuned MiniLM-L6-v2 Multi-task" },
        { label: "Training Corpus", value: "67,556 Literary Passages (54 Books)" },
        { label: "Inference Latency", value: "< 24ms per scene chunk" },
        { label: "Deployment", value: "FastAPI + Local Ollama Quantized Runner" },
      ],
    },
  },
  {
    id: "residual",
    slug: "residual",
    number: "03",
    title: "RESIDUAL",
    subtitle: "My creative identity for filmmaking and visual storytelling",
    domain: "Cinema & Direction",
    material: "STONE",
    year: "2023–PRESENT",
    status: "ACTIVE",
    tagline: "A filmmaking identity built on visual restraint, deep contrast, and atmospheric silence.",
    summary:
      "The production and visual storytelling identity under which I direct short films, explore low-key cinematography, and craft tactile sound design.",
    technologies: ["DaVinci Resolve Studio", "Blackmagic RAW", "Anamorphic Framing", "Blender Previs", "Spatial Sound Design"],
    accentColor: "#94a3b8",
    caseStudy: {
      whatIWantedToMake:
        "I wanted a creative filmmaking identity that avoided all the conventional clichés of modern videography: no flashy camera gear icons, no rapid hyper-edits, no saturated neon.",
      why:
        "I believe cinema is at its most powerful when it practices visual restraint. The weight of a stone, the texture of low-key shadows, and the deliberate pacing of a slow camera move allow the viewer's imagination to inhabit the space.",
      how:
        "I built Residual around geological and monolithic symbolism: weathered granite, quiet brutalist architecture, and darkroom tones. I shoot in wide anamorphic aspect ratios (2.39:1) and grade using custom ACES color curves in DaVinci Resolve.",
      whatWorked:
        "Using Blender for spatial previsualization allowed me to plan complex camera movements and lighting setups before ever stepping onto a physical set.",
      whatDidnt:
        "Early experiments leaned too far into pure abstraction. I learned that visual atmosphere needs an emotional anchor or narrative question to hold the audience.",
      whatILearned:
        "Filmmaking taught me how to direct the viewer's attention through light and rhythm — an instinct that directly shapes how I design software interfaces and 3D spaces.",
      quote: "Cinema is not about showing everything; it is about crafting the shadow where the imagination lives.",
      specifications: [
        { label: "Visual Motif", value: "Monolithic Stone & Brutalist Relics" },
        { label: "Color Science", value: "Low-Key Monochrome & Film Halation" },
        { label: "Aspect Ratios", value: "2.39:1 Anamorphic & 1.33:1 Archival" },
        { label: "Previs Workflow", value: "Blender 3D Set Extensions & ACES" },
      ],
    },
  },
  {
    id: "the-fifth-exit",
    slug: "the-fifth-exit",
    number: "04",
    title: "THE FIFTH EXIT",
    subtitle: "An experimental short film concept exploring liminal horror",
    domain: "Psychological Horror",
    material: "CORRIDOR",
    year: "2024",
    status: "IN DEVELOPMENT",
    tagline: "A narrative trapped within non-Euclidean brutalist corridors and five rooms representing internal limitations.",
    summary:
      "A short film concept exploring dissociation, impossible architecture, and distorted voices as a protagonist confronts rooms symbolizing their own limiting beliefs.",
    technologies: ["Screenplay & Treatment", "Blender Previs", "Binaural Sound Design", "Architectural Worldbuilding"],
    accentColor: "#fb7185",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to make a psychological horror film where the threat is not a monster with teeth, but the horrifying realization that the physical space around you is actively reflecting your own psychological isolation.",
      why:
        "Liminal spaces — endless empty hallways, deserted stairwells, identical doors — create a specific existential dread. I wanted to use that aesthetic to explore dissociation and the internal prisons we build out of guilt and doubt.",
      how:
        "The story follows a protagonist trapped in a non-Euclidean building. There are five numbered exits, but each exit opens into a room representing a core limiting belief: The Mirror, The Ledger, The Voice, The Void, and The Exit. I prototyped the architectural spaces in Blender with camera tracking simulations and designed a binaural audio treatment with layered whispered tape loops.",
      whatWorked:
        "The spatial mapping of psychological themes to physical rooms gave the script a clear architectural spine.",
      whatDidnt:
        "Balancing exposition with mystery is difficult in short-form horror. I stripped out unnecessary backstory dialogue so the physical environment carries the narrative weight.",
      whatILearned:
        "Architecture can be as much of a character in a film as the actor. How a room is proportioned changes the emotional temperature of the scene.",
      quote: "You did not enter the building. The building materialized around your silence.",
      specifications: [
        { label: "Narrative Arc", value: "5 Corridors / 5 Limiting Beliefs" },
        { label: "Visual Tone", value: "Sodium-Vapor Lighting & Liminal Brutalism" },
        { label: "Audio Texture", value: "Binaural Echoes & Tape Loop Distortions" },
        { label: "Format", value: "Experimental Narrative Short" },
      ],
    },
  },
  {
    id: "a-room-for-one-more",
    slug: "a-room-for-one-more",
    number: "05",
    title: "A ROOM FOR ONE MORE",
    subtitle: "A psychological horror novel manuscript",
    domain: "Writing & Literature",
    material: "PAPER",
    year: "2023–PRESENT",
    status: "IN DEVELOPMENT",
    tagline: "An archival manuscript tracing the unraveling reality and memory of Ira Elowen Mireille.",
    summary:
      "A long-form psychological horror manuscript examining grief, unreliable perception, and the terrifying architecture of memory.",
    technologies: ["Manuscript & Prose", "Archival Worldbuilding", "Character Psychology", "Typography Layout", "Cipher Inscriptions"],
    accentColor: "#c084fc",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to write a psychological horror novel that reads like an authentic historical manuscript discovered in an abandoned home.",
      why:
        "I've always been drawn to stories where reality isn't quite trustworthy. The feeling when your own memory contradicts the physical evidence in the room is far more terrifying than external shocks.",
      how:
        "The story centers on protagonist Ira Elowen Mireille as she documents subtle physical anomalies in her residence that slowly reveal inconsistencies in who she believed herself to be. I structured the chapters as archival field notes and diary entries, with marginal notes and cipher inscriptions embedded in the text.",
      whatWorked:
        "The epistolary format allows the prose to shift in tone and reliability as Ira's perception fractures.",
      whatDidnt:
        "Pacing a psychological mystery requires careful restraint; early drafts gave away too much too soon. Rewriting the middle chapters to let the atmosphere linger made the tension far more effective.",
      whatILearned:
        "Writing prose is the purest form of worldbuilding. Without actors, code, or render engines, every image and emotion exists solely through the choice and rhythm of words.",
      quote: "If the mirror remembers what stood before it yesterday, who is the stranger looking back today?",
      specifications: [
        { label: "Protagonist", value: "Ira Elowen Mireille" },
        { label: "Structure", value: "Fragmented Archival Manuscript & Notes" },
        { label: "Core Theme", value: "Grief, Unreliable Perception & Memory" },
        { label: "Visual Detail", value: "Embedded Geometric Cipher Annotations" },
      ],
    },
  },
  {
    id: "blender-3d",
    slug: "3d-art",
    number: "06",
    title: "3D ART & PROCEDURAL GEOMETRY",
    subtitle: "Monolithic structures and atmospheric light physics in Blender",
    domain: "3D & Art",
    material: "GEOMETRY",
    year: "2023–PRESENT",
    status: "ACTIVE",
    tagline: "I use Blender as a spatial sketchbook for procedural shaders, brutalist forms, and lighting experiments.",
    summary:
      "A digital exhibition of procedural node graphs, abstract monolithic sculptures, volumetric lighting studies, and Cycles renders.",
    technologies: ["Blender 4.x", "Cycles Render Engine", "Geometry Nodes", "Procedural Shaders", "Volumetric Scattering"],
    accentColor: "#60a5fa",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to create 3D artwork that felt heavy, cold, and physically manufactured — sculptures that look as if they were carved from granite and weathered by centuries.",
      why:
        "Digital 3D often looks too clean, plastic, and artificial. I wanted to explore how procedural math could generate micro-imperfections, realistic surface roughness, and volumetric light scattering.",
      how:
        "I build procedural geometry node graphs in Blender that distort and fracture basic architectural primitives. I design procedural materials using complex noise displacement for weathered concrete and obsidian, illuminated by raytraced volumetric fog.",
      whatWorked:
        "Procedural workflows allow me to iterate rapidly across dozens of variations without manually sculpting every vertex.",
      whatDidnt:
        "Heavy volumetric simulations can easily blow up render times. I learned how to balance ray samples and optimize geometry for both still renders and real-time WebGL export.",
      whatILearned:
        "Light is the most important material in 3D. A simple cube under thoughtful lighting will always be more striking than a million vertices under flat light.",
      quote: "Giving digital vertices the permanence and tactile coldness of carved stone.",
      specifications: [
        { label: "Core Toolchain", value: "Blender Cycles & Procedural Geometry Nodes" },
        { label: "Aesthetic Direction", value: "Brutalist Monoliths & Atmospheric Fog" },
        { label: "Shader Approach", value: "100% Procedural Micro-Displacement" },
      ],
    },
  },
  {
    id: "cipher-system",
    slug: "cipher",
    number: "07",
    title: "EXPERIMENTAL CIPHER & GLYPH SYSTEM",
    subtitle: "A custom 26-character geometric glyph alphabet",
    domain: "Typography & Cipher",
    material: "GLYPH",
    year: "2023–PRESENT",
    status: "ACTIVE",
    tagline: "I designed a geometric glyph writing system that functions as an embedded transmission layer across my work.",
    summary:
      "A proprietary visual language and typographic cipher constructed along a 24×24 orthogonal grid, blending architectural vectors with runes.",
    technologies: ["Custom Vector Typography", "SVG Coordinate Math", "Cryptographic Mapping", "Interactive Web Studio"],
    accentColor: "#facc15",
    caseStudy: {
      whatIWantedToMake:
        "I wanted to invent my own visual alphabet — a writing system that looked ancient yet mathematical, like coordinates carved into the wall of an unknown machine.",
      why:
        "Language is the first interface humanity ever created. Designing a custom alphabet allowed me to explore typography from its absolute geometric foundations.",
      how:
        "I drafted 26 distinct vector glyphs corresponding to the English alphabet. Every character adheres to a strict 24×24 telemetry grid using precise angles, singular nodes, open cantilevers, and closed polygons. I built a live interactive translator in React with acoustic feedback.",
      whatWorked:
        "The glyphs maintain high visual distinctiveness while sharing a consistent architectural weight and geometry.",
      whatDidnt:
        "Some early glyph designs were too complex to read at small sizes. I iteratively reduced stroke counts until each symbol was instantly recognizable even at 14 pixels.",
      whatILearned:
        "Every glyph in an alphabet is a tiny piece of architecture. Proportions, whitespace, and stroke rhythm matter just as much in a letter as they do in a building.",
      quote: "Language is the first machine human beings ever invented.",
      specifications: [
        { label: "Character Set", value: "26 Unique Geometric Glyphs (A–Z)" },
        { label: "Grid Space", value: "24 × 24 Orthogonal Telemetry Grid" },
        { label: "Integration", value: "Embedded throughout 3D Art & Manuscript Footnotes" },
      ],
    },
  },
  {
    id: "creative-coding",
    slug: "creative-coding",
    number: "08",
    title: "CREATIVE CODING & GENERATIVE EXPERIMENTS",
    subtitle: "Mathematical simulations and vector physics on canvas",
    domain: "Creative Coding",
    material: "PARTICLES",
    year: "2024–PRESENT",
    status: "ACTIVE",
    tagline: "A digital sketchbook where mathematical formulas become interactive visual systems.",
    summary:
      "A collection of interactive generative algorithms, vector flow fields, Lissajous frequency curves, and canvas physics experiments.",
    technologies: ["HTML5 Canvas 2D", "Vector Physics", "Perlin / Trigonometric Noise", "Audio Reactive FFT", "React Hooks"],
    accentColor: "#34d399",
    caseStudy: {
      whatIWantedToMake:
        "I wanted a digital playground where I could test ideas in generative math and physics before incorporating them into larger applications.",
      why:
        "Writing code to simulate natural physics — force fields, particle damping, harmonic interference — is one of the most direct ways to understand how mathematical systems behave.",
      how:
        "I built hardware-accelerated canvas experiments using requestAnimationFrame loops, implementing vector flow fields driven by gradient noise, particle springs responding to mouse coordinates, and harmonic Lissajous visualizers.",
      whatWorked:
        "Keeping the code zero-dependency and lightweight delivers a consistent 60 FPS across desktop and mobile browsers.",
      whatDidnt:
        "Overloading particle counts on mobile devices drained batteries. I added adaptive density scaling based on device pixel ratio.",
      whatILearned:
        "Simple mathematical formulas, when layered with velocity and damping, produce emergent organic beauty that looks remarkably alive.",
      quote: "Code is not merely an instruction set; it is a brush with infinite precision.",
      specifications: [
        { label: "Performance", value: "60 FPS Hardware-Accelerated 2D Canvas" },
        { label: "Algorithms", value: "Vector Flow Fields, Lissajous Harmonics, Cipher Streams" },
        { label: "Interactivity", value: "Real-time Force Disturbances & Velocity Tuning" },
      ],
    },
  },
];
