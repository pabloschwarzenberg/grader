numero1=int(input("ingrese numero"))
numero2=int(input("ingrese numero"))
numero3=int(input("ingrese numero"))
if numero1>=numero2 and numero2>=numero3:
    print(numero3, ",",numero2,",", numero1)
elif numero1>=numero3 and numero3>=numero2:
    print(numero2, ",",numero3, ",", numero1)
elif numero2>=numero1 and numero1>=numero3:
    print(numero3, ",",numero1, ",",numero2)
elif numero2>=numero3 and numero3>=numero1:
    print(numero1, ",",numero3, ",",numero2)
elif numero3>=numero1 and numero1>=numero2:
    print(numero2, ",",numero1, ",",numero3)
elif numero3>=numero2 and numero2>=numero1:
    print(numero1, ",",numero2,",", numero3)
   