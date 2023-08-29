#aprobacion de creditos
IP = int(input("indique su ingreso en pesos: "))
AN = int(input("indique su fecha de nacimineto: "))
NH = int(input("indique su numero de hijos: "))
APB = int(input("indique antiguiedad como cliente del banco: "))
EC = input("indique si es (S) para soltero y (C) para casado: ")
CC = input("indique (U) para ciudad y (R) para campo: ")
AÑOS = 2022
k = AÑOS - AN

if APB >= 10 and NH >= 2:
    print("APROBADO")
elif  NH > 3 and k > 45 and k < 55:
    print("APROBADO")

elif IP > 2500000 and "S" in EC and "U" in CC:
    print("APROBADO")

elif IP > 3500000 and APB > 5:
    print("APROBADO")

elif "R" in CC and "C" in EC and NH < 2:
    print("APROBADO")
else:
    print("NO APROBADO")
      