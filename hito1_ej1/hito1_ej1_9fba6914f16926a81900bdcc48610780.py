#entrada

PT = eval(input("Ingresa tu nota de tareas: "))
PI = eval(input("Ingresa tu nota de interrogaciones: "))
NE = eval(input("Ingresa tu nota de examen: "))
PP = eval(input("Ingresa tu nota de presentacion: "))

#procesamiento

z = 0.3 * round(PT)
x = 0.3 * round(PI)
c = 0.3 * round(NE)
y = 0.1 * round(PP)

resultado_final = (z + x + c + y)

#salida

print("tu nota final es: ", resultado_final)