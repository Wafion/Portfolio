/**
 * Cinematic Sound Engine
 * Procedural Web Audio: dark gallery installation ambient,
 * soft harmonic textures, and subtle environmental sound.
 * No harsh beeps. No constant clicks. Sound is optional.
 */

class SoundEngine {
  private ctx: AudioContext | null = null;
  private isMuted: boolean = true;
  private droneGain: GainNode | null = null;
  private oscNodes: OscillatorNode[] = [];
  private lfoNodes: OscillatorNode[] = [];

  private initContext() {
    if (!this.ctx && typeof window !== "undefined") {
      const AudioCtx =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  public toggleMute(): boolean {
    this.initContext();
    this.isMuted = !this.isMuted;
    if (this.isMuted) {
      this.stopAmbientDrone();
    } else {
      this.startAmbientDrone();
      this.playSoftClick(440, 0.08);
    }
    return !this.isMuted;
  }

  public getIsMuted(): boolean {
    return this.isMuted;
  }

  public startAmbientDrone() {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    if (this.droneGain) return;

    try {
      const now = this.ctx.currentTime;

      // Master gain — very quiet
      this.droneGain = this.ctx.createGain();
      this.droneGain.gain.setValueAtTime(0.001, now);
      this.droneGain.gain.exponentialRampToValueAtTime(0.03, now + 4);

      // Low-pass filter for warmth
      const filter = this.ctx.createBiquadFilter();
      filter.type = "lowpass";
      filter.frequency.setValueAtTime(200, now);
      filter.Q.setValueAtTime(0.5, now);

      // Sub bass drone — deep F1 (43.65 Hz)
      const osc1 = this.ctx.createOscillator();
      osc1.type = "sine";
      osc1.frequency.setValueAtTime(43.65, now);

      // Warm second — C2 (65.4 Hz)
      const osc2 = this.ctx.createOscillator();
      osc2.type = "triangle";
      osc2.frequency.setValueAtTime(65.4, now);

      // Ethereal fifth — very quiet (130.81 Hz)
      const osc3 = this.ctx.createOscillator();
      osc3.type = "sine";
      osc3.frequency.setValueAtTime(130.81, now);

      // LFO for subtle pulsation
      const lfo = this.ctx.createOscillator();
      lfo.type = "sine";
      lfo.frequency.setValueAtTime(0.08, now); // Very slow pulse
      const lfoGain = this.ctx.createGain();
      lfoGain.gain.setValueAtTime(0.005, now);
      lfo.connect(lfoGain);
      lfoGain.connect(this.droneGain.gain);

      osc1.connect(filter);
      osc2.connect(filter);
      osc3.connect(filter);
      filter.connect(this.droneGain);
      this.droneGain.connect(this.ctx.destination);

      osc1.start();
      osc2.start();
      osc3.start();
      lfo.start();

      this.oscNodes = [osc1, osc2, osc3];
      this.lfoNodes = [lfo];
    } catch {
      // Audio context might fail on non-interacted page
    }
  }

  public stopAmbientDrone() {
    if (this.droneGain && this.ctx) {
      const now = this.ctx.currentTime;
      this.droneGain.gain.setValueAtTime(this.droneGain.gain.value, now);
      this.droneGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.2);
      setTimeout(() => {
        [...this.oscNodes, ...this.lfoNodes].forEach((osc) => {
          try {
            osc.stop();
            osc.disconnect();
          } catch {}
        });
        this.oscNodes = [];
        this.lfoNodes = [];
        this.droneGain?.disconnect();
        this.droneGain = null;
      }, 1300);
    }
  }

  /** Soft interaction click — low, warm, tactile */
  public playSoftClick(freq = 440, duration = 0.06) {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now);
      osc.frequency.exponentialRampToValueAtTime(80, now + duration);

      gain.gain.setValueAtTime(0.02, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + duration + 0.01);
    } catch {}
  }

  /** Cipher chirp — slightly brighter, for encoding feedback */
  public playCipherChirp(pitchShift = 1) {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;
      const baseFreq = 660 * pitchShift;

      osc.type = "triangle";
      osc.frequency.setValueAtTime(baseFreq, now);
      osc.frequency.exponentialRampToValueAtTime(baseFreq * 0.6, now + 0.08);

      gain.gain.setValueAtTime(0.018, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.08);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.09);
    } catch {}
  }

  /** Deep artifact resonance — for 3D interaction */
  public playArtifactResonance() {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;

      osc.type = "sine";
      osc.frequency.setValueAtTime(55, now); // A1
      osc.frequency.linearRampToValueAtTime(82.4, now + 0.5); // E2

      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.035, now + 0.2);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.6);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.65);
    } catch {}
  }

  /** Soft section transition tone */
  public playSectionTone(freq = 220) {
    if (this.isMuted) return;
    this.initContext();
    if (!this.ctx) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      const now = this.ctx.currentTime;

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now);

      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.015, now + 0.15);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.4);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.45);
    } catch {}
  }

  /** Quiet procedural cues for the PAGE.OS archive discovery scene. */
  public playArchiveStatic() {
    if (this.isMuted) return;
    this.playSoftClick(175, 0.18);
  }

  public playArchiveCard() {
    if (this.isMuted) return;
    this.playSoftClick(290, 0.1);
    window.setTimeout(() => this.playSoftClick(440, 0.08), 90);
  }

  public playArchiveReveal() {
    if (this.isMuted) return;
    this.playSectionTone(92);
    window.setTimeout(() => this.playSectionTone(138), 130);
    window.setTimeout(() => this.playSectionTone(207), 270);
  }

  /** Sparse archive discovery cues. These stay procedural and quiet by design. */
  public playArchiveSignal() {
    this.playSoftClick(520, 0.12);
  }

  public playArchiveUnlock() {
    this.playSectionTone(110);
    window.setTimeout(() => this.playSectionTone(165), 110);
  }

  /** Short mechanical samples for the manuscript installation. */
  public playTypewriterKey() {
    if (this.isMuted || typeof window === "undefined") return;
    try {
      const audio = new Audio("/audio/typewriter-hit-soft.mp3");
      audio.volume = 0.24;
      audio.playbackRate = 0.92 + Math.random() * 0.16;
      void audio.play();
    } catch {}
  }

  public playTypewriterReturn() {
    if (this.isMuted || typeof window === "undefined") return;
    try {
      const audio = new Audio("/audio/typewriter-return-bell.mp3");
      audio.volume = 0.32;
      void audio.play();
    } catch {}
  }

}

export const sound = new SoundEngine();
