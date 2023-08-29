#Ordenar tres números
print("Debe ingresar 3 numeros distintos")
n1 = eval(input("Ingrese n1: "))
n2 = eval(input("Ingrese n2: "))
n3 = eval(input("Ingrese n3: "))
if n2<n1>n3 and n2>n3:
    print("El orden de menor a mayor es: ", n3, ",", n2 ,",", n1)
elif n2<n1>n3 and n3>n2:
    print("El orden de menor a mayor es: ", n2, "," ,n3 ,",", n1)
elif n1<n2>n3 and n1>n3:
    print("El orden de menor a mayor es: ", n3, ",", n1 ,",", n2)
elif n1<n2>n3 and n3>n1:
    print("El orden de menor a mayor es: ", n1, ",", n3 ,",", n2)
elif n1<n3>n2 and n1>n2:
    print("El orden de menor a mayor es: ", n2, ",", n1 ,",", n3)
elif n1<n3>n2 and n2>n1:
    print("El orden de menor a mayor es: ", n1, ",", n2 ,",", n3)
elif n1<n3>n2 and n2==n1:
    print("El orden de menor a mayor es: ", n1, ",", n2 ,",", n3)
elif n2<n1>n3 and n2==n3:
    print("El orden de menor a mayor es: ", n2, ",", n3 ,",", n1)    
elif n1<n2>n3 and n3==n1:
    print("El orden de menor a mayor es: ", n3, ",", n1 ,",", n2)
elif n1==n2==n3:
    print("El orden de menor a mayor es: ", n1, ",", n2 ,",", n3)
else:
    print("Opcion no valida")
