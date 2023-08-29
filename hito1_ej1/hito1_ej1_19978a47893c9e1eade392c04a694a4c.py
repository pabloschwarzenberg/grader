#Nota final
print("por favor ingrese sus cuatro notas")
pt = float(input("su nota en tareas es de: "))
pi = float(input("su nota en interrogaciones es de: "))
ne = float(input("su nota en examenes es de: "))
pp = float(input("su nota en presentaciones es de: "))
k =((0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp))
k = round(k,1)
print("su promedio redondeado es de: ", k) 