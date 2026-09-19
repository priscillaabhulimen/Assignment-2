#!/usr/bin/env python3
"""Game ending banner for successful escape."""

def game_ending() -> str:
    return """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                                 YOU SURVIVED                                   ║
║                                                                                ║
║                     The sun rises. You are free. You remember                  ║
║                            your name. You remember                             ║
║                         everything that came before.                           ║
║                                                                                ║
║                                   THE END                                      ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

if __name__ == "__main__":
    print(game_ending())
