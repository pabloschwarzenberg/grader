numeros = input("Dame un numero de hasta 4 digitos: ")
if int(numeros)<10: 
    print(numeros[0],"U")
elif int(numeros)<100:
    print(numeros[0],"D", "+", numeros[1],"U")
elif int(numeros)<1000:
    print(numeros[0],"C", "+", numeros[1],"D", "+", numeros[2],"U")
elif int(numeros)<100000:
    print(numeros[0],"M", "+", numeros[1],"C", "+", numeros[2],"D", "+", numeros[3],"U")