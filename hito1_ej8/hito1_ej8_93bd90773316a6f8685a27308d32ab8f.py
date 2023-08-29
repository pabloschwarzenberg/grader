#Descomponer un numero
numeroE = int(input("Ingrese numero de MAX 4 digitos para descomponer : "))
#UDM,C,D,U
unidadDeMil = (numeroE//1000)%10
centena = (numeroE//100)%10
decena = (numeroE//10)%10
unidad = (numeroE//1)%10
#Imprimir
if numeroE > 999:
    print(unidadDeMil,"M +",centena,"C +",decena,"D +",unidad,"U")
if numeroE > 99:
    print(centena,"C +",decena,"D +",unidad,"U")
if numeroE > 9:
    print(decena,"D +",unidad,"U")
if numeroE <= 9:
    print(unidad,"U")