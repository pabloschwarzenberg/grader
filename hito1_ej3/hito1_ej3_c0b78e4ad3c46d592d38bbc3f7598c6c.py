#Aprobación de créditos
##Programa Banco
ingresos = int(input("Ingresos: "))
año_nacimiento = int(input("Año de nacimiento: "))
num_hijos = int(input("¿Cuantos hijos tiene?: "))
año_pertenencia_banco = int(input("Años de pertenencia del banco: "))
estado_civil = input("Estado civil: ")
residencia = input("¿Vives en campo(R) o ciudad(U)?: ")

aprobado = False

if año_pertenencia_banco > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
    aprobado = True
elif ingresos > 2500000 and estado_civil == "S" and residencia == "U":
    aprobado = True
elif ingresos > 3500000 and año_pertenencia_banco > 5:
    aprobado = True
elif residencia == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")      