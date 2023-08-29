#Nota final
print("por favor ingrese sus cuatro notas")
pt = float(input("su nota en tareas es de: "))
pi = float(input("su nota en interrogaciones es de: "))
ne = float(input("su nota en examenes es de: "))
pp = float(input("su nota en presentaciones es de: "))
p =((pt*30/100) + (pi*30/100) + (ne*30/100) + (pp*10/100))
print("su promedio redondeado es de: {:.1f}".format(p))