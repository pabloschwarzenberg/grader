#Ordenar tres números
N1 = eval(input("Ingrese el valor 1: "))
N2 = eval(input("Ingrese el valor 2: "))
N3 = eval(input("Ingrese el valor 3: "))

if (N1 < N2 < N3):
        print("El orden de menor a mayor de los números es: ", N1,",", N2,",",N3)
elif (N2< N1 <N3):
        print("El orden de menor a mayor de los números es: ", N2,",",N1,",",N3)
elif (N3< N2 < N1):
        print("El orden de menor a mayor de los números es: ", N3,",",N2,",",N1)
elif (N1< N3 < N2):
        print("El orden de menor a mayor de los números es: ", N1,",",N3,",",N2)
elif (N3< N1< N2):
        print("El orden de menor a mayor de los números es: ", N3,",",N1,",",N2)
elif (N2< N3< N1):
        print("El orden de menor a mayor de los números es: ",N2,",",N3,",",N1)
else:
        print("el orden de menor a mayor de los números es: ",N1,",",N3,",",N2)
