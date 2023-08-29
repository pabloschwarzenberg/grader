#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if(hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif(hora >= 8 and hora <= 14):
    C = str(numero)
    D = C[5:8]
    F = int(D)
    if(F == 909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(hora >= 17 and hora <= 19):
    C = str(numero)
    D = C[0:3]
    F = int(D)
    if(F == 877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif(hora >= 19 and hora <= 24):
    print("NO CONTESTAR")