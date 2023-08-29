#Nota final
print("ingrese sus cuatro notas")
PT = float(input("su nota en tareas : "))
PI = float(input("su nota en interrogaciones : "))
NE = float(input("su nota en examenes : "))
PP = float(input("su nota en presentaciones : "))
k =((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP))
k = round(k,1)
print("su promedio redondeado es : ", k)
    