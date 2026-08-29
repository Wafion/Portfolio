import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#050505",
        surface: "#0A0A0A",
        "surface-raised": "#111111",
        "surface-card": "#18181A",
        foreground: "#F2F0EA",
        "muted-foreground": "#B8B6AF",
        "dim-foreground": "#7A7874",
        accent: {
          violet: "#8B5CF6",
          "violet-bright": "#A78BFA",
          ultramarine: "#4A6FA5",
          cyan: "#5BB8D4",
          amber: "#D4A753",
          crimson: "#C4565A",
          "warm-orange": "#E07A3A",
          "acid-green": "#4ADE80",
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
