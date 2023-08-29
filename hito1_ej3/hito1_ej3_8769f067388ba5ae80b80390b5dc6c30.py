#Aprobación de créditos
Ingreso = int(input("Ingrese un monto: "))
Ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese número de hijos: "))
Pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
Estado = input("Ingrese su estado civil (S: soltero, C: casado): ")
Residencia = input("Ingrese su lugar de residencia (U: urbano, R: rural): ")
Edad = 2020 - Ano_nacimiento
S = 1
C = 2
U = 3
R = 4
if (Pertenencia>=10 and Hijos>=2):
    Resultado = "APROBADO"
elif (Estado==2 and Hijos>3 and 45<=Edad>=55):
    Resultado = "APROBADO"
elif (Ingreso>250000 and Estado==1 and Residencia==3):
    Resultado = "APROBADO"
elif (Ingreso>350000 and Pertenencia>5):
    Resultado = "APROBADO"
elif (Residencia==4 and Estado==2 and Hijos<2):
    Resultado = "APROBADO"
else:
    Resultado = "RECHAZADO"
print("Su crédito ha sido: ",Resultado)