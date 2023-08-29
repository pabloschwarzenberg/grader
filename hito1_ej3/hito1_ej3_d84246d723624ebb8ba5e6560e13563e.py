#Aprobación de créditos
ingreso = int(input("Digite su ingreso mensual:"))
fechaNac = int(input("Digite su año de nacimiento Ej: '2021':"))
hijos = int(input("Digite la cantidad de hijos que tiene:"))
anos_banco = int(input("Digite años de pertenencia en el banco:"))
Estado_Civil = str(input("Digite su estado civil Ej: 'S' si es soltero, 'C' si es casado:"))
residencia = str(input("Digite si vive en campo o ciudad Ej: 'U' si es Urbano, 'R' si es Rural "))

res = residencia.upper()
est = Estado_Civil.upper()

ano = 2021

anos_user = ano - fechaNac

if anos_user > 45 and anos_user <=55 and hijos >= 3 and est == "C" and ingreso >= 2500000 and res == "U":
    print("APROBADO ")


elif anos_banco > 5 and ingreso >= 3500000:
    print("APROBADO ")

elif anos_banco > 10 and hijos >= 2:

    print("APROBADO ")


elif res == "R" and est == "C" and hijos <= 2:

    print("APROBADO ")

else:
    print("RECHAZADO  ")