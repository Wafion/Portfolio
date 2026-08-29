"use client";

import React, { useEffect, useMemo, useState } from "react";
import {
  CIPHER_DICTIONARY,
  CipherCharacterResult,
  decodeCipherText,
  encodeCipherText,
  GlyphDefinition,
  normalizeCipherKey,
} from "@/lib/data/cipher";
import { GlyphSymbol } from "@/components/ui/GlyphSymbol";
import { sound } from "@/components/audio/SoundEngine";
import { Check, Copy, LockKeyhole, RotateCcw } from "lucide-react";

const CHALLENGE_TEXT = "BUILD BETWEEN WORLDS";
type CipherMode = "encode" | "decode";
type ChallengeState = "idle" | "success" | "error";

function CharacterGlyphs({ characters, onSelect }: { characters: CipherCharacterResult[]; onSelect: (character: CipherCharacterResult) => void }) {
  return (
    <div className="cipher-output-grid" aria-label="Glyph output">
      {characters.map((character, index) => {
        if (character.original === " ") return <span className="cipher-word-gap" key={`${character.original}-${index}`} aria-hidden="true" />;
        if (!character.glyph) return <span className="cipher-punctuation" key={`${character.original}-${index}`}>{character.original}</span>;
        return (
          <button className="cipher-glyph-button" key={`${character.original}-${index}`} onClick={() => onSelect(character)} aria-label={`Inspect ${character.shifted}`}>
            <GlyphSymbol char={character.shifted} size={30} color="#D4C87A" interactive={false} />
            <span>{character.shifted}</span>
          </button>
        );
      })}
    </div>
  );
}

export function CipherLab() {
  const [keyInput, setKeyInput] = useState("MYSTERY");
  const [inputText, setInputText] = useState("HELLO WORLD");
  const [mode, setMode] = useState<CipherMode>("encode");
  const [selectedGlyph, setSelectedGlyph] = useState<GlyphDefinition>(CIPHER_DICTIONARY.A);
  const [selectedCharacter, setSelectedCharacter] = useState<CipherCharacterResult | null>(null);
  const [challengeAnswer, setChallengeAnswer] = useState("");
  const [challengeState, setChallengeState] = useState<ChallengeState>("idle");
  const [copied, setCopied] = useState(false);

  const normalizedKey = normalizeCipherKey(keyInput);
  const isKeyValid = normalizedKey.length > 0;
  const challenge = useMemo(() => encodeCipherText(CHALLENGE_TEXT, keyInput), [keyInput]);
  const result = useMemo(() => {
    if (!isKeyValid) return encodeCipherText("", "MYSTERY");
    return mode === "encode" ? encodeCipherText(inputText, keyInput) : decodeCipherText(inputText, keyInput);
  }, [inputText, isKeyValid, keyInput, mode]);

  useEffect(() => {
    setChallengeAnswer("");
    setChallengeState("idle");
    if (!isKeyValid) return;
    const timer = window.setTimeout(() => sound.playCipherChirp(0.85), 220);
    return () => window.clearTimeout(timer);
  }, [normalizedKey, isKeyValid]);

  useEffect(() => {
    const firstGlyph = result.characters.find((character) => character.glyph);
    if (firstGlyph?.glyph) {
      setSelectedGlyph(firstGlyph.glyph);
      setSelectedCharacter(firstGlyph);
    }
  }, [result]);

  const selectCharacter = (character: CipherCharacterResult) => {
    if (!character.glyph) return;
    sound.playCipherChirp(0.9);
    setSelectedGlyph(character.glyph);
    setSelectedCharacter(character);
  };

  const handleCopy = async () => {
    if (!isKeyValid) return;
    await navigator.clipboard.writeText(result.text);
    sound.playSoftClick(400);
    setCopied(true);
    window.setTimeout(() => setCopied(false), 1800);
  };

  const checkChallenge = () => {
    if (!isKeyValid) return;
    const answer = challengeAnswer.toUpperCase().replace(/[^A-Z ]/g, "").replace(/\s+/g, " ").trim();
    const isCorrect = answer === CHALLENGE_TEXT;
    setChallengeState(isCorrect ? "success" : "error");
    if (isCorrect) sound.playCipherChirp(1.25);
    else sound.playSoftClick(150);
  };

  return (
    <div className="cipher-lab-shell">
      <div className="cipher-key-card">
        <div className="cipher-card-heading">
          <div><span className="cipher-eyebrow">INTERACTIVE CIPHER LAB</span><h3>Change the key. Change the language.</h3></div>
          <span className={`cipher-key-status ${isKeyValid ? "is-valid" : "is-invalid"}`}><span className="cipher-status-dot" /> {isKeyValid ? "KEY ACCEPTED" : "KEY EMPTY"}</span>
        </div>
        <label className="cipher-field-label" htmlFor="cipher-key">CUSTOM KEY</label>
        <div className="cipher-key-row"><LockKeyhole className="cipher-key-icon" aria-hidden="true" /><input id="cipher-key" value={keyInput} onChange={(event) => setKeyInput(event.target.value)} placeholder="TYPE A WORD OR PHRASE" autoComplete="off" aria-describedby="cipher-key-help" /></div>
        <div className="cipher-key-meta" id="cipher-key-help"><span>NORMALIZED KEY: <strong>{normalizedKey || "NONE"}</strong></span><span>{normalizedKey.length} UNIQUE LETTERS / SPACES IGNORED</span></div>
      </div>

      <div className="cipher-pipeline" aria-label="Cipher pipeline"><span>CUSTOM KEY</span><i>→</i><span>KEYED ALPHABET</span><i>→</i><span>POSITION SHIFT</span><i>→</i><span>GLYPHS</span></div>

      <div className="cipher-console-grid">
        <div className="cipher-console">
          <div className="cipher-console-topline"><div className="cipher-mode-toggle" role="group" aria-label="Cipher operation"><button className={mode === "encode" ? "is-active" : ""} onClick={() => setMode("encode")}>ENCODE</button><button className={mode === "decode" ? "is-active" : ""} onClick={() => setMode("decode")}>DECODE</button></div><button className="cipher-copy-button" onClick={handleCopy} disabled={!isKeyValid}>{copied ? <Check size={13} /> : <Copy size={13} />} {copied ? "COPIED" : "COPY OUTPUT"}</button></div>
          <label className="cipher-field-label" htmlFor="cipher-message">{mode === "encode" ? "PLAINTEXT INPUT" : "CIPHER INPUT"}</label>
          <input id="cipher-message" value={inputText} onChange={(event) => setInputText(event.target.value)} maxLength={80} placeholder={mode === "encode" ? "TYPE TO ENCODE..." : "PASTE CIPHER TEXT..."} />
          <div className="cipher-output-heading"><span>{mode === "encode" ? "GLYPH OUTPUT" : "DECODED TEXT"}</span><span>{result.text.length} CHARS</span></div>
          {mode === "encode" ? <CharacterGlyphs characters={result.characters} onSelect={selectCharacter} /> : <div className="cipher-decoded-output">{result.text || "Awaiting cipher input..."}</div>}
        </div>

        <aside className="cipher-inspector"><div className="cipher-output-heading"><span>GLYPH INSPECTOR</span><span className="cipher-inspector-char">{selectedGlyph.char}</span></div><div className="cipher-inspector-glyph"><GlyphSymbol char={selectedGlyph.char} size={86} color="#D4C87A" strokeWidth={1.4} interactive={false} /></div><div className="cipher-inspector-rows"><div><span>NAME</span><strong>{selectedGlyph.name}</strong></div><div><span>TYPE</span><strong>{selectedGlyph.category.toUpperCase()}</strong></div><div><span>SHIFT</span><strong>{selectedCharacter?.shift ?? "--"}</strong></div><div><span>POSITION</span><strong>{selectedCharacter ? selectedCharacter.position + 1 : "--"}</strong></div></div><p>{selectedGlyph.description}</p></aside>
      </div>

      <div className="cipher-challenge"><div><span className="cipher-eyebrow">OPTIONAL FIELD TEST</span><h4>Break the seal</h4><p>Decode the challenge with your current key. Change the key and the seal resets.</p></div><div className="cipher-challenge-code" aria-label="Encrypted challenge">{challenge.text}</div><div className="cipher-challenge-actions"><label className="sr-only" htmlFor="cipher-challenge-answer">Challenge answer</label><input id="cipher-challenge-answer" value={challengeAnswer} onChange={(event) => { setChallengeAnswer(event.target.value); setChallengeState("idle"); }} placeholder="ENTER THE DECODED PHRASE" /><button onClick={checkChallenge} disabled={!isKeyValid}>CHECK</button><button className="cipher-reset-button" onClick={() => { setChallengeAnswer(""); setChallengeState("idle"); }} aria-label="Reset challenge"><RotateCcw size={14} /></button></div><div className={`cipher-challenge-status ${challengeState}`} role="status">{challengeState === "success" ? "SEAL OPENED / THE ARCHIVE REMEMBERS" : challengeState === "error" ? "NOT THIS READING / TRY AGAIN" : "ENTER YOUR READING TO VERIFY"}</div></div>
    </div>
  );
}
