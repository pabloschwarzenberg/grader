#Descomponer un número
numero_1=int(input("ingresar nunmero :"))


if numero_1 >= 1000:
    numero_m= int(str(numero_1)[0:1])
    numero_c= int(str(numero_1)[1:2])
    numero_d= int(str(numero_1)[2:3])
    numero_u= int(str(numero_1)[3:4])
    print(numero_m,"M +",numero_c,"C +",numero_d,"D +",numero_u,"U")

elif numero_1 <= 999 and numero_1 >= 100:
    numero_c= int(str(numero_1)[0:1])
    numero_d= int(str(numero_1)[1:2])
    numero_u= int(str(numero_1)[2:3])
    print(numero_c,"C +",numero_d,"D +",numero_u,"U")

elif numero_1 <= 99 and numero_1 >= 10:
    numero_d= int(str(numero_1)[0:1])
    numero_u= int(str(numero_1)[1:2])
    print(numero_d,"D +",numero_u,"U")

elif numero_1 <= 99and numero_1 >= 0:
    numero_u= int(str(numero_1)[0:1])
    print(numero_u,"U")
    