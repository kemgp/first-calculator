# Calculator

A simple desktop calculator built with Python and Tkinter. It provides a fixed-size, centered window with a numeric display and clickable buttons.

## Features

- Addition, subtraction, multiplication, and division
- Decimal numbers
- Sign toggle (`+/-`)
- Percentage conversion (`%`, divides the displayed number by 100)
- Square root (`√`)
- Clear all (`AC`)

## Requirements

- Python 3
- Tkinter support in your Python installation
- A desktop environment to display the calculator window

No third-party Python packages are required. To check that Tkinter is available, run:

```sh
python3 -m tkinter
```

This should open a small demonstration window. If Tkinter is missing, install Tkinter support for your Python distribution.

## Run

From the project directory:

```sh
python3 calc.py
```

On Windows, you can also use `python calc.py` or `py calc.py`.

## Usage

1. Click the number buttons to enter a value.
2. Select an operator (`+`, `-`, `×`, or `÷`).
3. Enter the second value and click `=`.
4. Click `AC` to reset the display and any pending operation.

For example, click `1`, `2`, `+`, `3`, then `=` to display `15`. The `+/-`, `%`, and `√` buttons act on the currently displayed value.

## Project structure

```text
calculator/
├── calc.py     # Tkinter interface and calculator logic
└── README.md   # Setup and usage instructions
```

## Current limitations

- Input uses the on-screen buttons; keyboard input is not implemented.
- Calculations support one binary operation at a time. Press `=` before starting another operation.
- Division by zero and square roots of negative numbers are not handled and raise errors.
