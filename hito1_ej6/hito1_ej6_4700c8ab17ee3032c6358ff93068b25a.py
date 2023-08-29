#Ordenar tres números
a = eval(input("Inserte un número: "))
b = eval(input("Inserte un segundo número: "))
c = eval(input("Inserte un tercer número: "))

Mayor = max(a,b,c)
Menor = min(a,b,c)
Central = a + b + c - Mayor - Menor

print("De forma ordenada es:",Menor,",",Central,",",Mayor)
