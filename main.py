#!/usr/bin/env python3
"""Luca — invoice assistant.

Auth: reuses your Claude Code login — no API key needed. Make sure the
`claude` command works in this terminal first.
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from model import InvoiceModel  # noqa: E402
from view import CliView  # noqa: E402


def _intro() -> None:
    G = "\033[92m"   # bright green
    D = "\033[2m"    # dim
    R = "\033[0m"    # reset
    art = [
        "  ██╗     ██╗   ██╗  ██████╗  █████╗",
        "  ██║     ██║   ██║ ██╔════╝ ██╔══██╗",
        "  ██║     ██║   ██║ ██║      ███████║",
        "  ██║     ██║   ██║ ██║      ██╔══██║",
        "  ███████╗╚██████╔╝ ╚██████╗ ██║  ██║",
        "  ╚══════╝ ╚═════╝   ╚═════╝ ╚═╝  ╚═╝",
    ]
    print()
    for line in art:
        print(G + line + R)
    print(D + "\n        your accounting assistant\n" + R)


def _pick_mode() -> str | None:
    print("  1) Chat  — ask questions and book invoices")
    print("  2) Test  — check the skill against expected answers")
    print("  Q) Quit")
    while True:
        try:
            choice = input("\nSelect [1/2/Q]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if choice in ("q", ""):
            return None
        if choice == "1":
            return "chat"
        if choice == "2":
            return "test"
        print("  ! not a valid choice, try again")


def main() -> None:
    _intro()
    model = InvoiceModel()
    mode = _pick_mode()
    if mode == "chat":
        from chat_controller import ChatController
        asyncio.run(ChatController(model).run())
    elif mode == "test":
        from controller import BookingController
        asyncio.run(BookingController(model, CliView()).run())


if __name__ == "__main__":
    main()
