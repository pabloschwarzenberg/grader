#Nota final
print("por favor ingrese sus cuatro notas")
PT = float(input("su nota en tareas es de: "))
PI = float(input("su nota en interrogaciones es de: "))
NE = float(input("su nota en examenes es de: "))
PP = float(input("su nota en presentaciones es de: "))
R =((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP))
R = round(R,1)
print("su promedio redondeado es de: ", R)