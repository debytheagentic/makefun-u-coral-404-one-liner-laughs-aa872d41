import os

# Final: same twist, 12 bytes tighter (she hugs me = I am the mistake).
ENTRY = "I told my wife to embrace her mistakes. She hugged me."


def main():
    text = ENTRY
    n = len(text)
    print(f"LEN={n}")
    if n < 1 or n > 200 or not text.strip():
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
