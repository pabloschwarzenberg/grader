IP = int(input("Indique su ingreso en pesos: "))
AN = int(input("Indique su fecha de nacimineto: "))
NH = int(input("Indique su numero de hijos: "))
APB = int(input("Indique antiguiedad como cliente del banco: "))
EC = input("Indique si es (S) para soltero y (C) para casado: ")
CC = input("Indique (U) para ciudad y (R) para campo: ")
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