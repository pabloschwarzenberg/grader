#Ejercicios Hito 1: Parte 1
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.

print("bienvenido al ordenador de numeros por favor ingrese los datos requeridos")

V1 = eval(input("ingrese digito 1:"))
V2 = eval(input("ingrese digito 2:"))
V3 = eval(input("ingrese digito 3:"))

valores = [V1,V2,V3]
valores.sort(reverse=False)
print("tus valores ordenados son" ,valores)

#si cambias reverse=False a True, lo convertiras en un programa para ordenar de mayor a menor