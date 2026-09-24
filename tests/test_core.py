from __future__ import annotations

import unittest

from reverse_string.core import (
    reverse_characters,
    reverse_characters_loop,
    reverse_text,
    reverse_words,
)


class CharacterReversalTests(unittest.TestCase):
    def test_reverses_basic_text(self) -> None:
        self.assertEqual("olleh", reverse_characters("hello"))

    def test_handles_empty_and_single_character_strings(self) -> None:
        self.assertEqual("", reverse_characters(""))
        self.assertEqual("A", reverse_characters("A"))

    def test_preserves_spaces_as_characters(self) -> None:
        self.assertEqual(" c b a ", reverse_characters(" a b c "))

    def test_handles_non_ascii_code_points(self) -> None:
        self.assertEqual("ابحرم", reverse_characters("مرحبا"))
        self.assertEqual("🙂A", reverse_characters("A🙂"))

    def test_loop_matches_slice_implementation(self) -> None:
        samples = ["", "a", "hello", " a b ", "مرحبا", "A🙂Z"]
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertEqual(
                    reverse_characters(sample),
                    reverse_characters_loop(sample),
                )

    def test_rejects_non_string_input(self) -> None:
        with self.assertRaises(TypeError):
            reverse_characters(123)  # type: ignore[arg-type]


class WordReversalTests(unittest.TestCase):
    def test_reverses_word_order(self) -> None:
        self.assertEqual("three two one", reverse_words("one two three"))

    def test_preserves_whitespace_structure(self) -> None:
        self.assertEqual(
            " three\t two  one ",
            reverse_words(" one\t two  three "),
        )

    def test_punctuation_stays_with_tokens(self) -> None:
        self.assertEqual("world! Hello,", reverse_words("Hello, world!"))

    def test_dispatches_modes_and_algorithms(self) -> None:
        self.assertEqual("cba", reverse_text("abc"))
        self.assertEqual("cba", reverse_text("abc", algorithm="loop"))
        self.assertEqual("two one", reverse_text("one two", mode="words"))

    def test_rejects_invalid_dispatch_values(self) -> None:
        with self.assertRaises(ValueError):
            reverse_text("abc", mode="unknown")  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            reverse_text("one two", mode="words", algorithm="loop")


if __name__ == "__main__":
    unittest.main()
