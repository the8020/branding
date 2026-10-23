"""Generate the 80|20 browser icon set into this folder.

Requires: pip install resvg-py pillow
Digits are drawn as geometric strokes, so no font is embedded or licensed.
"""

import io
from pathlib import Path

import resvg_py
from PIL import Image

YELLOW, WHITE, BACKGROUND = "#F5C04A", "#FFFFFF", "#0E0F14"
OUT = Path(__file__).parent


def stroke(color, width):
    return f'fill="none" stroke="{color}" stroke-width="{width}"'


def zero(x, y, w, h, color, sw):
    i = sw / 2
    return (f'<rect x="{x + i}" y="{y + i}" width="{w - sw}" height="{h - sw}" '
            f'rx="{(w - sw) / 2}" {stroke(color, sw)}/>')


def eight(x, y, w, h, color, sw):
    i, mid = sw / 2, y + h * 0.46
    tw = w * 0.84
    tx = x + (w - tw) / 2
    top = (f'<rect x="{tx + i}" y="{y + i}" width="{tw - sw}" height="{mid - y}" '
           f'rx="{min((tw - sw) / 2, (mid - y) / 2)}" {stroke(color, sw)}/>')
    bottom = (f'<rect x="{x + i}" y="{mid + i}" width="{w - sw}" height="{y + h - mid - sw}" '
              f'rx="{min((w - sw) / 2, (y + h - mid - sw) / 2)}" {stroke(color, sw)}/>')
    return top + bottom


def two(x, y, w, h, color, sw):
    i = sw / 2
    r = (w - sw) / 2
    cy = y + i + r
    return (f'<path d="M{x + i} {cy} A{r} {r} 0 0 1 {x + w - i} {cy} '
            f'C{x + w - i} {cy + r * 0.8} {x + w - i - 2} {cy + r * 1.1} {x + w * 0.55} {y + h * 0.68} '
            f'L{x + i} {y + h - i} H{x + w}" {stroke(color, sw)} stroke-linejoin="round"/>')


def svg(radius=14, sw=4.4, dw=17, gap=4.5, dh=23):
    x = (64 - (2 * dw + gap)) / 2
    top, bottom = 4, 64 - 4 - dh
    return "".join([
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">',
        f'<rect width="64" height="64" rx="{radius}" fill="{BACKGROUND}"/>',
        eight(x, top, dw, dh, YELLOW, sw),
        zero(x + dw + gap, top, dw, dh, YELLOW, sw),
        f'<rect x="{x - 3}" y="30" width="{2 * dw + gap + 6}" height="4" rx="1" fill="{WHITE}"/>',
        two(x, bottom, dw, dh, WHITE, sw),
        zero(x + dw + gap, bottom, dw, dh, WHITE, sw),
        "</svg>",
    ])


def png(source, size):
    data = bytes(resvg_py.svg_to_bytes(svg_string=source, width=size, height=size))
    return Image.open(io.BytesIO(data)).convert("RGBA")


rounded = svg()
(OUT / "favicon.svg").write_text(rounded + "\n")
small = [png(rounded, size) for size in (16, 32, 48)]
small[2].save(OUT / "favicon.ico", format="ICO",
              sizes=[(16, 16), (32, 32), (48, 48)], append_images=small[:2])
for size in (192, 512):
    png(rounded, size).save(OUT / f"icon-{size}.png")
# iOS rounds the corners itself and shows transparency as black.
png(svg(radius=0), 180).convert("RGB").save(OUT / "apple-touch-icon.png")
