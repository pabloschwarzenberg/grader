#Ordenar tres números
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
numero_1 = int(input("Favor ingresar primer numero: "))
numero_2 = int(input("Favor ingresar segundo numero: "))
numero_3 = int(input("Favor ingresar tercer numero: "))

if numero_1>numero_2 and numero_2>numero_3:
    print ("Los numeros ordenados de menor a mayor son ", numero_3,",",numero_2,",",numero_1)
elif numero_2>numero_1 and numero_1>numero_3:
    print ("Los numeros ordenados de menor a mayor son ", numero_3,",",numero_1,",",numero_2)
elif numero_3>numero_1 and numero_1>numero_2:
    print ("Los numeros ordenados de menor a mayor son ", numero_2,",",numero_1,",",numero_3)
elif numero_3>numero_2 and numero_2>numero_1:
    print ("Los numeros ordenados de menor a mayor son ", numero_1,",",numero_2,",",numero_3)
elif numero_1>numero_3 and numero_3>numero_2:
    print ("Los numeros ordenados de menor a mayor son ", numero_2,",",numero_3,",",numero_1)
elif numero_2>numero_3 and numero_3>numero_1:
    print ("Los numeros ordenados de menor a mayor son ", numero_1,",",numero_3,",",numero_2)
elif numero_1>=numero_2 and numero_2>=numero_3:
    print ("Los numeros ordenados de menor a mayor son ", numero_3,",",numero_2,",",numero_1)
elif numero_2>=numero_1 and numero_1>=numero_3:
    print ("Los numeros ordenados de menor a mayor son ", numero_3,",",numero_1,",",numero_2)
elif numero_3>=numero_1 and numero_1>=numero_2:
    print ("Los numeros ordenados de menor a mayor son ", numero_2,",",numero_1,",",numero_3)
elif numero_3>=numero_2 and numero_2>=numero_1:
    print ("Los numeros ordenados de menor a mayor son ", numero_1,",",numero_2,",",numero_3)
elif numero_1>=numero_3 and numero_3>=numero_2:
    print ("Los numeros ordenados de menor a mayor son ", numero_2,",",numero_3,",",numero_1)
elif numero_2>=numero_3 and numero_3>=numero_1:
    print ("Los numeros ordenados de menor a mayor son ", numero_1,",",numero_3,",",numero_2)
else:
    print ("Los numeros ingresados son iguales")