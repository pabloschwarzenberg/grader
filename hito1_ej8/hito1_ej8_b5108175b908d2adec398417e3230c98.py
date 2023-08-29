#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 digitos:", ))
mil = numero // 1000
cen = (numero // 100) - (mil * 10)
dec = (numero // 10) - (mil * 100) - (cen * 10)
uni = numero % 10
if numero > 1000:
    print(str(mil) + "M", "+", str(cen) + "C", "+", str(dec) + "D", "+", str(uni) + "U")
elif numero > 100:
    print(str(cen) + "C", "+", str(dec) + "D", "+", str(uni) + "U")
elif numero > 10:
    print(str(dec) + "D", "+", str(uni) + "U")
else:
    print(str(uni) + "U")     