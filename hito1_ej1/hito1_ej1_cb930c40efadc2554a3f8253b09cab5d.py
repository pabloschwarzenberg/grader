#Nota final
PT=float(input("Ingrese la nota de sus Tareas: "))
PI=float(input("Ingrese la nota de sus Interrogaciones: "))
NE=float(input("Ingrese la nota de su Examen: "))
PP=float(input("Ingrese la nota de sus Presentaciones: "))
if PT>=1 and PI>=1 and NE>=1 and PP>=1:
    Nota=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
    NotaF=round(Nota, 1)
    print("La nota final es: ", NotaF)
else:
    print("Ingrese un valor valido porfavor")