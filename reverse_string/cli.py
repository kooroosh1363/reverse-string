"""Command-line interface for the reverse-string lab."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from typing import TextIO

from .core import reverse_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="reverse-string",
        description="Reverse characters or whitespace-delimited words.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="text to reverse; omit it to use the interactive prompt",
    )
    parser.add_argument(
        "--mode",
        choices=("characters", "words"),
        default="characters",
        help="reverse individual code points or token order (default: characters)",
    )
    parser.add_argument(
        "--algorithm",
        choices=("slice", "loop"),
        default="slice",
        help="character reversal implementation (default: slice)",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="read the exact input stream from stdin instead of a positional value",
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    stdin: TextIO | None = None,
    stdout: TextIO | None = None,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    input_stream = stdin if stdin is not None else sys.stdin
    output_stream = stdout if stdout is not None else sys.stdout

    if args.stdin and args.text is not None:
        parser.error("provide either positional text or --stdin, not both")

    if args.mode == "words" and args.algorithm != "slice":
        parser.error("--algorithm loop is only available in character mode")

    if args.stdin:
        text = input_stream.read()
        append_newline = False
    elif args.text is not None:
        text = args.text
        append_newline = True
    else:
        output_stream.write("Text: ")
        output_stream.flush()
        text = input_stream.readline().rstrip("\r\n")
        append_newline = True

    result = reverse_text(text, mode=args.mode, algorithm=args.algorithm)
    output_stream.write(result)

    if append_newline and not result.endswith("\n"):
        output_stream.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
