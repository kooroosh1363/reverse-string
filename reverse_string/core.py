"""Pure string-reversal functions.

The default implementation uses Python slicing because it is the clearest
idiomatic solution. A loop implementation is kept as an educational contrast.
"""

from __future__ import annotations

import re
from typing import Literal

Mode = Literal["characters", "words"]
Algorithm = Literal["slice", "loop"]


def _require_text(text: str) -> None:
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")


def reverse_characters(text: str) -> str:
    """Return *text* in reverse Unicode code-point order.

    Time complexity: O(n)
    Space complexity: O(n) for the returned string
    """
    _require_text(text)
    return text[::-1]


def reverse_characters_loop(text: str) -> str:
    """Return *text* reversed with an explicit backwards loop.

    This exists to make the algorithm visible for learning and comparison.
    It intentionally builds a list and joins once, avoiding quadratic
    repeated string concatenation.
    """
    _require_text(text)
    characters: list[str] = []

    for index in range(len(text) - 1, -1, -1):
        characters.append(text[index])

    return "".join(characters)


def reverse_words(text: str) -> str:
    """Reverse whitespace-delimited token order while preserving whitespace.

    Punctuation remains attached to the token it was written with.

    Example:
        "one   two three" -> "three   two one"
    """
    _require_text(text)

    parts = re.split(r"(\s+)", text)
    token_indexes = [
        index for index, part in enumerate(parts) if part and not part.isspace()
    ]
    reversed_tokens = [parts[index] for index in reversed(token_indexes)]

    for index, token in zip(token_indexes, reversed_tokens, strict=True):
        parts[index] = token

    return "".join(parts)


def reverse_text(
    text: str,
    *,
    mode: Mode = "characters",
    algorithm: Algorithm = "slice",
) -> str:
    """Reverse text according to the selected mode and algorithm."""
    _require_text(text)

    if mode == "characters":
        if algorithm == "slice":
            return reverse_characters(text)
        if algorithm == "loop":
            return reverse_characters_loop(text)
        raise ValueError(f"unsupported character algorithm: {algorithm}")

    if mode == "words":
        if algorithm != "slice":
            raise ValueError("word mode does not use the character loop algorithm")
        return reverse_words(text)

    raise ValueError(f"unsupported reversal mode: {mode}")
