#Contestador de celular
numero = str(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de llamada: "))
if hora > 0 and hora < 7:
    print("CONTESTAR")
elif hora > 19 and hora <= 23:
    print("NO CONTESTAR")
elif hora > 7 and hora < 14 and numero[-3] == '9' and numero[-2] == '0' and numero[-1] == '9':
    print("CONTESTAR")
elif hora > 7 and hora < 14 and numero[-3] != '9' and numero[-2] != '0' and numero[-1] != '9':
    print("NO CONTESTAR")
elif hora > 17 and hora < 19 and numero[0] == '8' and numero[1] == '7' and numero[2] == '7':
    print("NO CONTESTAR")
elif hora > 17 and hora < 19 and numero[0] != '8' and numero[1] != '7' and numero[2] != '7':
    print("CONTESTAR")     