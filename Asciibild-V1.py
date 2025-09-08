import argparse
from PIL import Image

# Changable ASCII characters
ASCII_CHARS = " .:-=+*#%@"

def image_to_ascii(path, width=100, invert=False, charset=ASCII_CHARS, aspect_ratio=0.5):
    img = Image.open(path).convert("L")

    # Change image size
    w, h = img.size
    new_height = max(1, int(h / w * width * aspect_ratio))
    img = img.resize((width, new_height))

    # Optional invert colors
    pixels = list(img.getdata())
    if invert:
        pixels = [255 - p for p in pixels]

    scale = len(charset) - 1
    chars = [charset[int(p / 255 * scale)] for p in pixels]

    lines = ["".join(chars[i:i + width]) for i in range(0, len(chars), width)]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Bild -> ASCII Art")
    parser.add_argument("image", help="Pfad zum Bild (z.B. foto.jpg)")
    parser.add_argument("-w", "--width", type=int, default=100, help="Breite in Zeichen")
    parser.add_argument("--invert", action="store_true", help="Helligkeit invertieren")
    parser.add_argument("--charset", default=None, help="Zeichen von hell nach dunkel")
    parser.add_argument("--aspect", type=float, default=0.5, help="Zeichen-Aspect-Ratio (0.43–0.6)")
    parser.add_argument("-o", "--output", help="Ausgabedatei (txt). Wenn nicht gesetzt: Konsole")
    args = parser.parse_args()

    charset = args.charset or ASCII_CHARS
    art = image_to_ascii(
        args.image,
        width=args.width,
        invert=args.invert,
        charset=charset,
        aspect_ratio=args.aspect
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(art)
    else:
        print(art)

if __name__ == "__main__":
    main()


#   ___   _    _ ____ ___ _    _ __   _  ___
#  / _ \ | |  | |__  /  _| |  | |   \| |/  _|
# / / \ \| |  | | / /| |_| |  | | |\ \ |  /
# \ \_/ /| |__| |/ /_| |_| |_ | | | \  |  \_
#  \___/ |____|_|____|___|_|_||_|_|  \_|\___|
