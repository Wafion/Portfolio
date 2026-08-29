import type { Metadata, Viewport } from "next";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#050505",
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
    <html lang="en" className="dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body className="bg-[#050505] text-[#F2F0EA] antialiased">
        {children}
      </body>
    </html>
  );
}
