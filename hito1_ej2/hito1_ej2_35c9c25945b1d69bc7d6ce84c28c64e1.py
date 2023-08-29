#Contestador de celular
numero = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese hora de la llamada:"))
terminacion = numero%1000
empezada = numero//100000

if 0 <= hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14:
    if terminacion == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if empezada == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR") 
elif hora >= 19:
    print("NO CONTESTAR")
    

      