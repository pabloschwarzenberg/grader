#Aprobación de créditos
print("*Pedir un Pŕestamo*")
print("-----------------------------------")
print("Para solicitar un prestamo se requiere ingreso de los siguientes datos: Ingreso, edad, Numero de hijos, años de pertenencia al banco, Estado civil, vivienda.")
print("-----------------------------------")
ingreso = int(
    input("Digite su Ingreso en Pesos Chilenos: ") or "0")
edad = int(
    input("Digite su edad: ") or "0")
numero_hijos = int(
    input("Digite el numero de hijos que tiene: ") or "0")
anos_pertenencia_banco = int(
    input("Digite años de pertenencia al banco: ") or "0")
estado_civil = input(
    "Digite su estado civil [\"S\": soltero, \"C\": casado ]: ")
vivienda = input(
    "Digite si vive en campo o ciudad [\"U\": urbano, \"R\": rural ]: ")

# Se comprueba si el cliente cumple los requisitos del prestamo
credito_aprobado = True if ((anos_pertenencia_banco > 10 and numero_hijos >= 2) or (estado_civil == "C" and numero_hijos > 3 and edad >= 45 and edad <= 55) or (
    ingreso > 2500000 and estado_civil == "S" and vivienda == "U") or (ingreso > 3500000 and anos_pertenencia_banco > 5) or (vivienda == "R" and estado_civil == "C" and numero_hijos < 2)) else False

if (credito_aprobado):
    print("APROBADO")
else:
    print("RECHAZADO")
