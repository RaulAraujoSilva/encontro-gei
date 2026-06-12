# -*- coding: utf-8 -*-
"""
Gera a imagem de fundo do certificado Even3 (A4 paisagem, 2480x1754 px).
Layout: faixa navy no topo com logo do evento, título CERTIFICADO,
área central livre (texto + tags ficam no editor da Even3) e rodapé
com a faixa de logos das instituições realizadoras.

Saída: assets/certificado/fundo-certificado-gei.png (e .jpg)
Uso: python scripts/gerar_fundo_certificado.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, "assets", "certificado")

W, H = 2480, 1754  # A4 paisagem ~210dpi
NAVY = (9, 17, 54)
YELLOW = (245, 200, 66)
GREEN = (122, 199, 79)
WHITE = (255, 255, 255)
OFFWHITE = (250, 250, 252)
MUTED = (90, 96, 120)


def font(name, size):
    return ImageFont.truetype(os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name), size)


def paste_logo(canvas, path, center_x, center_y, max_w, max_h, invert=False):
    im = Image.open(path).convert("RGBA")
    if invert:  # logos brancos sobre transparente (ex.: TEP/PPGEP) viram navy
        r, g, b, a = im.split()
        from PIL import ImageOps
        solid = Image.new("RGBA", im.size, NAVY + (255,))
        im = Image.composite(solid, Image.new("RGBA", im.size, (0, 0, 0, 0)), a)
    ratio = min(max_w / im.width, max_h / im.height)
    im = im.resize((int(im.width * ratio), int(im.height * ratio)), Image.LANCZOS)
    canvas.paste(im, (int(center_x - im.width / 2), int(center_y - im.height / 2)), im)


img = Image.new("RGB", (W, H), OFFWHITE)
d = ImageDraw.Draw(img)

# moldura fina navy + filete amarelo
d.rectangle([40, 40, W - 40, H - 40], outline=NAVY, width=6)
d.rectangle([56, 56, W - 56, H - 56], outline=YELLOW, width=2)

# filete superior navy + amarelo
d.rectangle([46, 46, W - 46, 70], fill=NAVY)
d.rectangle([46, 70, W - 46, 78], fill=YELLOW)

# logo do evento (versão p/ fundo claro) no topo
paste_logo(img, os.path.join(BASE, "assets", "logo-fundo-branco.png"), W / 2, 240, 1320, 280)

# título
d.text((W / 2, 480), "CERTIFICADO", font=font("arialbd.ttf", 116), fill=NAVY, anchor="mm")
bbox = d.textbbox((W / 2, 480), "CERTIFICADO", font=font("arialbd.ttf", 116), anchor="mm")
d.rectangle([W / 2 - 160, bbox[3] + 18, W / 2 + 160, bbox[3] + 26], fill=GREEN)

# rodapé: linha + label + faixa de logos das realizadoras (sobre fundo branco)
FOOT_TOP = H - 420
d.rectangle([120, FOOT_TOP, W - 120, FOOT_TOP + 3], fill=(210, 213, 224))
d.text((W / 2, FOOT_TOP + 52), "REALIZAÇÃO", font=font("arialbd.ttf", 34), fill=MUTED, anchor="mm")

logos = [
    ("assets/logos/agenersa.png", 200, False),
    ("assets/logo-uff.png", 150, False),
    ("assets/logos/abar.png", 170, False),
    ("assets/logos/logo-eng-768x184.png", 120, True),
    ("assets/logos/labdge.png", 150, False),
    ("assets/logos/gigs-unicamp.jpg", 150, False),
]
slot_w = (W - 360) / len(logos)
cy = FOOT_TOP + 210
for i, (path, max_h, inv) in enumerate(logos):
    cx = 180 + slot_w * (i + 0.5)
    paste_logo(img, os.path.join(BASE, path), cx, cy, slot_w - 70, max_h, invert=inv)

# datas / local discretos na base
d.text((W / 2, H - 110), "08, 09 e 10 de julho de 2026 · Rio de Janeiro / Niterói, RJ · encontrogeig.org",
       font=font("arial.ttf", 34), fill=MUTED, anchor="mm")

os.makedirs(OUT_DIR, exist_ok=True)
png = os.path.join(OUT_DIR, "fundo-certificado-gei.png")
jpg = os.path.join(OUT_DIR, "fundo-certificado-gei.jpg")
img.save(png, optimize=True)
img.save(jpg, quality=90)
print("OK:", png)
print("OK:", jpg, f"({os.path.getsize(jpg)//1024} KB)")
