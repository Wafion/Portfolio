<div align="center">

# ✨ YASH — Interactive Portfolio ✨

### `ENGINEERING × AI × FILM × 3D × WRITING × SYSTEMS`

**A portfolio that refuses to behave like a portfolio.**

<br/>

[![LIVE](https://img.shields.io/badge/🌐_LIVE_SITE-yashs--builds.vercel.app-FF3CAC?style=for-the-badge&labelColor=1a1a2e)](https://yashs-builds.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Wafion-2CD9FF?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a2e)](https://github.com/Wafion)

<br/>

![Next.js](https://img.shields.io/badge/Next.js_14-FF6B6B?style=for-the-badge&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React_18-4ECDC4?style=for-the-badge&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-FFD93D?style=for-the-badge&logo=typescript&logoColor=black)
![Three.js](https://img.shields.io/badge/Three.js-A66CFF?style=for-the-badge&logo=threedotjs&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-6BFF8C?style=for-the-badge&logo=greensock&logoColor=black)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)

</div>

<br/>

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                         Y A S H                                      ║
║                                                                      ║
║   ENGINEERING   SOFTWARE   AI   FILM   3D   WRITING   SYSTEMS        ║
║                                                                      ║
║   STATUS       ONLINE                                                ║
║   MODE         EXPERIMENTAL                                          ║
║   MEDIUM       WHATEVER FITS THE IDEA                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

<br/>

## 🧬 What Is This?

This isn't another `About` → `Skills` → `Projects` → `Contact` template.

It's an **interactive archive** of everything I build, explore, render, write, and obsess over — engineering, AI, film, 3D, and systems, collided into one experience.

```
         ┌──────────────┐
         │ MECHATRONICS │
         └──────┬───────┘
                │
                ▼
   ┌──────────────────────┐
   │       SYSTEMS         │
   └──────────┬───────────┘
              / \
             /   \
            ▼     ▼
      ┌───────┐ ┌───────┐
      │  AI   │ │ CODE  │
      └───┬───┘ └───┬───┘
          │         │
          └────┬────┘
               ▼
       ┌──────────────┐
       │ EXPERIMENTS   │
       └──────┬───────┘
              │
  ┌───────────┼───────────┐
  ▼           ▼           ▼
🎬 FILM      🧊 3D      📖 WRITING
```

> The interesting part isn't each discipline individually — it's what happens **when they collide**.

<br/>

## 🌈 Features

<table>
<tr>
<td width="50%" valign="top">

### 🎨 Experience
- 🧊 Interactive 3D scenes (WebGL)
- 🖱️ Custom, context-aware cursor
- 🎞️ Cinematic scroll-driven motion
- 🌫️ Film grain & atmospheric layers
- 🔊 Procedural / ambient audio
- ♿ Reduced-motion & non-3D fallbacks

</td>
<td width="50%" valign="top">

### 🧠 Content Systems
- 📚 Interactive **PAGE.OS** archive
- ✍️ Scroll-controlled writing/manuscript engine
- 🔐 Experimental glyph / cipher lab
- 🧬 Generative creative-coding sketches
- 🗺️ Spatial, exploration-driven navigation
- 📱 Dedicated mobile experience shell

</td>
</tr>
</table>

| System | Purpose |
|---|---|
| 🧊 **3D Engine** | Interactive WebGL environments (`react-three-fiber`, `drei`) |
| 🎞️ **Motion Engine** | Scroll choreography & transitions (`GSAP`, `Framer Motion`, `Lenis`) |
| 🖱️ **Cursor System** | Context-aware interaction |
| 🔊 **Sound Engine** | Ambient & interaction audio |
| 📚 **PAGE.OS Archive** | Interactive project discovery |
| ✍️ **Writing Engine** | Scroll-controlled manuscript experience |
| 🔐 **Cipher Lab** | Experimental visual language |
| 🧬 **Creative Coding** | Generative visual experiments |
| 📱 **Mobile Shell** | Dedicated mobile composition |
| ♿ **Accessibility** | Reduced-motion & fallback experiences |

<br/>

## ⚙️ How It Works

The homepage is a collection of independent interactive systems assembled into one experience, built on **Next.js 14** with the App Router.

```
                 ┌─────────────┐
                 │   NEXT.JS   │
                 │     APP     │
                 └──────┬──────┘
                        │
     ┌──────────────────┼──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌──────────┐       ┌──────────┐      ┌──────────┐
│ THREE.JS │       │   GSAP   │      │  MOTION  │
│  WEBGL   │       │  SCROLL  │      │    UI    │
└────┬─────┘       └────┬─────┘      └────┬─────┘
     │                  │                  │
     └──────────────────┼──────────────────┘
                         ▼
              ┌──────────────────┐
              │    EXPERIENCE     │
              └────────┬─────────┘
                        │
     ┌──────────────────┼──────────────────┐
     ▼                  ▼                  ▼
┌──────────┐      ┌──────────┐      ┌──────────┐
│  AUDIO   │      │ ARCHIVE  │      │ WRITING  │
└──────────┘      └──────────┘      └──────────┘
```

Each project on the site gets its **own visual language** instead of a generic card:

```
PROJECT
   │
   ├── IDEA
   ├── CONTEXT
   ├── PROCESS
   ├── TECHNOLOGY
   ├── FAILURE
   ├── DISCOVERY
   └── RESULT
```

- 3D scenes render through `react-three-fiber` canvases (`ArchiveCoreCanvas`, `IntersectionHeroCanvas`, `MonolithHeroCanvas`, `UnfinishedArtifactCanvas`)
- `Lenis` drives smooth scrolling, which `GSAP` hooks into for scroll-triggered choreography
- `Framer Motion` handles UI-level transitions and micro-interactions
- A dedicated `MobilePortfolioShell` swaps in on small viewports instead of degrading the desktop layout
- `prefers-reduced-motion` and non-3D fallbacks are respected throughout

<br/>

## 🚀 Getting Started

### Prerequisites
- **Node.js** 18+
- **npm** (or your package manager of choice)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Wafion/Portfolio.git
cd Portfolio

# 2. Install dependencies
npm install

# 3. Run the development server
npm run dev
```

Open [**http://localhost:3000**](http://localhost:3000) to view it locally.

### Available Scripts

| Command | Description |
|---|---|
| `npm run dev` | Starts the local development server |
| `npm run build` | Builds the production-optimized app |
| `npm run start` | Serves the production build |
| `npm run lint` | Runs ESLint checks |

### Project Structure

```
src/
│
├── app/                       # Next.js App Router entry
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
│
├── components/
│   ├── 3d/                    # WebGL / react-three-fiber canvases
│   ├── animations/             # Custom cursor, film grain
│   ├── audio/                  # Sound engine
│   ├── navigation/              # Exhibition & system navigation
│   ├── mobile/                  # Mobile-specific shell
│   ├── sections/                # All homepage sections
│   └── ui/                      # Shared UI primitives (e.g. GlyphSymbol)
│
├── hooks/                       # Custom hooks (e.g. useIsMobile)
│
└── lib/
    ├── data/                    # Static content: projects, cipher, capabilities
    └── utils.ts
```

<br/>

## 🧰 Tech Stack

<div align="center">

**Core**
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

**3D & Motion**
![Three.js](https://img.shields.io/badge/Three.js-black?style=flat-square&logo=threedotjs)
![React Three Fiber](https://img.shields.io/badge/React_Three_Fiber-20232A?style=flat-square&logo=react)
![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=flat-square&logo=greensock&logoColor=black)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white)

**Tooling**
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white)

</div>

<br/>

## 🧪 Design Principles

| # | Principle | Meaning |
|---|---|---|
| 01 | **Make it mean something** | An animation should communicate something. A 3D object should have a reason to exist. |
| 02 | **Different work, different language** | A neural model shouldn't look like a horror manuscript. A film shouldn't look like a dashboard. |
| 03 | **Interaction over decoration** | If interaction can explain an idea better than a paragraph, use interaction. If not — write the paragraph, make the film, or open Blender. |

<br/>

## ♿ Accessibility

Immersion shouldn't require sacrificing usability:

- `prefers-reduced-motion` support
- Full keyboard interaction
- Touch-optimized interaction
- Dedicated mobile layouts
- Non-3D fallbacks
- Accessible interactive controls

<br/>

## 🧭 Current State

```
╭────────────────────────────────────────────╮
│                                             │
│  PAGE.OS             ● BUILDING            │
│  ANE                  ● EXPLORING          │
│  RESIDUAL             ● ACTIVE             │
│  THE FIFTH EXIT       ● DEVELOPING         │
│  A ROOM FOR ONE MORE  ● WRITING            │
│  3D                   ● EXPERIMENTING      │
│  CIPHER               ● EXPERIMENTAL       │
│                                             │
╰────────────────────────────────────────────╯
```

<br/>

## 🔗 Connect

<div align="center">

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-yashs--builds.vercel.app-FF3CAC?style=for-the-badge&labelColor=1a1a2e)](https://yashs-builds.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Wafion-2CD9FF?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a2e)](https://github.com/Wafion)

</div>

<br/>

<div align="center">

### `STILL BUILDING.`  ·  `STILL EXPLORING.`  ·  `STILL FIGURING IT OUT.`

*Built with TypeScript, React, Three.js, GSAP, caffeine,
and an unreasonable number of ideas.*

</div>
