#Nota final
lista =[]
lista.append(float(input("ingrese notas de tareas: ")))
lista.append(float(input("ingrese notas de interrogaciones: ")))
lista.append(float(input("ingrese notas de examen: ")))
lista.append(float(input("ingrses notas de presentacion: ")))

resultado = (lista[0] * 0.3 )+ (lista[1] * 0.3)+ (lista[2]* 0.3)+ (lista[3]* 0.1)

print(resultado)     