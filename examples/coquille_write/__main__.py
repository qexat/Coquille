from coquille import Coquille
from coquille.sequences import fg_truecolor

print("Normal Hello World!")

coquille = Coquille.new(fg_truecolor(128, 255, 0))
coquille.write("Colorful Hello World!")
