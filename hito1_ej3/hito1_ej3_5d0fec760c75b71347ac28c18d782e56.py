#Aprobación de créditos
print("Programa Automatizado de Aprobacion de Creditos")
print("===============================================")
print("A continuacion rellene sus datos y verificaremos si es usted apto para la aprobacion del credito")
print("================================================================================================")

ingresos = int(input("Ingrese su Ingresos mensuales(en pesos): "))
años = int(input("Ingrese su año de nacimiento : "))
hijos = int(input("Ingrese su Número de hijos (en caso de no tener rellene con un cero): "))
pertenencia = int(input("Ingrese los años a los que ha pertenecido a nuestro Banco(Si es menos de 1 año,rellene con un cero): "))
civil = str(input("Ingrese su estado Civil (S: soltero, C: casado): "))
vivienda = str(input("Ingrese su ambiente de estadia (U: urbano, R: rural): "))

print("Espere un momento mientras procesamos su soliitud")
print("=================================================")

if pertenencia >= 10 and hijos >= 2:
    print("APROBADO")

elif civil == "C" and  hijos >= 3 and 1965>=años<=1975:
    print("APROBADO")

elif ingresos >= 2500000 and civil == "S" and vivienda == "U":
    print("APROBADO")

elif ingresos >= 3500000 and pertenencia >= 5:
    print("APROBADO")

elif vivienda == "R" and civil == "C" and hijos<=2:
    print("APROBADO")
