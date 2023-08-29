#Contestador de celu hora = int(input("Ingrese la hora de la llamada:"))
n_fono = str(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
if(hora >= 0 and hora <= 7):
    print("CONTESTAR")
if(hora < 14):
    if(n_fono[5:8] == str(909)):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(hora >= 17 and hora <= 19):
    if(n_fono[5:8] == str(877)):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(hora > 19 and hora < 23):
    print("NO CONTESTAR")