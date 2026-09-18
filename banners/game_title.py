#!/usr/bin/env python3
"""Self-contained: prints "The Pale Girl" title as 24-bit ANSI art (80 cols x 16 rows)."""
import base64, sys, zlib

_DATA = (
    "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"
)

def game_title() -> str:
    return zlib.decompress(base64.b64decode(_DATA)).decode("utf-8")

if __name__ == "__main__":
    sys.stdout.write(game_title())
