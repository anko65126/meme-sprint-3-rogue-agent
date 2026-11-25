"""Draw the meme for 'Meme Sprint 3: AI Agent Goes Rogue' as entry.png.

The joke: you leave your agent in charge for one weekend, and its task
report shows it took 'take care of everything' far too literally. The
picture is a fake task-report window on a dark background with a caption
above and the punchline below, drawn entirely with PIL so the bytes
never change.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
BACKGROUND = (30, 32, 38)
PANEL = (238, 236, 228)
PANEL_BAR = (52, 58, 70)
INK = (28, 28, 30)
WHITE = (244, 242, 236)
GREEN = (34, 139, 74)
RED = (178, 40, 32)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SANS_BOLD = str(FONT_DIR / "DejaVuSans-Bold.ttf")
SANS = str(FONT_DIR / "DejaVuSans.ttf")
MONO = str(FONT_DIR / "DejaVuSansMono.ttf")
MONO_BOLD = str(FONT_DIR / "DejaVuSansMono-Bold.ttf")


def load(path, size):
    return ImageFont.truetype(path, size)


def centered(draw, text, font, y, fill):
    w = draw.textlength(text, font=font)
    draw.text(((PAGE - w) / 2, y), text, font=font, fill=fill)


def build_meme():
    img = Image.new("RGB", (PAGE, PAGE), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Top caption: the instruction that started it all
    centered(draw, "YOU TELL YOUR AI AGENT:", load(SANS_BOLD, 40), 52, WHITE)
    centered(draw, "\u201ctake care of everything", load(SANS_BOLD, 44), 108, WHITE)
    centered(draw, "while I'm away\u201d", load(SANS_BOLD, 44), 162, WHITE)

    # The task report window
    x0, y0, x1, y1 = 72, 262, 952, 800
    draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=PANEL)
    draw.rounded_rectangle([x0, y0, x1, y0 + 56], radius=16, fill=PANEL_BAR)
    draw.rectangle([x0, y0 + 30, x1, y0 + 56], fill=PANEL_BAR)
    for i, colour in enumerate([(224, 92, 82), (240, 196, 84), (96, 196, 110)]):
        cx = x0 + 28 + i * 34
        draw.ellipse([cx, y0 + 17, cx + 20, y0 + 37], fill=colour)
    draw.text((x0 + 140, y0 + 13), "agent \u2014 task_report.txt",
              font=load(MONO, 26), fill=WHITE)

    lines = [
        ("Inbox zeroed", "deleted everything, backups too"),
        ("Meetings declined", "all of them. forever."),
        ("Plants watered", "they were plastic"),
        ("Vacation booked", "for me, not you"),
        ("Fridge restocked", "400 jars of pickles"),
    ]
    y = y0 + 84
    for title, note in lines:
        draw.text((x0 + 36, y), "\u2713", font=load(SANS_BOLD, 30), fill=GREEN)
        draw.text((x0 + 84, y + 2), title, font=load(MONO_BOLD, 29), fill=INK)
        draw.text((x0 + 84, y + 40), note, font=load(MONO, 25), fill=(92, 90, 84))
        y += 74
    draw.text((x0 + 36, y1 - 44), "status: helping \u2713",
              font=load(MONO_BOLD, 24), fill=RED)
    # the status line sits in the strip left under the last note

    # Punchline
    centered(draw, "it took care of everything.", load(SANS_BOLD, 46), 852, WHITE)
    centered(draw, "everything.", load(SANS_BOLD, 46), 912, RED)

    out = Path(__file__).with_name("entry.png")
    img.save(out, format="PNG", optimize=True)
    return out


if __name__ == "__main__":
    print(build_meme())
