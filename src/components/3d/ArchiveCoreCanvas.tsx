"use client";

import { useEffect, useRef } from "react";
import * as THREE from "three";

export function ArchiveCoreCanvas() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
    camera.position.set(0, 0.25, 8.2);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    const root = new THREE.Group();
    scene.add(root);
    const core = new THREE.Group();
    root.add(core);

    scene.add(new THREE.HemisphereLight(0xdde7ff, 0x120d0c, 1.6));
    const cyan = new THREE.PointLight(0x6dd9e8, 18, 12);
    cyan.position.set(3, 2, 4);
    scene.add(cyan);
    const ember = new THREE.PointLight(0xe2a75b, 10, 10);
    ember.position.set(-3, -2, 2);
    scene.add(ember);

    const materials = [
      new THREE.MeshPhysicalMaterial({ color: 0x151a24, metalness: 0.82, roughness: 0.22, clearcoat: 0.8 }),
      new THREE.MeshPhysicalMaterial({ color: 0x2a2630, metalness: 0.7, roughness: 0.3, clearcoat: 0.5 }),
      new THREE.MeshBasicMaterial({ color: 0x8de4e8, transparent: true, opacity: 0.8 }),
    ];

    const slabGeo = new THREE.BoxGeometry(2.25, 0.16, 1.38);
    const slabAngles = [-0.24, 0.08, 0.32, -0.08, 0.2];
    slabAngles.forEach((angle, index) => {
      const slab = new THREE.Mesh(slabGeo, materials[index % 2]);
      slab.position.set(Math.sin(index * 1.6) * 0.32, (index - 2) * 0.58, Math.cos(index * 1.2) * 0.22);
      slab.rotation.z = angle;
      slab.rotation.y = index % 2 ? 0.14 : -0.1;
      core.add(slab);
    });

    const prism = new THREE.Mesh(new THREE.OctahedronGeometry(0.72, 1), materials[0]);
    prism.scale.set(0.74, 1.42, 0.74);
    prism.rotation.z = Math.PI / 4;
    core.add(prism);

    const spine = new THREE.Mesh(new THREE.BoxGeometry(0.06, 3.5, 0.06), materials[2]);
    spine.position.z = 0.48;
    core.add(spine);

    const orbit = new THREE.Group();
    orbit.rotation.set(0.58, -0.25, 0.18);
    root.add(orbit);
    const orbitGeo = new THREE.TorusGeometry(2.05, 0.012, 8, 96);
    const orbitLine = new THREE.Mesh(orbitGeo, new THREE.MeshBasicMaterial({ color: 0xb3d8d3, transparent: true, opacity: 0.5 }));
    orbit.add(orbitLine);
    const markerGeo = new THREE.BoxGeometry(0.1, 0.1, 0.28);
    for (let i = 0; i < 8; i += 1) {
      const marker = new THREE.Mesh(markerGeo, materials[i % 3 === 0 ? 2 : 1]);
      const theta = (i / 8) * Math.PI * 2;
      marker.position.set(Math.cos(theta) * 2.05, Math.sin(theta) * 2.05, 0);
      marker.rotation.z = theta;
      orbit.add(marker);
    }

    const particlePositions = new Float32Array(180 * 3);
    for (let i = 0; i < 180; i += 1) {
      const theta = Math.random() * Math.PI * 2;
      const radius = 2.8 + Math.random() * 2.8;
      particlePositions[i * 3] = Math.cos(theta) * radius;
      particlePositions[i * 3 + 1] = (Math.random() - 0.5) * 5.5;
      particlePositions[i * 3 + 2] = (Math.random() - 0.5) * 2.5;
    }
    const particles = new THREE.Points(
      new THREE.BufferGeometry().setFromPoints(Array.from({ length: 180 }, (_, i) => new THREE.Vector3(particlePositions[i * 3], particlePositions[i * 3 + 1], particlePositions[i * 3 + 2]))),
      new THREE.PointsMaterial({ color: 0xb6d6d2, size: 0.035, transparent: true, opacity: 0.62 }),
    );
    scene.add(particles);

    let width = 0;
    let height = 0;
    const resize = () => {
      width = container.clientWidth;
      height = container.clientHeight;
      camera.aspect = width / Math.max(height, 1);
      camera.updateProjectionMatrix();
      renderer.setSize(width, height, false);
    };
    resize();
    window.addEventListener("resize", resize);

    let pointerX = 0;
    let pointerY = 0;
    const onPointerMove = (event: PointerEvent) => {
      const rect = container.getBoundingClientRect();
      pointerX = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
      pointerY = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
    };
    container.addEventListener("pointermove", onPointerMove);

    const clock = new THREE.Clock();
    let frame = 0;
    const render = () => {
      const t = clock.getElapsedTime();
      root.rotation.y += (pointerX * 0.3 + t * 0.08 - root.rotation.y) * 0.035;
      root.rotation.x += (pointerY * -0.16 - root.rotation.x) * 0.035;
      core.position.y = Math.sin(t * 1.1) * 0.08;
      orbit.rotation.z += 0.003;
      particles.rotation.y = t * 0.018;
      renderer.render(scene, camera);
      frame = requestAnimationFrame(render);
    };
    render();

    return () => {
      cancelAnimationFrame(frame);
      window.removeEventListener("resize", resize);
      container.removeEventListener("pointermove", onPointerMove);
      renderer.dispose();
      slabGeo.dispose();
      orbitGeo.dispose();
      markerGeo.dispose();
      materials.forEach((material) => material.dispose());
      scene.traverse((object) => {
        if (object instanceof THREE.Mesh && object.geometry !== slabGeo && object.geometry !== orbitGeo && object.geometry !== markerGeo) object.geometry.dispose();
      });
      if (container.contains(renderer.domElement)) container.removeChild(renderer.domElement);
    };
  }, []);

  return <div ref={containerRef} className="archive-core-canvas h-full w-full" aria-label="Interactive suspended archive core" />;
}
