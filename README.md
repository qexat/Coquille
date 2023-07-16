# Coquille

Coquille (IPA: `/kɔ.kij/`, english: 'shell' or 'typo') is a library that wraps terminal escape sequences to easily apply them to a stream.

## Notes

Requires Python 3.9 or higher.

This library attempts to cover as many escape sequences as possible ; but it is not an exhaustive list, some might be missing. Also, you might find that few have no effect on your terminal emulator.

This library is based on the following resources:

- The Wikipedia page: <https://en.m.wikipedia.org/wiki/ANSI_escape_code>
- Some Microsoft documentation about console virtual terminal sequences: <https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences>

## Examples

Even though the examples are mostly showcasing [SGR escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters) (because they are pretty visible), Coquille can do more! See the [documentation](#documentation).

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

### write()

```py
from coquille import write
from coquille.sequences import bold, fg_blue, fg_magenta, italic

print("Hello World!")

write("Hello World, but in magenta and italic!", fg_magenta, italic)

with open("examples/write/output.txt", "w") as my_file:
    write("A pretty Hello World in a file!", fg_blue, bold, file=my_file)

```

![screenshot.png](https://raw.githubusercontent.com/qexat/Coquille/main/examples/write/screenshot.png)

Source code: [examples/write/](https://github.com/qexat/Coquille/blob/main/examples/write/__main__.py)

### Coquille.write()

```py
from coquille import Coquille
from coquille.sequences import fg_truecolor

print("Normal Hello World!")

coquille = Coquille.new(fg_truecolor(128, 255, 0))
coquille.write("Colorful Hello World!")

```

![screenshot.png](https://raw.githubusercontent.com/qexat/Coquille/main/examples/coquille_write/screenshot.png)

Source code: [examples/coquille_write/](https://github.com/qexat/Coquille/blob/main/examples/coquille_write/__main__.py)

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

## Documentation

Coming soon! 🚧

## Related projects

If you like Coquille, you might want to check these projects as well:

- [Colorama](https://github.com/tartley/colorama): a simple cross-platform colored terminal text in Python, by [Jonathan Hartley](https://github.com/tartley)
- [Rich_](https://github.com/Textualize/rich): a Python library for rich text and beautiful formatting in the terminal, by [Dave Pearson](https://github.com/davep)
- [Dahlia](https://github.com/dahlia-lib/dahlia): a simple text formatting package, inspired by the game Minecraft, by [trag1c](https://github.com/trag1c/)
