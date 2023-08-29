numero = eval(input("Ingrese un numero: "))

miles = (numero//1000)%10
centenas =(numero//100)%10
decenas = (numero//10)%10
unidades = (numero//1)%10

respuesta = print(str(miles)+"M + "+str(centenas)+"C + "+str(decenas)+"D + "+str(unidades)+"U")