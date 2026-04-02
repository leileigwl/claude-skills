#!/usr/bin/env python3
"""Generate seamless texture tiles for PPT backgrounds."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

OUTPUT_DIR = Path(__file__).resolve().parent / "textures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SIZE = 1024  # texture resolution; power of two keeps tiling crisp


@dataclass
class TextureSpec:
    filename: str
    palette: list[tuple[float, tuple[int, int, int]]]
    seed: int
    wave_layers: int
    contrast: float
    detail: float
    overlay_strength: float


def _wave_field(size: int, layers: int, seed: int, detail: float) -> np.ndarray:
    """Create a seamless wave-based noise field."""
    rng = random.Random(seed)
    x = np.linspace(0.0, 2.0 * math.pi, size, endpoint=False)
    y = np.linspace(0.0, 2.0 * math.pi, size, endpoint=False)
    xx, yy = np.meshgrid(x, y)

    field = np.zeros((size, size), dtype=np.float32)

    for _ in range(layers):
        fx = rng.randint(1, 7) * rng.choice((-1, 1))
        fy = rng.randint(1, 7) * rng.choice((-1, 1))
        phase = rng.uniform(0.0, 2.0 * math.pi)
        amplitude = rng.uniform(0.25, 1.0)
        tilt = rng.uniform(-0.7, 0.7)

        base = np.sin(fx * xx + fy * yy + phase)
        harmonic = np.sin((fx * tilt) * xx + (fy * (1 - tilt)) * yy + phase * 1.5)
        field += amplitude * (0.7 * base + 0.3 * harmonic)

    # radial modifier adds a sense of volume without breaking tiling
    center_shift = math.pi
    radius = np.sqrt((xx - center_shift) ** 2 + (yy - center_shift) ** 2)
    field += 0.35 * np.cos(radius * detail)

    return field


def _micro_overlay(size: int, seed: int) -> np.ndarray:
    """High-frequency overlay that stays tileable."""
    rng = random.Random(seed)
    x = np.linspace(0.0, 2.0 * math.pi, size, endpoint=False)
    y = np.linspace(0.0, 2.0 * math.pi, size, endpoint=False)
    xx, yy = np.meshgrid(x, y)

    freq = rng.randint(6, 12)
    angled = np.sin(freq * (xx * math.cos(math.pi / 4) + yy * math.sin(math.pi / 4)))
    cross = np.sin(freq * 0.6 * xx) * np.sin(freq * 0.6 * yy)
    return 0.5 * angled + 0.5 * cross


def _normalize(field: np.ndarray, contrast: float) -> np.ndarray:
    field = field - field.mean()
    max_abs = np.max(np.abs(field))
    if max_abs > 0:
        field = field / max_abs
    field = np.tanh(field * contrast)
    field = (field - field.min()) / (field.max() - field.min())
    return field


def _apply_palette(values: np.ndarray, palette: list[tuple[float, tuple[int, int, int]]]) -> np.ndarray:
    stops, colors = zip(*palette)
    stops_arr = np.array(stops)
    colors_arr = np.array(colors, dtype=np.float32)

    rgb = np.empty(values.shape + (3,), dtype=np.float32)
    for channel in range(3):
        rgb[..., channel] = np.interp(values, stops_arr, colors_arr[:, channel])
    return rgb.astype(np.uint8)


def render_texture(spec: TextureSpec) -> Path:
    field = _wave_field(SIZE, spec.wave_layers, spec.seed, spec.detail)
    overlay = _micro_overlay(SIZE, spec.seed + 17)
    combined = field + spec.overlay_strength * overlay
    normalized = _normalize(combined, spec.contrast)
    rgb = _apply_palette(normalized, spec.palette)

    image = Image.fromarray(rgb, mode="RGB")
    output_path = OUTPUT_DIR / spec.filename
    image.save(output_path)
    return output_path


def main() -> None:
    textures = [
        TextureSpec(
            filename="texture_light.png",
            palette=[
                (0.0, (233, 238, 244)),
                (0.4, (209, 222, 236)),
                (0.75, (188, 208, 227)),
                (1.0, (170, 194, 216)),
            ],
            seed=2024,
            wave_layers=9,
            contrast=1.8,
            detail=1.6,
            overlay_strength=0.22,
        ),
        TextureSpec(
            filename="texture_dark.png",
            palette=[
                (0.0, (14, 20, 30)),
                (0.45, (28, 42, 63)),
                (0.8, (54, 77, 106)),
                (1.0, (92, 121, 148)),
            ],
            seed=4096,
            wave_layers=11,
            contrast=2.4,
            detail=2.2,
            overlay_strength=0.32,
        ),
    ]

    for spec in textures:
        path = render_texture(spec)
        print(f"Saved {path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
