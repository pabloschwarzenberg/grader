#Descomponer un número
numero = int(input("Ingrese un número entero de hasta 4 dígitos: "))

if numero > 0 and numero < 10:
    str(numero)
    print("%sU" % numero)
elif numero >= 10 and numero <= 99:
    numero_str = str(numero)
    print("%sD + %sU" % (str(numero_str[0:1]), str(numero_str[1:2])))
elif numero >= 100 and numero <= 999:
    numero_str = str(numero)
    print("%sC + %sD + %sU" % (str(numero_str)[0:1], str(numero_str)[1:2], str(numero_str)[2:3]))
elif numero >= 1000 and numero <= 9999:
    numero_str = str(numero)
    print("%sM + %sC + %sD + %sU" % (str(numero_str)[0:1], str(numero_str)[1:2], str(numero_str)[2:3], str(numero_str)[3:4]))

else:
    print("Número inválido")
