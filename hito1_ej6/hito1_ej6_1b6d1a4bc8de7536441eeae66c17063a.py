#Ordenar tres números
numero1 =int(input("ingrese el primer numero "))
numero2 =int(input("ingrese el segundo numero "))
numero3 =int(input("ingrese el tercer numero "))

a=min(numero1, numero2, numero3)
c=max(numero1, numero2, numero3)
b= (numero1 + numero2 + numero3) - a - c

#1, 2, 3
#a= 1
#c= 3
#b= (1 + 2 + 3) -1 - 3
#b= 6 - 1 - 3= 2

print("los numeros enteros ordenados son: {}, {}, {}".format(a, b, c))      