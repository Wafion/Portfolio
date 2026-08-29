"use client";

import { useEffect, useRef } from "react";
import * as THREE from "three";

type Palette = Record<"steel" | "aluminium" | "brass" | "glass" | "emissive", THREE.Material>;

function buildCrystal() {
  const sides = 9;
  const levels = [
    { y: -1.6, radius: 0.08, depth: 0.08 },
    { y: -1.32, radius: 0.38, depth: 0.3 },
    { y: -0.82, radius: 0.66, depth: 0.55 },
    { y: -0.15, radius: 0.78, depth: 0.68 },
    { y: 0.52, radius: 0.7, depth: 0.61 },
    { y: 1.05, radius: 0.48, depth: 0.4 },
    { y: 1.42, radius: 0.22, depth: 0.2 },
    { y: 1.62, radius: 0.06, depth: 0.06 },
  ];
  const vertices: number[] = [];
  levels.forEach((level, levelIndex) => {
    for (let i = 0; i < sides; i += 1) {
      const angle = (i / sides) * Math.PI * 2 + levelIndex * 0.17;
      const jitter = 1 + Math.sin(i * 4.7 + levelIndex * 1.8) * 0.11;
      vertices.push(
        Math.cos(angle) * level.radius * jitter,
        level.y,
        Math.sin(angle) * level.depth * jitter,
      );
    }
  });
  const indices: number[] = [];
  for (let level = 0; level < levels.length - 1; level += 1) {
    for (let side = 0; side < sides; side += 1) {
      const a = level * sides + side;
      const b = level * sides + ((side + 1) % sides);
      const c = (level + 1) * sides + side;
      const d = (level + 1) * sides + ((side + 1) % sides);
      if ((level + side) % 2 === 0) indices.push(a, c, b, b, c, d);
      else indices.push(a, c, d, a, d, b);
    }
  }
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.Float32BufferAttribute(vertices, 3));
  geometry.setIndex(indices);
  geometry.computeVertexNormals();
  return { geometry, vertices, sides, levels };
}

function addStrut(parent: THREE.Object3D, start: THREE.Vector3, end: THREE.Vector3, material: THREE.Material, radius = 0.018) {
  const direction = end.clone().sub(start);
  const mesh = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, direction.length(), 8), material);
  mesh.position.copy(start).add(end).multiplyScalar(0.5);
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction.normalize());
  parent.add(mesh);
  return mesh;
}

function addBearing(parent: THREE.Object3D, position: THREE.Vector3, material: THREE.Material, radius = 0.12) {
  const housing = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, 0.12, 12), material);
  housing.position.copy(position);
  housing.rotation.x = Math.PI / 2;
  parent.add(housing);
  const bolt = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.3, radius * 0.3, 0.14, 8), material);
  bolt.position.copy(position);
  bolt.rotation.x = Math.PI / 2;
  parent.add(bolt);
}

export function IntersectionHeroCanvas() {
  const containerRef = useRef<HTMLDivElement>(null);
  const hoverRef = useRef(false);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100);
    camera.position.set(0, 0.04, 8.4);
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: "high-performance" });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    const palette: Palette = {
      steel: new THREE.MeshPhysicalMaterial({ color: 0x151719, metalness: 0.92, roughness: 0.26, clearcoat: 0.6 }),
      aluminium: new THREE.MeshPhysicalMaterial({ color: 0x8f979d, metalness: 0.88, roughness: 0.3 }),
      brass: new THREE.MeshPhysicalMaterial({ color: 0xb58c48, metalness: 0.9, roughness: 0.24 }),
      glass: new THREE.MeshPhysicalMaterial({ color: 0xbfd7e4, metalness: 0.12, roughness: 0.12, transmission: 0.48, transparent: true, opacity: 0.78, clearcoat: 1 }),
      emissive: new THREE.MeshBasicMaterial({ color: 0xd9e9ed, transparent: true, opacity: 0.74 }),
    };
    scene.add(new THREE.HemisphereLight(0xe8edf0, 0x0b0908, 1.7));
    const coolLight = new THREE.PointLight(0xd8ecf1, 13, 11);
    coolLight.position.set(2.4, 2.8, 4);
    scene.add(coolLight);
    const brassLight = new THREE.PointLight(0xc9954d, 8, 8);
    brassLight.position.set(-2.8, -1.8, 3);
    scene.add(brassLight);

    const artifact = new THREE.Group();
    artifact.rotation.order = "YXZ";
    scene.add(artifact);
    const inner = new THREE.Group();
    artifact.add(inner);

    const crystalData = buildCrystal();
    const crystal = new THREE.Mesh(crystalData.geometry, palette.glass);
    crystal.position.z = 0.14;
    inner.add(crystal);
    const crystalEdges = new THREE.LineSegments(new THREE.EdgesGeometry(crystalData.geometry, 12), new THREE.LineBasicMaterial({ color: 0xe7f1f3, transparent: true, opacity: 0.52 }));
    crystalEdges.position.copy(crystal.position);
    inner.add(crystalEdges);
    const energy = new THREE.Mesh(new THREE.OctahedronGeometry(0.18, 1), palette.emissive);
    energy.scale.set(0.55, 2.8, 0.55);
    energy.position.set(0.06, -0.04, 0.3);
    inner.add(energy);

    // A fitted triangular cage built from the crystal's actual vertices.
    const cage = new THREE.Group();
    inner.add(cage);
    const cageMaterial = new THREE.MeshPhysicalMaterial({ color: 0x5e6b71, metalness: 0.85, roughness: 0.25 });
    const selectedEdges = new Set<string>();
    const addCageEdge = (a: number, b: number) => {
      const key = a < b ? `${a}-${b}` : `${b}-${a}`;
      if (selectedEdges.has(key)) return;
      selectedEdges.add(key);
      const start = new THREE.Vector3(crystalData.vertices[a * 3], crystalData.vertices[a * 3 + 1], crystalData.vertices[a * 3 + 2] + 0.18);
      const end = new THREE.Vector3(crystalData.vertices[b * 3], crystalData.vertices[b * 3 + 1], crystalData.vertices[b * 3 + 2] + 0.18);
      addStrut(cage, start, end, cageMaterial, 0.014);
    };
    for (let level = 0; level < crystalData.levels.length - 1; level += 1) {
      for (let side = 0; side < crystalData.sides; side += 1) {
        const a = level * crystalData.sides + side;
        const b = level * crystalData.sides + ((side + 1) % crystalData.sides);
        const c = (level + 1) * crystalData.sides + side;
        if (side % 2 === 0 || level === 2 || level === 4) {
          addCageEdge(a, b);
          addCageEdge(a, c);
        }
      }
    }

    // Outer frame follows an engineered arch instead of two generic bars.
    const frame = new THREE.Group();
    artifact.add(frame);
    const frameCurves = [-1, 1].map((side) => new THREE.CatmullRomCurve3([
      new THREE.Vector3(side * 0.98, -2.05, -0.12),
      new THREE.Vector3(side * 1.05, -0.85, -0.12),
      new THREE.Vector3(side * 1.02, 0.82, -0.12),
      new THREE.Vector3(side * 0.82, 1.82, -0.12),
      new THREE.Vector3(0, 2.18, -0.12),
    ]));
    frameCurves.forEach((curve) => frame.add(new THREE.Mesh(new THREE.TubeGeometry(curve, 28, 0.055, 8, false), palette.steel)));
    addStrut(frame, new THREE.Vector3(-0.98, -2.05, -0.12), new THREE.Vector3(0.98, -2.05, -0.12), palette.aluminium, 0.045);
    addStrut(frame, new THREE.Vector3(-0.12, 2.17, -0.12), new THREE.Vector3(0.12, 2.17, -0.12), palette.brass, 0.05);

    // Three orbital systems with different orientations, mounts, and bearing housings.
    const orbitalSystems: THREE.Group[] = [];
    const orbitalSpecs = [
      { radius: 1.22, tilt: 0.18, roll: -0.08, material: palette.aluminium },
      { radius: 1.55, tilt: -0.56, roll: 0.3, material: palette.brass },
      { radius: 1.92, tilt: 1.12, roll: -0.18, material: palette.steel },
    ];
    orbitalSpecs.forEach((spec, index) => {
      const orbit = new THREE.Group();
      orbit.rotation.set(spec.tilt, index * 0.16, spec.roll);
      const ring = new THREE.Mesh(new THREE.TorusGeometry(spec.radius, index === 1 ? 0.055 : index === 2 ? 0.035 : 0.025, 10, 96), spec.material);
      orbit.add(ring);
      [0, Math.PI].forEach((angle) => {
        const mount = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.12, 0.16), palette.steel);
        mount.position.set(Math.cos(angle) * spec.radius, Math.sin(angle) * spec.radius, 0);
        mount.rotation.z = angle;
        orbit.add(mount);
        addBearing(orbit, mount.position.clone().setZ(0.07), palette.brass, 0.08);
      });
      artifact.add(orbit);
      orbitalSystems.push(orbit);
    });

    // Right-side film aperture: housing, inner ring, blades, and a mounting arm.
    const aperture = new THREE.Group();
    aperture.position.set(1.42, -0.12, 0.42);
    aperture.rotation.y = -0.28;
    artifact.add(aperture);
    aperture.add(new THREE.Mesh(new THREE.CylinderGeometry(0.68, 0.68, 0.16, 32), palette.steel));
    const apertureRing = new THREE.Mesh(new THREE.TorusGeometry(0.55, 0.07, 10, 64), palette.aluminium);
    apertureRing.position.z = 0.11;
    aperture.add(apertureRing);
    const blades = new THREE.Group();
    blades.position.z = 0.15;
    aperture.add(blades);
    for (let i = 0; i < 7; i += 1) {
      const blade = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.075, 0.025), palette.brass);
      blade.position.set(0.17, 0, 0);
      blade.rotation.z = (i / 7) * Math.PI * 2;
      blades.add(blade);
    }
    const opening = new THREE.Mesh(new THREE.CylinderGeometry(0.27, 0.27, 0.04, 32), palette.steel);
    opening.position.z = 0.18;
    aperture.add(opening);
    addStrut(artifact, new THREE.Vector3(0.95, -0.2, 0.05), new THREE.Vector3(1.12, -0.12, 0.3), palette.steel, 0.06);
    addBearing(artifact, new THREE.Vector3(0.96, -0.2, 0.08), palette.brass, 0.12);

    // Lower engineering assembly: connecting rods, joints, and a small gear.
    const lower = new THREE.Group();
    artifact.add(lower);
    const crank = new THREE.Mesh(new THREE.TorusGeometry(0.32, 0.045, 8, 32), palette.brass);
    crank.position.set(0, -1.42, 0.24);
    crank.rotation.x = Math.PI / 2;
    lower.add(crank);
    const rod = addStrut(lower, new THREE.Vector3(-0.34, -1.34, 0.22), new THREE.Vector3(-0.72, -1.76, 0.16), palette.aluminium, 0.035);
    const rodJoint = new THREE.Mesh(new THREE.SphereGeometry(0.09, 12, 8), palette.brass);
    rodJoint.position.copy(rod.position).add(new THREE.Vector3(-0.22, -0.18, 0));
    lower.add(rodJoint);
    addBearing(lower, new THREE.Vector3(-0.72, -1.76, 0.16), palette.steel, 0.12);

    // Small geometry module and engraved plate integrated into the lower orbit.
    const geometryModule = new THREE.Mesh(new THREE.DodecahedronGeometry(0.25, 1), palette.aluminium);
    geometryModule.position.set(-1.28, -1.03, 0.2);
    geometryModule.scale.set(1, 0.72, 0.72);
    artifact.add(geometryModule);
    const plate = new THREE.Mesh(new THREE.BoxGeometry(0.36, 0.5, 0.035), palette.brass);
    plate.position.set(0.72, -1.34, 0.38);
    plate.rotation.z = -0.2;
    artifact.add(plate);
    const engraving = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(0.2, 0.3, 0.01)), new THREE.LineBasicMaterial({ color: 0xf0d9a2, transparent: true, opacity: 0.72 }));
    engraving.position.set(0.72, -1.34, 0.41);
    engraving.rotation.z = -0.2;
    artifact.add(engraving);

    const fragments = new THREE.Points(new THREE.BufferGeometry(), new THREE.PointsMaterial({ color: 0xf0f7f8, size: 0.035, transparent: true, opacity: 0.7 }));
    const fragmentPositions = new Float32Array(32 * 3);
    for (let i = 0; i < 32; i += 1) {
      fragmentPositions[i * 3] = (Math.random() - 0.5) * 0.8;
      fragmentPositions[i * 3 + 1] = (Math.random() - 0.5) * 2.6;
      fragmentPositions[i * 3 + 2] = 0.3 + Math.random() * 0.18;
    }
    fragments.geometry.setAttribute("position", new THREE.BufferAttribute(fragmentPositions, 3));
    inner.add(fragments);

    let pointerX = 0;
    let pointerY = 0;
    const onPointerMove = (event: PointerEvent) => {
      const rect = container.getBoundingClientRect();
      pointerX = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
      pointerY = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
    };
    const resize = () => {
      const width = container.clientWidth;
      const height = Math.max(container.clientHeight, 1);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height, false);
    };
    container.addEventListener("pointermove", onPointerMove);
    resize();
    window.addEventListener("resize", resize);

    const clock = new THREE.Clock();
    let frameId = 0;
    const render = () => {
      const time = clock.getElapsedTime();
      artifact.rotation.y += (pointerX * 0.12 + time * 0.018 - artifact.rotation.y) * 0.025;
      artifact.rotation.x += (pointerY * -0.09 - artifact.rotation.x) * 0.025;
      inner.rotation.y = time * 0.04;
      inner.position.y = Math.sin(time * 0.9) * 0.035;
      energy.scale.y = 2.8 + Math.sin(time * 1.5) * 0.16;
      orbitalSystems[0].rotation.z += 0.0018;
      orbitalSystems[1].rotation.z -= 0.0012;
      orbitalSystems[2].rotation.z += 0.0008;
      aperture.rotation.z += hoverRef.current ? 0.009 : 0.0025;
      blades.rotation.z += hoverRef.current ? 0.012 : 0.002;
      fragments.rotation.y = time * 0.08;
      renderer.render(scene, camera);
      frameId = requestAnimationFrame(render);
    };
    render();

    return () => {
      cancelAnimationFrame(frameId);
      window.removeEventListener("resize", resize);
      container.removeEventListener("pointermove", onPointerMove);
      renderer.dispose();
      scene.traverse((object) => {
        const item = object as THREE.Mesh | THREE.LineSegments | THREE.Points;
        if (item.geometry) item.geometry.dispose();
        if (Array.isArray(item.material)) item.material.forEach((material) => material.dispose());
        else if (item.material) item.material.dispose();
      });
      if (container.contains(renderer.domElement)) container.removeChild(renderer.domElement);
    };
  }, []);

  return (
    <div
      ref={containerRef}
      onPointerEnter={() => { hoverRef.current = true; }}
      onPointerLeave={() => { hoverRef.current = false; }}
      className="archive-core-canvas h-full w-full"
      aria-label="Interactive Intersection precision kinetic sculpture"
      data-cursor="FILM / APERTURE"
    />
  );
}
