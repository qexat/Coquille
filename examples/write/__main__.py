from coquille import write
from coquille.sequences import bold
from coquille.sequences import fg_blue
from coquille.sequences import fg_magenta
from coquille.sequences import italic

print("Hello World!")

write("Hello World, but in magenta and italic!", fg_magenta, italic)

with open("examples/write/output.txt", "w") as my_file:
    write("A pretty Hello World in a file!", fg_blue, bold, file=my_file)
