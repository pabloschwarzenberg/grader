print("ingrese las siguientes notas para calcular el promedio")
print("tareas: ")
n1=eval(input())
print("inerrogaciones: ")
n2=eval(input())
print("examen: ")
n3=eval(input())
print("precentacion: ")
n4=eval(input())
calculo = 0.3 * n1 + 0.3 * n2 + 0.3 * n3 + 0.1 * n4
notafinal=round(calculo,1)
print("el promedio de todas sus notas es: ",notafinal)