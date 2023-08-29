#Ordenar tres números
#Este programa tiene la capacidad de poder recibir 3 números enteros y ordenarlos de menor a mayor.
print("Este programa tiene la capacidad de poder recibir 3 números enteros y ordenarlos de menor a mayor.")
numero1=int(input("Ingrese su primer número entero: "))
numero2=int(input("Ingrese su segundo número entero: "))
numero3=int(input("Ingrese su tercer número entero: "))

if numero1 < numero2 and numero2 < numero3:
    print(" ", numero1, " , ", numero2, " , ", numero3)
elif(numero2 < numero1 and numero1 < numero3):
    print(" ", numero2, " , ", numero1, " , ", numero3)
elif(numero3 < numero1 and numero1 < numero2):
    print(" ", numero3, " , ", numero1, " , ", numero2)
elif(numero3 < numero2 and numero2 < numero1):
    print(" ", numero3, " , ", numero2, " , ", numero1)
elif(numero1 < numero2 and numero3 < numero2):
    print(" ", numero1, " , ", numero3, " , ", numero2)   
elif(numero2 < numero3 and numero3 < numero1):
    print(" ", numero2, " , ", numero3, " , ", numero1)
else:
    print("Se ingresaron números iguales, inicie nuevamente el programa.")