#Ordenar tres números
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese el último número: "))
mayor = max(a,b,c)
menor = min(a,b,c)
order = (a + b + c) - mayor - menor
print(menor, ",", order , ",", mayor)