#Aprobación de créditos
ingresos = int(input("¿Cuantos ingresos posee?: $"))
nacimiento = int(input("Ingrese su AÑO de nacimiento: "))
edad = (2020 - nacimiento)
hijos = int(input("¿Cuantos hijos tiene?: "))
pertenencia = int(input("¿Cuantos años lleva perteneciendo al banco?: "))
ECivil = str(input("Ingrese su estado civil (soltero(S) o casado(C): "))
S = "soltero"
C = "casado"
vivienda = str(input("¿En que zona vive? (rural(R) o urbana(U): "))
R = "rural"
U = "urbana"
if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif ECivil == C and hijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingresos > 2500000 and ECivil == S and vivienda == U:
    print("APROBADO")
elif ingresos > 350000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == R and ECivil == C and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      