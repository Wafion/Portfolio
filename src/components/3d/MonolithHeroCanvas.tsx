"use client";

import React, { useEffect, useRef, useState } from "react";
import * as THREE from "three";
import { sound } from "@/components/audio/SoundEngine";

export function MonolithHeroCanvas() {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    let width = container.clientWidth || window.innerWidth;
    let height = container.clientHeight || window.innerHeight;

    // 1. Scene
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x0c0f17, 0.08);

    // 2. Camera
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    camera.position.set(0, 0, 5.5);

    // 3. Renderer with hardware acceleration and anti-aliasing
    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;
    container.appendChild(renderer.domElement);

    // 4. Lighting
    const ambientLight = new THREE.AmbientLight(0x2a364f, 1.8);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0x38bdf8, 2.5);
    keyLight.position.set(4, 5, 4);
    scene.add(keyLight);

    const rimLight = new THREE.DirectionalLight(0xfbbf24, 2.0);
    rimLight.position.set(-4, -2, -3);
    scene.add(rimLight);

    const bottomGlow = new THREE.PointLight(0x06b6d4, 3.0, 10);
    bottomGlow.position.set(0, -2.5, 1);
    scene.add(bottomGlow);

    // 5. Monolith Group
    const monolithGroup = new THREE.Group();
    scene.add(monolithGroup);

    // Primary Monolith Core (Chamfered look with glossy obsidian material)
    const monolithGeo = new THREE.BoxGeometry(1.25, 3.2, 0.75);
    const monolithMat = new THREE.MeshPhysicalMaterial({
      color: 0x181e2e,
      roughness: 0.15,
      metalness: 0.85,
      clearcoat: 0.6,
      clearcoatRoughness: 0.2,
      reflectivity: 0.9,
    });
    const monolithMesh = new THREE.Mesh(monolithGeo, monolithMat);
    monolithGroup.add(monolithMesh);

    // Luminous Edge Wireframe
    const edgesGeo = new THREE.EdgesGeometry(new THREE.BoxGeometry(1.255, 3.205, 0.755));
    const edgesMat = new THREE.LineBasicMaterial({
      color: 0x38bdf8,
      linewidth: 1.5,
      transparent: true,
      opacity: 0.7,
    });
    const edgesLine = new THREE.LineSegments(edgesGeo, edgesMat);
    monolithGroup.add(edgesLine);

    // Center Glowing Vertical Core Line
    const coreGeo = new THREE.PlaneGeometry(0.06, 2.2);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.85,
    });
    const coreFront = new THREE.Mesh(coreGeo, coreMat);
    coreFront.position.set(0, 0, 0.38);
    monolithGroup.add(coreFront);

    const coreBack = coreFront.clone();
    coreBack.position.set(0, 0, -0.38);
    coreBack.rotation.y = Math.PI;
    monolithGroup.add(coreBack);

    // Concentric Mechanical Rings
    const ring1Geo = new THREE.TorusGeometry(2.3, 0.018, 16, 80);
    const ring1Mat = new THREE.MeshStandardMaterial({
      color: 0x64748b,
      metalness: 0.9,
      roughness: 0.2,
    });
    const ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
    ring1.rotation.x = Math.PI / 3;
    monolithGroup.add(ring1);

    const ring2Geo = new THREE.TorusGeometry(2.8, 0.014, 16, 80);
    const ring2Mat = new THREE.MeshStandardMaterial({
      color: 0x475569,
      metalness: 0.9,
      roughness: 0.2,
    });
    const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
    ring2.rotation.x = -Math.PI / 4;
    ring2.rotation.y = Math.PI / 6;
    monolithGroup.add(ring2);

    // 6. Volumetric Particle Field
    const particleCount = 380;
    const particlePositions = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      const radius = 2.5 + Math.random() * 5.5;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(Math.random() * 2 - 1);

      particlePositions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
      particlePositions[i * 3 + 1] = (Math.random() - 0.5) * 6;
      particlePositions[i * 3 + 2] = radius * Math.cos(phi);
    }
    const particleGeo = new THREE.BufferGeometry();
    particleGeo.setAttribute("position", new THREE.BufferAttribute(particlePositions, 3));
    const particleMat = new THREE.PointsMaterial({
      color: 0x93c5fd,
      size: 0.04,
      transparent: true,
      opacity: 0.65,
      blending: THREE.AdditiveBlending,
    });
    const particleSystem = new THREE.Points(particleGeo, particleMat);
    scene.add(particleSystem);

    // 7. Mouse Interaction & Parallax Tracking
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;

    const onMouseMove = (e: MouseEvent) => {
      mouseX = (e.clientX / window.innerWidth) * 2 - 1;
      mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
    };
    window.addEventListener("mousemove", onMouseMove);

    const onResize = () => {
      if (!container) return;
      width = container.clientWidth;
      height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    };
    window.addEventListener("resize", onResize);

    // 8. Animation Loop
    let animId: number;
    let clock = new THREE.Clock();

    const animate = () => {
      const delta = clock.getDelta();
      const elapsedTime = clock.getElapsedTime();

      // Smooth mouse lerp
      targetX += (mouseX * 0.45 - targetX) * 0.06;
      targetY += (mouseY * 0.35 - targetY) * 0.06;

      monolithGroup.rotation.y = targetX + elapsedTime * 0.12;
      monolithGroup.rotation.x = -targetY;
      monolithGroup.position.y = Math.sin(elapsedTime * 0.8) * 0.12;

      // Rotate orbital rings
      ring1.rotation.z += delta * 0.25;
      ring1.rotation.x += delta * 0.1;
      ring2.rotation.z -= delta * 0.2;
      ring2.rotation.y += delta * 0.15;

      // Rotate particle field
      particleSystem.rotation.y += delta * 0.025;

      renderer.render(scene, camera);
      animId = requestAnimationFrame(animate);
    };

    animate();

    // 9. Cleanup
    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("resize", onResize);
      if (renderer.domElement && container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
      renderer.dispose();
      monolithGeo.dispose();
      monolithMat.dispose();
      edgesGeo.dispose();
      edgesMat.dispose();
      particleGeo.dispose();
      particleMat.dispose();
      ring1Geo.dispose();
      ring1Mat.dispose();
      ring2Geo.dispose();
      ring2Mat.dispose();
    };
  }, []);

  const handleMouseEnter = () => {
    setIsHovered(true);
    sound.playArtifactResonance();
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <div
      ref={containerRef}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className="w-full h-full relative cursor-grab active:cursor-grabbing select-none"
      data-cursor="MONOLITH 3D"
    />
  );
}
