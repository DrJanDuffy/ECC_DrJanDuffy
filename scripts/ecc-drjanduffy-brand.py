#!/usr/bin/env python3
"""Insert the ECC_DrJanDuffy banner into README.md if missing."""
from pathlib import Path

README = Path("README.md")
BANNER = (
    "> **ECC_DrJanDuffy** is Dr. Jan Duffy's working copy of "
    "[ECC](https://github.com/affaan-m/ECC) (MIT). See [`SOURCE.md`](SOURCE.md). "
    "Official installs still come from the upstream project, not this fork.\n\n"
)

def main() -> None:
    text = README.read_text(encoding="utf-8")
    if "ECC_DrJanDuffy" in text[:900]:
        print("README already branded")
        return
    needle = "</p>\n\n"
    idx = text.find(needle)
    if idx == -1:
        raise SystemExit("README hero close tag not found")
    insert_at = idx + len(needle)
    README.write_text(text[:insert_at] + BANNER + text[insert_at:], encoding="utf-8")
    print("Branded README.md")

if __name__ == "__main__":
    main()
