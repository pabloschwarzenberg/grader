#Ordenar tres números
n1 = int(input("Escriba el primer N°: "))
n2= int(input("Escriba el segundo N°: "))
n3= int(input("Escriba el tercer N°: "))

minimo= min(n1,n2,n3)
maximo= max(n1,n2,n3)
intermedio=(n1+n2+n3)-maximo-minimo

print("Los numeros se ordenan de menor a mayor: ",(minimo, intermedio, maximo))