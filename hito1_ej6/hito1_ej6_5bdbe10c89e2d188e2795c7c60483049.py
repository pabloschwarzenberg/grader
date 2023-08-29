#Ordenar tres números
print("Ingrese tres numeros")
a=eval(input("ingrese el primer numero:"))
b=eval(input("ingrese el segundo numero:"))
c=eval(input("ingrese el tercer numero:"))
#ordenar
d=min(a, b, c)
e=max(a, b, c)
f=(a+b+c)-d-e
#mostrar en pantalla el orden
print("El orden de los numeros de menor a mayor es:", d, ",", f, ",", e)