#Nota final
#Entrada
print("Hola Calcularemos tu nota de presentacion para el examen final")
print("-"*62)
#Datos
PT = eval(input("Ingrese Nota de Tareas: "))
PI = eval(input("Ingrese Notas de Interrogaciones: "))
NE = eval(input("Ingrese Notas de Examen: "))
PP = eval(input("Ingrese Nota de Presentacion: "))
#Procesos
nota_presentacion = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
#Salida
print("Su Nota de Presentacion es,{}".format({round(nota_presentacion,1)}))