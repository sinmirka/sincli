# sincli

A lightweight Python library for expressive terminal text styling.

`sincli` turns strings into FIGlet headings and applies smooth RGB gradients with ANSI escape sequences.

## Features

- Text rendering with FIGlet fonts.
- RGB gradients for single-line and multi-line text.
- A straightforward API with no unnecessary setup.

## Installation

Python 3.10 or newer is required.

```bash
python -m pip install .
```

## Usage

```python
from sincli import Formatter

formatter = Formatter()

title = formatter.format_string("sincli")

print(
    formatter.gradient_string(
        title,
        start_color=(255, 93, 143),
        end_color=(116, 86, 255),
    )
)
```

`format_string()` returns text rendered with a FIGlet font. It uses `ansi_shadow` by default; pass a different font through the `font` parameter.

```python
print(formatter.format_string("Hello", font="slant"))
```

`gradient_string()` accepts a source string and start and end RGB colours. By default, it appends a terminal colour reset after the text; disable it with `reset_after=False`.

```python
print(
    formatter.gradient_string(
        "Styled CLI output",
        start_color=(0, 229, 255),
        end_color=(157, 78, 221),
        reset_after=False,
    )
)
```

For correct FIGlet text and gradient rendering, use a terminal with UTF-8, ANSI, and True Color support.

## API

| Method | Purpose |
| --- | --- |
| `Formatter.format_string(string, font=None)` | Renders a string with a FIGlet font. |
| `Formatter.gradient_string(string, start_color, end_color, reset_after=True)` | Returns a string with an RGB gradient. |

Colours are supplied as `(R, G, B)` tuples, where every value is between `0` and `255`.
