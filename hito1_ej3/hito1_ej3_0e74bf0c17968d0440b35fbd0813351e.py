#Aprobación de créditos

#Ingreso de datos

ing = float(input("Ingrese su ingreso mensual en pesos: "))
anos = int(input("Ingrese su año de nacimiento: "))
nhijos = int(input("Ingrese el número de hijos: "))
apertinencia = int(input("Ingrese los años de pertenencia al banco: "))
ecivil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubi = input("Ingrese su ubicación (U para urbano, R para rural): ")

#Operacion

if apertinencia > 10 and nhijos >= 2:
    resultado = "APROBADO"
elif ecivil == "C" and nhijos > 3 and 45 <= (2023 - anos) <= 55:
    resultado = "APROBADO"
elif ing > 2500000 and ecivil == "S" and ubi == "U":
    resultado = "APROBADO"
elif ing > 3500000 and apertenencia > 5:
    resultado = "APROBADO"
elif ubi == "R" and ecivil == "C" and nhijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

#Resultado
print("Resultado:", resultado)
