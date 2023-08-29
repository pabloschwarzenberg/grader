#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 dígitos: "))
if 0 < numero < 10000:
    mil = numero//1000
    centena = (numero%1000)//100
    decena = ((numero%1000)%100)//10
    unidad = ((numero%1000)%100)%10
    print(str(mil) + "M + " + str(centena) + "C + " + str(decena) + "D + " + str(unidad) + "U")
else:
    print("Este numero no es de 4 dígitos vuelva a intentar")
