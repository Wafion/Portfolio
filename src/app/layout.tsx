import type { Metadata, Viewport } from "next";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: [{ media: "(prefers-color-scheme: dark)", color: "#050505" }, { color: "#f4f1e8" }],
};

export const metadata: Metadata = {
  title: "YASH — Digital Exhibition",
  description:
    "I build things across engineering, software, film, and art. A digital exhibition of multidisciplinary work by Yash — mechatronics, AI, cinema, writing, 3D, cipher systems, and creative coding.",
  keywords: [
    "Yash",
    "Portfolio",
    "Mechatronics Engineering",
    "PAGE.OS",
    "Audio Narrative Engine",
    "Residual",
    "The Fifth Exit",
    "Creative Coding",
    "Blender",
    "AI",
    "Filmmaking",
    "Cipher",
  ],
  authors: [{ name: "Yash" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        {/* Flash prevention: apply saved theme class before first paint */}
        <script
          dangerouslySetInnerHTML={{
            __html: `
(function(){try{var t=localStorage.getItem('yash-theme');var d=window.matchMedia('(prefers-color-scheme:dark)').matches;var isLight=(t==='light')||(!t&&d===false);document.documentElement.classList.add(isLight?'light':'dark');}catch(e){document.documentElement.classList.add('dark');}})();
`,
          }}
        />
      </head>
      <body className="antialiased">
        {children}
        <Analytics />
      </body>
    </html>
  );
}
