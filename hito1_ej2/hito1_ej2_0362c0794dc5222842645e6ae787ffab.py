#Contestador de celular
     hora = eval(input("ingrese la hora de su llamada(reemplaze el , por un .): "))
numero = eval(input("ingrese su numero telefonico de 8 cifras: "))
strnumero = str(numero)
if(hora > 00.00 and hora < 7.00):
    print("contestar")
if(hora < 14.00 and hora > 7.01 or strnumero[5:9] != str(909)):
    print("No contestar")
if(hora < 14.00 and hora > 7.01 and strnumero[5:9] == str(909)):
    print("contestar")
if(hora < 17.00 and hora > 19.00 and strnumero[0:3] == str(807) and hora > 12):
    print("contestar")
if(hora < 17.00 and hora > 19.00):
    print(" no contestar")
if(hora > 17.00 and hora < 19.00):
    print("contestar")
if(hora > 19.00):
    print("no contestar")
    