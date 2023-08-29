#Descomponer un número
numero = input("Ingrese un numero de 4 digitos: ")
numerousuario = int(numero)
if numerousuario >= 0 and numerousuario <= 9:
    print(numerousuario,"U")
elif numerousuario >=10 and numerousuario <= 99:
    unidad = int(numero[1])
    decena = int(numero[0])
    print(decena,"D", "+", unidad,"U")
elif numerousuario >= 100 and numerousuario <= 999:
    unidad = int(numero[2])
    decena = int(numero[1])
    centena = int(numero[0])
    print(centena,"C", "+", decena,"D", "+", unidad,"U")
else:
    numerousuario >= 1000 and numerousuario <= 9999
    unidad = int(numero[3])
    decena = int(numero[2])
    centena = int(numero[1])
    mil = int(numero[0])
    print(mil,"M", "+", centena,"C", "+", decena,"D", "+", unidad,"U")