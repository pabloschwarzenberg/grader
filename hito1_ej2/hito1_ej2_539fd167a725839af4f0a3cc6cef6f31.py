#Contestador de celular
num = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese hora de la llamada:"))
if hora >= 23 or hora < 0:
    print("hora debe ser entre 0 y 23")
elif num <= 10000000 or num >= 99999999:
    print("debe ser un numero de 8 digitos")
else:
    ult = num%1000
    if hora > 19:
        print("Resultado:NO CONTESTAR")
    elif hora > 0 and hora < 7:
        print("Resultado:CONTESTAR")
    elif hora > 7 and hora < 14 and ult == 909:
        print("Resultado:CONTESTAR")
    elif hora > 17 and hora < 17 and not ult == 877:
        print("Resultado:CONTESTAR")
    else:
        print("Resultado:NO CONTESTAR")