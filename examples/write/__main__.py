from coquille import write

print("Hello World!")

write("Hello World, but in magenta and italic!", "fg_magenta", "italic")

with open("examples/write/output.txt", "w") as my_file:
    write("A pretty Hello World in a file!", "fg_blue", "bold", file=my_file)
