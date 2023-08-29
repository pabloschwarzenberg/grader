#Descomponer un número
numero = int(input("Ingresa un numero de  digitos: "))
if  numero > 999 and numero < 9999 :
    mil = int(numero//1000)
    centena = int(numero//100)-mil*10
    decena = int(numero//10)-mil*100-centena*10
    unidad = numero - (mil*1000)-(centena*100)-(decena*10)
    print(str(mil)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U+")
elif numero > 99 and numero < 1000 :
    centena = int(numero // 100)
    decena = int(numero // 10) - centena * 10
    unidad = numero -  (centena * 100) - (decena * 10)
    print(str(centena) + "C+" + str(decena) + "D+" + str(unidad) + "U")

elif numero < 100 :
    decena = int(numero // 10)
    unidad = numero - (decena * 10)
    print(str(decena) + "D+" + str(unidad) + "U")
