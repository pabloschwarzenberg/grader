#Ordenar tres números de menor a mayor, separados por una coma.
numero1=int(input("Ingrese primer número: "))
numero2=int(input("Ingrese segundo número: "))
numero3=int(input("Ingrese tercer número: "))
a=min(numero1,numero2,numero3)
c=max(numero1,numero2,numero3)
b=(numero1+numero2+numero3) - a - c
print("Los números ordenados de menor a mayor son: {} , {} , {}" .format(a,b,c))