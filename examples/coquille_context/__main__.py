from coquille import Coquille

print("Hello World!")

# By default, the coquille wraps the standard output
with Coquille.new("fg_magenta", "italic") as coquille:
    print("Hello World, but in magenta and italic!")
    coquille.apply("bold")
    print("Now, with a touch of bold :D")

print("Oh, we are back to normal now...")
