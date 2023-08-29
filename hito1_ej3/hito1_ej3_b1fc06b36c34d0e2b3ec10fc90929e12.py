contador = 0
ingreso = int(input("ingreso en pesos: "))
anodenacimiento = int(input("año de nacimiento: "))
edad = 2021 - anodenacimiento
numerodehijos = int(input("numero de hijos: "))
anoenbanco = int (input("años en el banco: "))
estadocivil = str(input("estado civil, soltero (S) o casado (C): "))
S = "soltero"
C = "casado"
campociudad = str(input("vive en rural(R) o urbano (U): "))
R = "rural"
U = "urbano"

if 10 < anoenbanco:
    contador += 1
if estadocivil == C and 3<numerodehijos and 45<=edad<=55:
    contador +=1
if 2500000<ingreso and estadocivil == S and campociudad ==C:
    contador +=1
if 3500000<ingreso and 5<anoenbanco:
    contador +=1
if campociudad == R and estadocivil == C and numerodehijos<2:
    contador +=1
print (contador)
if 1<=contador:
    print("APROBADO")
else:
    print("RECHAZADO")

