#Ordenar tres números
print("Este programa tiene la capacidad de poder recibir 3 números enteros y ordenarlos de menor a mayor.")
n1=int(input("Ingrese su primer número entero: "))
n2=int(input("Ingrese su segundo número entero: "))
n3=int(input("Ingrese su tercer número entero: "))

if n1 < n2 and n2 < n3:
    print(" ", n1, " , ", n2, " , ", n3)
elif(n2 < n1 and n1 < n3):
    print(" ", n2, " , ", n1, " , ", n3)
elif(n3 < n1 and n1 < n2):
    print(" ", n3, " , ", n1, " , ", n2)
elif(n3 < n2 and n2 < n1):
    print(" ", n3, " , ", n2, " , ", n1)
elif(n1 < n2 and n3 < n2):
    print(" ", n1, " , ", n3, " , ", n2)   
elif(n2 < n3 and n3 < n1):
    print(" ", n2, " , ", n3, " , ", n1)
else:
    print("Se ingresaron números iguales, inicie nuevamente el programa.")