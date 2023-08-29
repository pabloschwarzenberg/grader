#Aprobación de créditos
ingreso = int(input())
edad = 2023 - int(input()) 
hijos = int(input())
año_banco = int(input())
estado = input()
localidad = input()

if (año_banco >= 10 and hijos >= 2) or (estado == 'C' and hijos > 3 and edad >= 45 and edad >= 55) or (ingreso >= 2500000 and estado == 'S' and localidad == 'U') or (ingreso == 3500000 and año > 5) or (localidad == 'R' and estado == 'C' and hijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")