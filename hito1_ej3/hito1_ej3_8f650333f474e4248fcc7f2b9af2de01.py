#Aprobación de créditos
ingreso = int(input())
ano = int(input())
hijos = int(input())
anobanco = int(input())
civil = input()
casa = input()
edad = 2021 - ano
a = "APROBADO"
if anobanco > 10 and hijos > 2:
    print(a)
elif civil == "c" and hijos > 3 and 45 <= edad <= 55:
    print(a)
elif ingreso >= 2500000 and civil == "S" and casa == "U":
    print(a)
elif ingreso >= 3500000 and anobanco > 5:
    print(a)
elif casa == "R" and civil == "C" and hijos < 2:
    print(a)
else:
    print("rechazado")    