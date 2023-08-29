#Ordenar tres números
a1=int(input("ingrese un numero: "))
a2=int(input("ingrese un numero: "))
a3=int(input("ingrese un numero: "))
b1 = min(a1, a2, a3)
b2 = max(a1, a2, a3)
b3 = (a1+a2+a3)-b1 - b2
print("Tu resultado es: ",b1," , ",b3,",",b2)

