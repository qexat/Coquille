from coquille import Coquille
from coquille.sequences import bold
from coquille.sequences import fg_magenta
from coquille.sequences import italic

print("Hello World!")

# By default, the coquille wraps the standard output
with Coquille.new(fg_magenta, italic) as coquille:
    print("Hello World, but in magenta and italic!")
    coquille.apply(bold)
    print("Now, with a touch of bold :D")

print("Oh, we are back to normal now...")
