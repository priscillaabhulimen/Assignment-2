#!/usr/bin/env python3
"""Self-contained: prints a close, slightly blurred ghost as 24-bit ANSI art (55 cols x 25 rows)."""
import base64, sys, zlib

_DATA = (
    "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"
)

def ghost_close() -> str:
    return zlib.decompress(base64.b64decode(_DATA)).decode("utf-8")

if __name__ == "__main__":
    sys.stdout.write(ghost_close())
