"use client";

import React, { useEffect, useRef, useState } from "react";
import * as THREE from "three";
import { sound } from "@/components/audio/SoundEngine";

interface HoveredFragmentInfo {
  title: string;
  sublabels: string[];
  color: string;
}

export function UnfinishedArtifactCanvas() {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [hoveredFragment, setHoveredFragment] = useState<HoveredFragmentInfo | null>(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    let width = container.clientWidth || window.innerWidth;
    let height = container.clientHeight || window.innerHeight;

    // Scene
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050505, 0.06);

    // Camera — cinematic perspective
    const camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
    camera.position.set(0, 0.3, 6.5);

    // Renderer
    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;
    container.appendChild(renderer.domElement);

    // === LIGHTING — Dark Gallery ===
    // Ambient — very subtle, just enough to see form
    const ambient = new THREE.AmbientLight(0x1a1a2e, 1.2);
    scene.add(ambient);

    // Key light — soft, from upper right
    const keyLight = new THREE.DirectionalLight(0xE8E5DD, 1.8);
    keyLight.position.set(4, 5, 3);
    keyLight.castShadow = true;
    scene.add(keyLight);

    // Rim light — very subtle, cool
    const rimLight = new THREE.DirectionalLight(0x4A6FA5, 0.6);
    rimLight.position.set(-3, 2, -4);
    scene.add(rimLight);

    // Ground reflection — faint warm
    const groundLight = new THREE.PointLight(0xE8E5DD, 0.4, 10);
    groundLight.position.set(0, -3, 1);
    scene.add(groundLight);

    // === ARTIFACT GROUP ===
    const artifactGroup = new THREE.Group();
    scene.add(artifactGroup);

    // === CENTRAL CORE — Irregular, sculpted, dark translucent ===
    // Use IcosahedronGeometry with low detail for irregular form
    const coreGeo = new THREE.IcosahedronGeometry(0.9, 1);
    // Distort vertices for organic irregularity
    const corePositions = coreGeo.attributes.position;
    for (let i = 0; i < corePositions.count; i++) {
      const x = corePositions.getX(i);
      const y = corePositions.getY(i);
      const z = corePositions.getZ(i);
      const noise = 1 + Math.sin(x * 3.7) * 0.08 + Math.cos(y * 2.3) * 0.06 + Math.sin(z * 4.1) * 0.05;
      corePositions.setXYZ(i, x * noise, y * noise, z * noise);
    }
    coreGeo.computeVertexNormals();

    const coreMat = new THREE.MeshPhysicalMaterial({
      color: 0x0a0a12,
      roughness: 0.15,
      metalness: 0.7,
      transmission: 0.4,
      ior: 1.6,
      thickness: 1.5,
      clearcoat: 0.6,
      clearcoatRoughness: 0.15,
      envMapIntensity: 0.8,
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    artifactGroup.add(coreMesh);

    // Inner core glow — subtle wireframe pulse
    const innerGeo = new THREE.IcosahedronGeometry(0.35, 0);
    const innerMat = new THREE.MeshBasicMaterial({
      color: 0xE8E5DD,
      wireframe: true,
      transparent: true,
      opacity: 0.4,
    });
    const innerCore = new THREE.Mesh(innerGeo, innerMat);
    artifactGroup.add(innerCore);

    // === STRUCTURAL FRAME — Angular mechanical supports ===
    const frameGroup = new THREE.Group();
    artifactGroup.add(frameGroup);

    // 6 angular struts radiating from core
    const strutMat = new THREE.MeshStandardMaterial({
      color: 0x3a3a42,
      metalness: 0.95,
      roughness: 0.2,
    });

    const strutDirections = [
      [1, 0.6, 0],
      [-1, 0.4, 0.5],
      [0, 1, 0.3],
      [0, -1, 0.2],
      [0.5, 0, -1],
      [-0.5, -0.3, -0.8],
    ];

    strutDirections.forEach(([dx, dy, dz]) => {
      const strutGeo = new THREE.CylinderGeometry(0.012, 0.008, 1.6, 6);
      const strut = new THREE.Mesh(strutGeo, strutMat);
      strut.position.set(dx * 1.1, dy * 0.9, dz * 0.9);
      strut.lookAt(0, 0, 0);
      strut.rotateX(Math.PI / 2);
      frameGroup.add(strut);

      // Joint node at strut end
      const jointGeo = new THREE.SphereGeometry(0.04, 8, 8);
      const jointMat = new THREE.MeshStandardMaterial({
        color: 0x5a5a62,
        metalness: 0.9,
        roughness: 0.15,
      });
      const joint = new THREE.Mesh(jointGeo, jointMat);
      joint.position.set(dx * 1.9, dy * 1.7, dz * 1.7);
      frameGroup.add(joint);
    });

    // === SEVEN DOMAIN FRAGMENTS ===
    interface FragmentEntry {
      mesh: THREE.Object3D;
      info: HoveredFragmentInfo;
      orbitRadius: number;
      orbitSpeed: number;
      orbitAngle: number;
      baseY: number;
      raycastTarget: THREE.Object3D;
    }

    const fragments: FragmentEntry[] = [];
    const raycastTargets: THREE.Object3D[] = [];

    // 1. CODE — Computational lattice / geometric grid
    const codeGroup = new THREE.Group();
    const codeGeo = new THREE.BoxGeometry(0.4, 0.4, 0.4);
    const codeWireframe = new THREE.EdgesGeometry(codeGeo);
    const codeLine = new THREE.LineSegments(
      codeWireframe,
      new THREE.LineBasicMaterial({ color: 0x4A90D9, transparent: true, opacity: 0.7 })
    );
    codeGroup.add(codeLine);
    // Inner grid planes
    const codePlaneGeo = new THREE.PlaneGeometry(0.35, 0.35, 3, 3);
    const codePlaneMat = new THREE.MeshBasicMaterial({ color: 0x4A90D9, wireframe: true, transparent: true, opacity: 0.4 });
    const codePlane = new THREE.Mesh(codePlaneGeo, codePlaneMat);
    codeGroup.add(codePlane);
    artifactGroup.add(codeGroup);
    fragments.push({
      mesh: codeGroup,
      info: { title: "CODE", sublabels: ["SOFTWARE", "SYSTEMS", "ARCHITECTURE"], color: "#4A90D9" },
      orbitRadius: 2.3,
      orbitSpeed: 0.35,
      orbitAngle: 0,
      baseY: 0.7,
      raycastTarget: codePlane,
    });
    raycastTargets.push(codePlane);

    // 2. FILM — Aperture / cinematic frame mechanism
    const filmGroup = new THREE.Group();
    // Aperture ring (not literal camera)
    const filmRingGeo = new THREE.RingGeometry(0.18, 0.3, 6);
    const filmRingMat = new THREE.MeshStandardMaterial({
      color: 0xD4A753,
      metalness: 0.85,
      roughness: 0.2,
      side: THREE.DoubleSide,
    });
    const filmRing = new THREE.Mesh(filmRingGeo, filmRingMat);
    filmGroup.add(filmRing);
    // Inner blades
    for (let i = 0; i < 5; i++) {
      const bladeGeo = new THREE.PlaneGeometry(0.12, 0.06);
      const bladeMat = new THREE.MeshStandardMaterial({
        color: 0xD4A753,
        metalness: 0.9,
        roughness: 0.15,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.6,
      });
      const blade = new THREE.Mesh(bladeGeo, bladeMat);
      const angle = (i / 5) * Math.PI * 2;
      blade.position.set(Math.cos(angle) * 0.15, Math.sin(angle) * 0.15, 0);
      blade.rotation.z = angle;
      filmGroup.add(blade);
    }
    artifactGroup.add(filmGroup);
    fragments.push({
      mesh: filmGroup,
      info: { title: "FILM", sublabels: ["DIRECTING", "EDITING", "VISUAL STORYTELLING"], color: "#D4A753" },
      orbitRadius: 2.5,
      orbitSpeed: 0.28,
      orbitAngle: Math.PI * 0.35,
      baseY: -0.4,
      raycastTarget: filmRing,
    });
    raycastTargets.push(filmRing);

    // 3. AI — Branching neural lattice (organic + computational)
    const aiGroup = new THREE.Group();
    const aiNodeGeo = new THREE.IcosahedronGeometry(0.2, 1);
    const aiNodeMat = new THREE.MeshStandardMaterial({
      color: 0x5BB8D4,
      metalness: 0.5,
      roughness: 0.25,
      transparent: true,
      opacity: 0.8,
    });
    const aiNode = new THREE.Mesh(aiNodeGeo, aiNodeMat);
    aiGroup.add(aiNode);
    // Branching connections
    const branchMat = new THREE.LineBasicMaterial({ color: 0x5BB8D4, transparent: true, opacity: 0.5 });
    for (let i = 0; i < 8; i++) {
      const theta = (i / 8) * Math.PI * 2;
      const phi = Math.random() * Math.PI;
      const r = 0.35;
      const start = new THREE.Vector3(0, 0, 0);
      const end = new THREE.Vector3(
        r * Math.sin(phi) * Math.cos(theta),
        r * Math.sin(phi) * Math.sin(theta),
        r * Math.cos(phi)
      );
      const branchGeo = new THREE.BufferGeometry().setFromPoints([start, end]);
      const branch = new THREE.Line(branchGeo, branchMat);
      aiGroup.add(branch);
      // Node at end
      const endNodeGeo = new THREE.SphereGeometry(0.025, 6, 6);
      const endNodeMat = new THREE.MeshBasicMaterial({ color: 0x5BB8D4 });
      const endNode = new THREE.Mesh(endNodeGeo, endNodeMat);
      endNode.position.copy(end);
      aiGroup.add(endNode);
    }
    artifactGroup.add(aiGroup);
    fragments.push({
      mesh: aiGroup,
      info: { title: "AI", sublabels: ["MACHINE LEARNING", "NLP", "LOCAL AI"], color: "#5BB8D4" },
      orbitRadius: 2.4,
      orbitSpeed: -0.3,
      orbitAngle: Math.PI * 0.7,
      baseY: 0.5,
      raycastTarget: aiNode,
    });
    raycastTargets.push(aiNode);

    // 4. 3D — Partially constructed polyhedral structure
    const d3Group = new THREE.Group();
    const d3Geo = new THREE.OctahedronGeometry(0.22, 0);
    const d3Mat = new THREE.MeshStandardMaterial({
      color: 0x6B9FD4,
      metalness: 0.8,
      roughness: 0.2,
      wireframe: true,
    });
    const d3Mesh = new THREE.Mesh(d3Geo, d3Mat);
    d3Group.add(d3Mesh);
    // Partial faces — "partially constructed"
    const partialGeo = new THREE.TetrahedronGeometry(0.15, 0);
    const partialMat = new THREE.MeshStandardMaterial({
      color: 0x6B9FD4,
      metalness: 0.7,
      roughness: 0.3,
      transparent: true,
      opacity: 0.5,
    });
    const partialMesh = new THREE.Mesh(partialGeo, partialMat);
    partialMesh.position.set(0.15, 0.1, 0.05);
    d3Group.add(partialMesh);
    artifactGroup.add(d3Group);
    fragments.push({
      mesh: d3Group,
      info: { title: "3D", sublabels: ["BLENDER", "GEOMETRY", "VISUAL EXPERIMENTATION"], color: "#6B9FD4" },
      orbitRadius: 2.6,
      orbitSpeed: 0.25,
      orbitAngle: Math.PI * 1.1,
      baseY: -0.7,
      raycastTarget: d3Mesh,
    });
    raycastTargets.push(d3Mesh);

    // 5. WRITING — Thin layered paper/manuscript planes
    const writingGroup = new THREE.Group();
    const paperMat = new THREE.MeshStandardMaterial({
      color: 0xB8B6AF,
      roughness: 0.85,
      metalness: 0.02,
      side: THREE.DoubleSide,
    });
    for (let i = 0; i < 4; i++) {
      const paperGeo = new THREE.BoxGeometry(0.28, 0.38, 0.008);
      const paper = new THREE.Mesh(paperGeo, paperMat.clone());
      paper.rotation.z = i * 0.12 - 0.18;
      paper.position.z = i * 0.015;
      paper.position.y = i * 0.01;
      paper.material.opacity = 1 - i * 0.15;
      paper.material.transparent = true;
      writingGroup.add(paper);
    }
    artifactGroup.add(writingGroup);
    fragments.push({
      mesh: writingGroup,
      info: { title: "WRITING", sublabels: ["MANUSCRIPTS", "LITERATURE", "STORIES"], color: "#B8B6AF" },
      orbitRadius: 2.35,
      orbitSpeed: -0.32,
      orbitAngle: Math.PI * 1.45,
      baseY: 0.3,
      raycastTarget: writingGroup.children[0] as THREE.Object3D,
    });
    raycastTargets.push(writingGroup.children[0] as THREE.Object3D);

    // 6. ENGINEERING — Small mechanical assembly
    const engGroup = new THREE.Group();
    // Gear-like cylinder
    const gearGeo = new THREE.CylinderGeometry(0.18, 0.18, 0.04, 12);
    const gearMat = new THREE.MeshStandardMaterial({
      color: 0xB8860B,
      metalness: 0.95,
      roughness: 0.15,
    });
    const gearMesh = new THREE.Mesh(gearGeo, gearMat);
    gearMesh.rotation.x = Math.PI / 2;
    engGroup.add(gearMesh);
    // Piston rod
    const pistonGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.3, 6);
    const pistonMat = new THREE.MeshStandardMaterial({ color: 0x8B7355, metalness: 0.9, roughness: 0.2 });
    const piston = new THREE.Mesh(pistonGeo, pistonMat);
    piston.position.set(0.2, 0, 0);
    engGroup.add(piston);
    // Small bearing
    const bearingGeo = new THREE.TorusGeometry(0.06, 0.012, 8, 16);
    const bearingMat = new THREE.MeshStandardMaterial({ color: 0xA0906B, metalness: 0.85, roughness: 0.2 });
    const bearing = new THREE.Mesh(bearingGeo, bearingMat);
    bearing.position.set(-0.15, 0.1, 0);
    engGroup.add(bearing);
    artifactGroup.add(engGroup);
    fragments.push({
      mesh: engGroup,
      info: { title: "ENGINEERING", sublabels: ["MECHATRONICS", "ROBOTICS", "SYSTEMS"], color: "#B8860B" },
      orbitRadius: 2.55,
      orbitSpeed: 0.22,
      orbitAngle: Math.PI * 1.75,
      baseY: -0.2,
      raycastTarget: gearMesh,
    });
    raycastTargets.push(gearMesh);

    // 7. CIPHER — Dark engraved plate with glyph system
    const cipherGroup = new THREE.Group();
    const tabletGeo = new THREE.BoxGeometry(0.3, 0.3, 0.025);
    const tabletMat = new THREE.MeshStandardMaterial({
      color: 0x8B7B3A,
      metalness: 0.85,
      roughness: 0.25,
    });
    const tabletMesh = new THREE.Mesh(tabletGeo, tabletMat);
    cipherGroup.add(tabletMesh);
    // Engraved glyph lines on surface
    const glyphLineMat = new THREE.LineBasicMaterial({ color: 0xD4C87A, transparent: true, opacity: 0.6 });
    // Cross pattern suggesting cipher
    const glyphPatterns = [
      [[0, -0.08], [0, 0.08]],
      [[-0.08, 0], [0.08, 0]],
      [[-0.06, -0.06], [0.06, 0.06]],
      [[0.06, -0.06], [-0.06, 0.06]],
    ];
    glyphPatterns.forEach(([start, end]) => {
      const geo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(start[0], start[1], 0.015),
        new THREE.Vector3(end[0], end[1], 0.015),
      ]);
      const line = new THREE.Line(geo, glyphLineMat);
      cipherGroup.add(line);
    });
    artifactGroup.add(cipherGroup);
    fragments.push({
      mesh: cipherGroup,
      info: { title: "CIPHER", sublabels: ["GLYPH SYSTEM", "VISUAL LANGUAGE", "TYPOGRAPHY"], color: "#D4C87A" },
      orbitRadius: 2.2,
      orbitSpeed: -0.35,
      orbitAngle: Math.PI * 0.9,
      baseY: -0.5,
      raycastTarget: tabletMesh,
    });
    raycastTargets.push(tabletMesh);

    // === AMBIENT PARTICLES — sparse, gallery dust ===
    const particleCount = 180;
    const particlePositions = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      const radius = 1.5 + Math.random() * 6;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(Math.random() * 2 - 1);
      particlePositions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
      particlePositions[i * 3 + 1] = (Math.random() - 0.5) * 5;
      particlePositions[i * 3 + 2] = radius * Math.cos(phi);
    }
    const particleGeo = new THREE.BufferGeometry();
    particleGeo.setAttribute("position", new THREE.BufferAttribute(particlePositions, 3));
    const particleMat = new THREE.PointsMaterial({
      color: 0xE8E5DD,
      size: 0.02,
      transparent: true,
      opacity: 0.3,
      blending: THREE.AdditiveBlending,
    });
    const particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    // === MOUSE TRACKING ===
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2(-999, -999);
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;

    const onMouseMove = (e: MouseEvent) => {
      const rect = container.getBoundingClientRect();
      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
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

    // === ANIMATION LOOP ===
    let animId: number;
    const clock = new THREE.Clock();
    let hoveredObj: FragmentEntry | null = null;

    const animate = () => {
      const delta = clock.getDelta();
      const time = clock.getElapsedTime();

      // Smooth mouse lerp — restrained
      targetX += (mouseX * 0.3 - targetX) * 0.04;
      targetY += (mouseY * 0.2 - targetY) * 0.04;

      // Artifact group rotation — subtle, museum-quality drift
      artifactGroup.rotation.y = targetX + time * 0.06;
      artifactGroup.rotation.x = -targetY * 0.6 + Math.sin(time * 0.3) * 0.02;
      artifactGroup.position.y = Math.sin(time * 0.5) * 0.08;

      // Core rotation — very slow
      coreMesh.rotation.y += delta * 0.08;
      coreMesh.rotation.x += delta * 0.04;

      // Inner core counter-rotation
      innerCore.rotation.z -= delta * 0.15;
      innerCore.rotation.x += delta * 0.05;

      // Structural frame — slight drift
      frameGroup.rotation.y += delta * 0.03;
      frameGroup.rotation.z += delta * 0.02;

      // Orbiting fragments
      fragments.forEach((frag) => {
        frag.orbitAngle += delta * frag.orbitSpeed;
        const x = Math.cos(frag.orbitAngle) * frag.orbitRadius;
        const z = Math.sin(frag.orbitAngle) * frag.orbitRadius;
        const y = frag.baseY + Math.sin(time * 0.7 + frag.orbitAngle) * 0.1;
        frag.mesh.position.set(x, y, z);
        frag.mesh.rotation.y += delta * 0.3;
        frag.mesh.rotation.x += delta * 0.15;
      });

      // Raycasting — hover detection
      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(raycastTargets, true);

      let newHovered: FragmentEntry | null = null;
      if (intersects.length > 0) {
        const hitMesh = intersects[0].object;
        newHovered = fragments.find(
          (f) => f.raycastTarget === hitMesh || f.mesh.children.includes(hitMesh)
        ) || null;
      }

      if (newHovered !== hoveredObj) {
        hoveredObj = newHovered;
        setHoveredFragment(newHovered ? newHovered.info : null);
      }

      // Particles — very slow rotation
      particles.rotation.y += delta * 0.008;

      renderer.render(scene, camera);
      animId = requestAnimationFrame(animate);
    };

    animate();

    // Cleanup
    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("resize", onResize);
      if (renderer.domElement && container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
      renderer.dispose();
    };
  }, []);

  return (
    <div className="w-full h-full relative select-none">
      <div
        ref={containerRef}
        className="w-full h-full relative cursor-grab active:cursor-grabbing"
        data-cursor="EXPLORE"
        onClick={() => sound.playArtifactResonance()}
      />

      {/* Fragment tooltip — minimal, editorial */}
      {hoveredFragment && (
        <div className="absolute bottom-8 right-8 max-w-[220px] p-5 rounded-lg bg-[#0B0B0C]/95 border border-[#F2F0EA]/10 backdrop-blur-xl font-mono text-xs space-y-2 pointer-events-none z-20">
          <h4
            className="text-sm font-display font-bold tracking-wider"
            style={{ color: hoveredFragment.color }}
          >
            {hoveredFragment.title}
          </h4>
          <div className="space-y-0.5">
            {hoveredFragment.sublabels.map((label) => (
              <p key={label} className="text-[10px] text-[#B8B6AF] tracking-[0.15em]">
                {label}
              </p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
