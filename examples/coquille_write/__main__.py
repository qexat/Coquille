from coquille import Coquille
from coquille.sequences import bold
from coquille.sequences import fg_blue
from coquille.sequences import fg_magenta
from coquille.sequences import italic

print("Hello World!")

Coquille.write("Hello World, but in magenta and italic!", fg_magenta, italic)

with open("examples/coquille_write/output.txt", "w") as my_file:
    Coquille.write("A pretty Hello World in a file!", fg_blue, bold, file=my_file)
