#Le pedimos al usuario que entrega sus notas
print("A continuación deberás ingresar tus notas con un decimal:")
pt=float(input("Ingresa tu nota obtenida en tareas: "))
pi=float(input("Ingresa tu nota obtenida en interrogaciones: "))
ne=float(input("Ingresa tu nota obtenida en examen: "))
pp=float(input("Ingresa tu nota obtenida en tu presentación: "))
#creamos la operación y el resultado lo redondeamos a un decimal
promedio=0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
prom_decimal=round(promedio,1)

#imprimimos el promedio redoneado
print("El promedio final de todas sus notas es de :",prom_decimal)
      