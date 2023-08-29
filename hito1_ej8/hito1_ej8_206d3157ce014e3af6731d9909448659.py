#Descomponer un número

print ("INTRODUCE EL NUMERO: ")

numero = int(input())



umil = int(numero/1000)

tmp = int(numero % 1000)



centenas = int(tmp/100)

tmp = int(tmp % 100)



decenas = int(tmp/10)

unidades = int(tmp%10)



if umil > 0:

    print (umil,"M + ",centenas,"C + ",decenas,"D + ",unidades,"U")

else:

    if centenas > 0:

        print (centenas,"C + ",decenas,"D + ",unidades,"U")

    else:

        if decenas > 0:

            print (decenas,"D + ",unidades,"U")

        else:

            print (unidades,"U")