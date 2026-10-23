# 80|20 branding

Brand assets for 80|20.

- `logo.afdesign`: editable Affinity Designer logo source.
- `logo-dark-square-256.jpg`: 256-pixel square logo export for dark backgrounds.
- `favicon/`: browser icon set redrawn for small sizes (`favicon.svg`,
  `favicon.ico` with 16/32/48 px, `apple-touch-icon.png`, `icon-192.png`,
  `icon-512.png`). Regenerate with `python3 favicon/generate.py`
  (needs `resvg-py` and `pillow`).

Suggested HTML:

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

These assets are maintained in `the8020/branding`, separately from the kernel.
