#Contestador de celular
numero = input("Ingresar numero: ")
x = int(len(numero))

if(x != 8):
    while(x != 8):
        numero = input("Ingresar numero de 8 dígitos: ")
        x = len(numero)

hora = int(input("Ingresar hora: "))

if(hora > 0 and hora < 7):
    print("CONTESTAR")

if(hora >=7 and hora < 14):
    if((numero[5] == "9") and (numero[6] == "0") and (numero[7] == "9")):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if(hora >= 14 and hora <= 17):
    print("NO CONTESTAR")

if(hora > 17 and hora < 19):
    if((numero[0] == "8") and (numero[1] == "7") and (numero[2] == "7")):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if(hora >= 19 and hora <= 23):
    print("NO CONTESTAR")