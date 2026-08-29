/**
 * YASH.OS Custom Cipher & Glyph Writing System
 * Geometric glyphs composed of precise vector coordinates, runes, and cryptography schematics.
 */

export interface GlyphDefinition {
  char: string;
  name: string;
  category: "vowel" | "consonant" | "numeral" | "operator";
  description: string;
  path: string; // SVG path data (viewBox 0 0 24 24)
}

export const CIPHER_DICTIONARY: Record<string, GlyphDefinition> = {
  A: {
    char: "A",
    name: "Apex Gate",
    category: "vowel",
    description: "Triangular convergence with central horizontal datum and nadir point.",
    path: "M 12 3 L 20 21 L 4 21 Z M 7 15 L 17 15 M 12 8 L 12 12",
  },
  B: {
    char: "B",
    name: "Dual Chamber",
    category: "consonant",
    description: "Vertical spine anchoring two mirrored hexagonal orbital nodes.",
    path: "M 6 3 L 6 21 M 6 3 L 15 3 L 18 7 L 15 11 L 6 11 M 6 11 L 16 11 L 19 16 L 16 21 L 6 21",
  },
  C: {
    char: "C",
    name: "Crescent Arc",
    category: "consonant",
    description: "Open quadrant vector tracing angular curvature of incomplete orbits.",
    path: "M 19 6 L 12 3 L 6 8 L 6 16 L 12 21 L 19 18",
  },
  D: {
    char: "D",
    name: "Monolith Node",
    category: "consonant",
    description: "Linear spine bound to parabolic field curvature.",
    path: "M 6 3 L 6 21 M 6 3 L 13 3 L 19 9 L 19 15 L 13 21 L 6 21 M 11 9 L 11 15",
  },
  E: {
    char: "E",
    name: "Triple Horizon",
    category: "vowel",
    description: "Three parallel telemetry datums crossed by a singular vertical spine.",
    path: "M 6 3 L 6 21 M 6 3 L 19 3 M 6 12 L 15 12 M 6 21 L 19 21 M 19 3 L 19 6 M 19 18 L 19 21",
  },
  F: {
    char: "F",
    name: "Cantilever",
    category: "consonant",
    description: "Dual asymmetrical overhangs suspended from primary structural axis.",
    path: "M 6 3 L 6 21 M 6 3 L 19 3 L 19 7 M 6 12 L 15 12 L 15 15",
  },
  G: {
    char: "G",
    name: "Vortex Loop",
    category: "consonant",
    description: "Inward-spiraling boundary envelope with core telemetry intercept.",
    path: "M 19 6 L 12 3 L 6 8 L 6 16 L 12 21 L 18 17 L 18 12 L 12 12",
  },
  H: {
    char: "H",
    name: "Parallel Pillars",
    category: "consonant",
    description: "Twin vertical obelisks linked by high-tension cross-brace.",
    path: "M 6 3 L 6 21 M 18 3 L 18 21 M 6 12 L 18 12 M 12 9 L 12 15",
  },
  I: {
    char: "I",
    name: "Singularity Vector",
    category: "vowel",
    description: "Pure vertical axis capped with orthogonal limiters.",
    path: "M 12 3 L 12 21 M 7 3 L 17 3 M 7 21 L 17 21 M 12 9 L 12 15",
  },
  J: {
    char: "J",
    name: "Anchor Hook",
    category: "consonant",
    description: "Descent trace curving into retrograde kinetic return.",
    path: "M 17 3 L 17 16 L 13 21 L 7 19 L 6 13 M 11 3 L 20 3",
  },
  K: {
    char: "K",
    name: "Chevron Divergence",
    category: "consonant",
    description: "Axial guide branching into acute zenith and nadir thrust lines.",
    path: "M 6 3 L 6 21 M 18 4 L 7 12 L 18 20 M 12 7 L 18 12",
  },
  L: {
    char: "L",
    name: "Orthogonal Base",
    category: "consonant",
    description: "Right-angle baseline establishing spatial foundation coordinates.",
    path: "M 6 3 L 6 21 L 19 21 M 6 9 L 10 9 M 15 21 L 15 17",
  },
  M: {
    char: "M",
    name: "Dual Apex Wave",
    category: "consonant",
    description: "Oscillatory twin-peak frequency envelope grounded at both termini.",
    path: "M 4 21 L 4 3 L 12 14 L 20 3 L 20 21 M 12 14 L 12 21",
  },
  N: {
    char: "N",
    name: "Transverse Diagonal",
    category: "consonant",
    description: "Shearing diagonal gradient coupling opposing vertical vectors.",
    path: "M 5 21 L 5 3 L 19 21 L 19 3 M 12 10 L 12 14",
  },
  O: {
    char: "O",
    name: "Hexagonal Enclosure",
    category: "vowel",
    description: "Closed polygonal perimeter shielding internal vacuum.",
    path: "M 12 3 L 19 7 L 19 17 L 12 21 L 5 17 L 5 7 Z M 12 9 L 12 15",
  },
  P: {
    char: "P",
    name: "Upper Loop Monolith",
    category: "consonant",
    description: "Elevated containment sphere mounted on deep vertical pylon.",
    path: "M 6 3 L 6 21 M 6 3 L 15 3 L 19 7 L 15 12 L 6 12",
  },
  Q: {
    char: "Q",
    name: "Orbed Vector",
    category: "consonant",
    description: "Enclosed orbital ring pierced by downward trajectory vector.",
    path: "M 12 3 L 19 7 L 19 15 L 14 20 L 6 19 L 5 8 Z M 13 14 L 21 21",
  },
  R: {
    char: "R",
    name: "Stabilized Node",
    category: "consonant",
    description: "Loop chamber reinforced with outward-leaning structural strut.",
    path: "M 6 3 L 6 21 M 6 3 L 15 3 L 18 7 L 15 12 L 6 12 M 13 12 L 19 21",
  },
  S: {
    char: "S",
    name: "Sigmoid Stream",
    category: "consonant",
    description: "Sinusoidal flow reversing polarity across central nexus.",
    path: "M 18 6 L 13 3 L 7 6 L 6 10 L 17 14 L 17 18 L 12 21 L 6 18",
  },
  T: {
    char: "T",
    name: "Crossbeam Axis",
    category: "consonant",
    description: "Wide horizontal superstructure balanced upon central plumbline.",
    path: "M 3 4 L 21 4 M 12 4 L 12 21 M 3 4 L 3 8 M 21 4 L 21 8 M 9 21 L 15 21",
  },
  U: {
    char: "U",
    name: "Catenary Well",
    category: "vowel",
    description: "Gravitational basin suspended between symmetrical boundaries.",
    path: "M 5 3 L 5 15 L 10 21 L 14 21 L 19 15 L 19 3 M 12 15 L 12 18",
  },
  V: {
    char: "V",
    name: "Convergence Vertex",
    category: "consonant",
    description: "Acute angle funneling multidirectional forces into focal point.",
    path: "M 4 3 L 12 21 L 20 3 M 9 3 L 12 10 L 15 3",
  },
  W: {
    char: "W",
    name: "Dual Inversion",
    category: "consonant",
    description: "Interlocking twin-vertex troughs mapping quantum superposition.",
    path: "M 3 3 L 7 21 L 12 10 L 17 21 L 21 3 M 7 9 L 17 9",
  },
  X: {
    char: "X",
    name: "Cross Singularity",
    category: "consonant",
    description: "Biaxial diagonal intersection defining absolute coordinate zero.",
    path: "M 4 4 L 20 20 M 20 4 L 4 20 M 12 6 L 12 8 M 12 16 L 12 18 M 6 12 L 8 12 M 16 12 L 18 12",
  },
  Y: {
    char: "Y",
    name: "Bifurcation Branch",
    category: "vowel",
    description: "Upward branching split channeling single feed into dual futures.",
    path: "M 4 4 L 12 13 L 20 4 M 12 13 L 12 21 M 8 21 L 16 21",
  },
  Z: {
    char: "Z",
    name: "Zeta Traverse",
    category: "consonant",
    description: "Opposing horizontal rails bound by rapid oblique scanline.",
    path: "M 4 4 L 20 4 L 4 20 L 20 20 M 4 4 L 4 8 M 20 16 L 20 20 M 9 12 L 15 12",
  },
  " ": {
    char: " ",
    name: "Void Gap",
    category: "operator",
    description: "Empty spacetime delimiter holding zero energy state.",
    path: "M 8 18 L 16 18 M 12 15 L 12 18",
  },
  "0": {
    char: "0",
    name: "Null Ring",
    category: "numeral",
    description: "Zero entropy closed circuit with center diagonal slice.",
    path: "M 12 3 L 19 7 L 19 17 L 12 21 L 5 17 L 5 7 Z M 7 7 L 17 17",
  },
  "1": {
    char: "1",
    name: "Prime Pillar",
    category: "numeral",
    description: "Unit impulse vector.",
    path: "M 8 7 L 12 3 L 12 21 M 7 21 L 17 21",
  },
};

export const CIPHER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

export interface CipherCharacterResult {
  original: string;
  substituted: string;
  shifted: string;
  position: number;
  shift: number;
  glyph: GlyphDefinition | null;
}

export interface CipherResult {
  text: string;
  keyedAlphabet: string;
  characters: CipherCharacterResult[];
}

export function normalizeCipherKey(key: string): string {
  const seen = new Set<string>();
  let normalized = "";

  for (const char of key.toUpperCase()) {
    if (!/[A-Z]/.test(char) || seen.has(char)) continue;
    seen.add(char);
    normalized += char;
  }

  return normalized;
}

export function buildKeyedAlphabet(key: string): string {
  const normalizedKey = normalizeCipherKey(key);
  const remainder = CIPHER_ALPHABET
    .split("")
    .filter((char) => !normalizedKey.includes(char))
    .join("");

  return normalizedKey + remainder;
}

export function getShiftForPosition(position: number, key: string): number {
  return normalizeCipherKey(key).length + position;
}

function getGlyphOrNull(char: string): GlyphDefinition | null {
  return /^[A-Z]$/.test(char) ? getGlyph(char) : null;
}

export function encodeCipherText(text: string, key: string): CipherResult {
  const keyedAlphabet = buildKeyedAlphabet(key);
  const normalizedKey = normalizeCipherKey(key);
  let position = 0;
  let encoded = "";
  const characters: CipherCharacterResult[] = [];

  for (const original of text.toUpperCase()) {
    if (!/^[A-Z]$/.test(original) || !normalizedKey) {
      encoded += original;
      characters.push({ original, substituted: original, shifted: original, position, shift: 0, glyph: getGlyphOrNull(original) });
      continue;
    }

    const alphabetIndex = CIPHER_ALPHABET.indexOf(original);
    const substituted = keyedAlphabet[alphabetIndex];
    const shift = getShiftForPosition(position, key);
    const shifted = keyedAlphabet[(keyedAlphabet.indexOf(substituted) + shift) % keyedAlphabet.length];
    encoded += shifted;
    characters.push({ original, substituted, shifted, position, shift, glyph: getGlyphOrNull(shifted) });
    position += 1;
  }

  return { text: encoded, keyedAlphabet, characters };
}

export function decodeCipherText(text: string, key: string): CipherResult {
  const keyedAlphabet = buildKeyedAlphabet(key);
  const normalizedKey = normalizeCipherKey(key);
  let position = 0;
  let decoded = "";
  const characters: CipherCharacterResult[] = [];

  for (const original of text.toUpperCase()) {
    if (!/^[A-Z]$/.test(original) || !normalizedKey) {
      decoded += original;
      characters.push({ original, substituted: original, shifted: original, position, shift: 0, glyph: getGlyphOrNull(original) });
      continue;
    }

    const shift = getShiftForPosition(position, key);
    const shiftedIndex = (keyedAlphabet.indexOf(original) - shift + keyedAlphabet.length) % keyedAlphabet.length;
    const substituted = keyedAlphabet[shiftedIndex];
    const decodedChar = CIPHER_ALPHABET[alphabetIndexFor(keyedAlphabet, substituted)];
    decoded += decodedChar;
    characters.push({ original, substituted, shifted: decodedChar, position, shift, glyph: getGlyphOrNull(decodedChar) });
    position += 1;
  }

  return { text: decoded, keyedAlphabet, characters };
}

function alphabetIndexFor(keyedAlphabet: string, char: string): number {
  return keyedAlphabet.indexOf(char);
}

export function getGlyph(char: string): GlyphDefinition {
  const upper = char.toUpperCase();
  if (CIPHER_DICTIONARY[upper]) {
    return CIPHER_DICTIONARY[upper];
  }
  // Default fallback glyph
  return {
    char: upper,
    name: "Indeterminate Node",
    category: "operator",
    description: "Undefined boundary coordinate in cipher space.",
    path: "M 12 6 L 18 12 L 12 18 L 6 12 Z M 12 10 L 12 14",
  };
}

export function encodeText(text: string): GlyphDefinition[] {
  return text.split("").map((c) => getGlyph(c));
}
