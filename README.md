# Coquille

Coquille (IPA: `/kɔ.kij/`, english: 'shell' or 'typo') is a library that wraps terminal escape sequences to easily apply them to a stream.

## Notes

Requires Python 3.9 or higher.

This library attempts to cover as many escape sequences as possible ; but it is not an exhaustive list, some might be missing. Also, you might find that few have no effect on your terminal emulator.

## Install

### Normal installation

```sh
pip install coquille
```

### Dev installation

```sh
pip install coquille[dev]
```

This allows you to run the tests:

```sh
coverage run -m pytest
```

Then check the coverage:

```sh
coverage report -m
```

## Examples

### Coquille context manager

```py
from coquille import Coquille
from coquille.sequences import bold, fg_magenta, italic

print("Hello World!")

# By default, the coquille wraps the standard output
with Coquille.new(fg_magenta, italic) as coquille:
    print("Hello World, but in magenta and italic!")
    coquille.apply(bold)
    print("Now, with a touch of bold :D")

print("Oh, we are back to normal now...")
```

![screenshot.png](https://raw.githubusercontent.com/qexat/Coquille/main/examples/coquille_context/screenshot.png)

Source code: [examples/coquille_context/](https://github.com/qexat/Coquille/blob/main/examples/coquille_context/__main__.py)

### Coquille.print()

```py
from coquille import Coquille
from coquille.sequences import bold, fg_blue, fg_magenta, italic

print("Hello World!")

Coquille.print("Hello World, but in magenta and italic!", fg_magenta, italic)

with open("examples/coquille_print/output.txt", "w") as my_file:
    Coquille.print("A pretty Hello World in a file!", fg_blue, bold, file=my_file)

```

![screenshot.png](https://raw.githubusercontent.com/qexat/Coquille/main/examples/coquille_print/screenshot.png)

Source code: [examples/coquille_print/](https://github.com/qexat/Coquille/blob/main/examples/coquille_print/__main__.py)

## Documentation

Coming soon! 🚧
