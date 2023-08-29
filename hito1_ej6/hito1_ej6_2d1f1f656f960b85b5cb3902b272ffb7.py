#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un segundo numero: "))
c = int(input("Ingrese un tercer numero: "))

mayor = max(a, b, c)
menor = min(a, b, c)

n = (a + b + c) - mayor - menor
print( menor ,", ", n , ", ", mayor) 