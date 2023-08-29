numero=int(input("Ingrese númeror :"))
hora=int(input("Ingrese la hora de la llamada :"))

numero_fin=numero%1000
numero_ini=(numero - numero%100000)/100000
contestar="CONTESTAR"


if  hora>=0 and hora<=7:
    contestar="CONTESTAR"
elif  hora>7 and hora<14:
    if numero_fin==909:
        contestar="CONTESTAR"
    else:contestar="NO CONTESTAR"
elif  hora>17 and hora<=19:
    if numero_ini==877:
        contestar="NO CONTESTAR"
    else:contestar="CONTESTAR"
else: contestar="NO CONTESTAR"


print(contestar)