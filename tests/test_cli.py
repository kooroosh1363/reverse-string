from __future__ import annotations

import io
import unittest

from reverse_string.cli import main


class CliTests(unittest.TestCase):
    def test_positional_character_input(self) -> None:
        output = io.StringIO()
        exit_code = main(["hello"], stdin=io.StringIO(), stdout=output)

        self.assertEqual(0, exit_code)
        self.assertEqual("olleh\n", output.getvalue())

    def test_word_mode(self) -> None:
        output = io.StringIO()
        main(["one  two three", "--mode", "words"], stdout=output)

        self.assertEqual("three  two one\n", output.getvalue())

    def test_explicit_stdin_is_reversed_exactly(self) -> None:
        output = io.StringIO()
        main(["--stdin"], stdin=io.StringIO("abc\n"), stdout=output)

        self.assertEqual("\ncba", output.getvalue())

    def test_interactive_prompt(self) -> None:
        output = io.StringIO()
        main([], stdin=io.StringIO("drawer\n"), stdout=output)

        self.assertEqual("Text: reward\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
