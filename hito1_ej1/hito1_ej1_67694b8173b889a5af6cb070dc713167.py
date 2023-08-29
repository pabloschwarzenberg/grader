#Nota final
tareas=float(input("Ingresa tu calificacion que obtuviste en tareas: "))
interrogaciones=float(input("ingresa tu calificacion que obtuviste interrogaciones: "))
examen=float(input("ingresa tu califcacion que obtuviste en el examen: "))
presentacion=float(input("ingresa tu calificacion que obtuviste en la presentacion: "))

x = (tareas * 0.3) + (interrogaciones * 0.3) + (examen * 0.3) + (presentacion * 0.1)

y = round(x,1)

print(y)