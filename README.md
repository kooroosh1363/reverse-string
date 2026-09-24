# Reverse String Lab

[![Quality](https://github.com/kooroosh1363/reverse-string/actions/workflows/quality.yml/badge.svg)](https://github.com/kooroosh1363/reverse-string/actions/workflows/quality.yml)

A small Python exercise modernized into a clean, testable learning project for string reversal, CLI design, package structure, edge cases, and algorithm trade-offs.

The repository started in 2023 as a short loop that read from `input()` and printed characters in reverse order. The current version keeps that learning history while separating pure logic from user interaction and adding automated tests and CI.

## Features

- reverse characters with idiomatic slicing
- reverse characters with an explicit backwards loop
- reverse whitespace-delimited word order
- preserve whitespace structure in word mode
- positional, interactive, and stdin CLI input
- zero runtime dependencies
- type hints and focused docstrings
- unit tests for core behavior and CLI behavior
- GitHub Actions across Python 3.11, 3.12, and 3.13

## Quick start

Run directly from the repository:

```bash
python -m reverse_string "hello"
```

Output:

```text
olleh
```

Reverse word order:

```bash
python -m reverse_string "one  two three" --mode words
```

Output:

```text
three  two one
```

Use the explicit loop implementation:

```bash
python -m reverse_string "hello" --algorithm loop
```

Read exact content from stdin:

```bash
printf 'abc\n' | python -m reverse_string --stdin
```

Interactive mode:

```bash
python -m reverse_string
```

## Install as a CLI

```bash
python -m pip install -e .
reverse-string "drawer"
```

## API

```python
from reverse_string import reverse_characters, reverse_words

reverse_characters("hello")
# "olleh"

reverse_words("one two three")
# "three two one"
```

## Algorithms

### Slicing

```python
text[::-1]
```

This is the default implementation because it is concise, idiomatic, and easy to review.

### Explicit backwards loop

The project also keeps a loop-based implementation for learning. Instead of repeatedly concatenating strings, it appends characters to a list and joins once.

Both approaches are:

- **Time:** O(n)
- **Extra result storage:** O(n)

The loop version is more verbose but exposes the indexing algorithm directly.

## Character mode vs word mode

Character mode reverses Python string elements:

```text
"abc" -> "cba"
```

Word mode reverses non-whitespace tokens while preserving the existing whitespace slots:

```text
"one   two three" -> "three   two one"
```

Punctuation stays attached to the token:

```text
"Hello, world!" -> "world! Hello,"
```

## Unicode note

Python strings are Unicode, but `text[::-1]` reverses Unicode code points, not user-perceived grapheme clusters.

That distinction matters for some combining marks, emoji sequences, flags, and scripts with multi-code-point graphemes. A production-grade "reverse what a user sees" feature would require grapheme-cluster segmentation, typically via a Unicode-aware library.

This project intentionally stays dependency-free and documents that boundary rather than pretending code-point reversal solves every Unicode case.

## Project structure

```text
.
├── reverse_string/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── core.py
├── tests/
│   ├── test_cli.py
│   └── test_core.py
├── .github/workflows/
│   └── quality.yml
├── pyproject.toml
└── reverse_str_1.py
```

## Tests

Run all tests:

```bash
python -m unittest discover -s tests -v
```

Compile-check the code:

```bash
python -m compileall -q reverse_string tests reverse_str_1.py
```

The test suite covers:

- empty strings
- single-character strings
- whitespace
- non-ASCII text
- emoji code points
- equivalence of slice and loop implementations
- word-order reversal
- punctuation behavior
- invalid mode/algorithm combinations
- positional CLI input
- interactive CLI input
- exact stdin behavior

## Engineering decisions

### Pure functions first

The original implementation mixed input, reversal, and printing. The modern version returns values from pure functions, which makes the logic reusable and easy to test.

### No unnecessary framework

This problem does not need a web app, database, or external package. The upgrade improves engineering quality without inflating a five-line algorithm into an unrelated system.

### Preserve learning history

The original filename remains as a compatibility wrapper, while the 2023 implementation is still visible in Git history. This makes the repository a clear before/after example.

## Trade-offs

- Word mode is intentionally token-based, not natural-language-aware.
- Character mode is code-point-based, not grapheme-cluster-aware.
- The project uses the standard library test framework to remain dependency-free.
- It targets Python 3.11+ so the implementation can use current typing and `zip(..., strict=True)`.

## License

No license is currently included. Add one before redistributing the code as reusable software.
