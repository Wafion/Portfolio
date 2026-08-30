import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "rgb(var(--background) / <alpha-value>)",
        surface: "rgb(var(--surface) / <alpha-value>)",
        "surface-raised": "rgb(var(--surface-raised) / <alpha-value>)",
        "surface-card": "rgb(var(--surface-card) / <alpha-value>)",
        foreground: "rgb(var(--foreground) / <alpha-value>)",
        "muted-foreground": "rgb(var(--muted-foreground) / <alpha-value>)",
        "dim-foreground": "rgb(var(--dim-foreground) / <alpha-value>)",
        accent: {
          violet: "#7C3AED",
          "violet-bright": "#8B5CF6",
          ultramarine: "#2563EB",
          cyan: "#06B6D4",
          amber: "#D97706",
          crimson: "#DC2626",
          "warm-orange": "#EA580C",
          "acid-green": "#16A34A",
          paper: "#C8C0AE",
          steel: "#94A3B8",
        },
      },
      fontFamily: {
        display: ["var(--font-cinzel)", "Playfair Display", "Georgia", "serif"],
        serif: ["var(--font-cormorant)", "Georgia", "serif"],
        sans: ["var(--font-space-grotesk)", "var(--font-inter)", "-apple-system", "sans-serif"],
        mono: ["var(--font-mono)", "JetBrains Mono", "Space Mono", "monospace"],
        heading: ["var(--font-space-grotesk)", "var(--font-inter)", "sans-serif"],
      },
      backgroundImage: {
        "radial-dark": "radial-gradient(ellipse at 50% 30%, rgba(30, 30, 32, 0.5) 0%, rgba(5, 5, 5, 1) 80%)",
        "radial-violet": "radial-gradient(ellipse at 50% 50%, rgba(139, 92, 246, 0.08) 0%, rgba(5, 5, 5, 0) 70%)",
        "radial-warm": "radial-gradient(ellipse at 50% 50%, rgba(212, 167, 83, 0.06) 0%, rgba(5, 5, 5, 0) 70%)",
      },
      animation: {
        "pulse-slow": "pulse 5s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        "float-slow": "float 8s ease-in-out infinite",
        "fade-in": "fadeIn 0.6s ease-out forwards",
        "drift": "drift 12s ease-in-out infinite",
        "spin-slow": "spin 20s linear infinite",
      },
      keyframes: {
        float: {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%": { transform: "translateY(-8px)" },
        },
        fadeIn: {
          "0%": { opacity: "0", transform: "translateY(8px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        drift: {
          "0%, 100%": { transform: "translate(0, 0)" },
          "25%": { transform: "translate(3px, -3px)" },
          "50%": { transform: "translate(-2px, 4px)" },
          "75%": { transform: "translate(4px, 2px)" },
        },
      },
    },
  },
  plugins: [],
};
export default config;
