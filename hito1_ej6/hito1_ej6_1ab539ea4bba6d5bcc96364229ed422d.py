numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

if numero1 <= numero2 <= numero3:
    print(numero1,",",numero2,",",numero3)
elif numero3 <= numero2 <= numero1:
    print(numero3,",",numero2,",",numero1)
elif numero2 <= numero3 <= numero1:
    print(numero2,",",numero3,",",numero1)
elif numero1 <= numero3 <= numero2:
    print(numero1,",",numero3,",",numero2)
elif numero2 <= numero1 <= numero3:
    print(numero2,",",numero1,",",numero3)
elif numero3 <= numero1 <= numero2:
    print(numero3,",",numero1,",",numero2)
else:
    print("no se pueden ordenar totalmente")
          

