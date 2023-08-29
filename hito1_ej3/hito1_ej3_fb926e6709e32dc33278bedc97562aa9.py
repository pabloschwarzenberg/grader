#Aprobación de créditos
ingreso = int(input())
anonac = int(input())
hijos = int(input())
anopert = int(input())
ecivil = input()
ubic = input()

if anopert >= 10 and hijos >= 2:
    print("APROBADO")

if ecivil == "C" and hijos >= 3 and 1963 <= anonac <= 1973:
    print("APROBADO")

if ingreso >= 2500000 and ecivil == "S" and ubic == "U":
    print("APROVADO")

if ingreso >= 3500000 and anopert >= 5:
    print("APROBADO")

if ubic == "R" and ecivil == "C" and hijos <= 2 :
    print("APROBADO")

else:
    print("RECHAZADO")
