numero_1=int(input("ingrese numero 1:  "))

numero_2=int(input("ingrese numero 2:  "))

numero_3=int(input("ingrese numero 3:  "))


if numero_1>=numero_2>=numero_3:
    print(numero_3,",",numero_2,",",numero_1)
elif numero_1>=numero_3>=numero_2:
    print(numero_2,",",numero_3,",",numero_1)
elif numero_2>=numero_1>=numero_3:
    print(numero_3,",",numero_1,",",numero_2)
elif numero_2>=numero_3>=numero_1:
    print(numero_1,",",numero_3,",",numero_2)
elif numero_3>=numero_2>=numero_1:
    print(numero_1,",",numero_2,",",numero_3)
elif numero_3>=numero_1>=numero_2:
    print(numero_2,",",numero_1,",",numero_3)
        

        