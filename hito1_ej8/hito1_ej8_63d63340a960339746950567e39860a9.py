numero = int(input("ingrese un numero(maximo 4 cifras): "))
if numero<=9:
    unidad = (numero%10)
    print(unidad,"U")
elif numero<=99:
    unidad = (numero%10)
    decena = (numero//10)%10
    print(decena,"D + ",unidad,"U" )
elif numero<=999:
    unidad = (numero%10)
    decena = (numero//10)%10
    centena = (numero//100)%10
    print(centena,"C + " ,decena,"D + ",unidad,"U" )
elif numero<=9999:
    unidad = (numero%10)
    decena = (numero//10)%10
    centena = (numero//100)%10
    uDeMil = (numero//1000)%10
    print(uDeMil,"M + " ,centena,"C + " ,decena,"D + ",unidad,"U" )
else:
    print("ingrese otro número")