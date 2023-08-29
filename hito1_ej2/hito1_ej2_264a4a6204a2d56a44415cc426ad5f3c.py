#Contestador de celular
N_T = str(input("Ingrese el numero telefonico: "))
Hora = int(input("Ingrese la hora del llamado (marcar la hora desde las 0hrs a 23hrs): "))

if((Hora >= 0) and (Hora < 7)) or ((Hora >= 7) and (Hora < 14) and (N_T[5:] == str(909))) or ((Hora >= 17) and (Hora < 19) and not(N_T[:-5] == str(877))):
    print("Contestar")
else:
    print("no contestar")
