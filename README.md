# Coquille

Coquille (IPA: `/kɔ.kij/`, english: 'shell' or 'typo') is a library that wraps terminal escape sequences to easily apply them to a stream.

## Notes

Requires Python 3.9 or higher.

This library attempts to cover as many escape sequences as possible ; but it is not an exhaustive list, some might be missing. Also, you might find that few have no effect on your terminal emulator.

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

## Documentation

Coming soon! 🚧
