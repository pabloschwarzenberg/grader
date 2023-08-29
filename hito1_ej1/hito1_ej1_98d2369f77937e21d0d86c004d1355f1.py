tar = float(input("Ingrese la nota de su tarea"))
inte = float(input("ingrese la nota de su interrogacion"))
exa = float(input("ingrese la nota de su examen"))
pre = float(input("ingrese la nota de su presentación"))

pm = 0.3*tar + 0.3*inte + 0.3*exa + 0.1*pre

print("su nota final es", pm)