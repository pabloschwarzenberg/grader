print("Aprobación de Créditos: ")

ingreso = int(input("Escribir en CLP (pesos chilenos):  "))
año = int(input("Escribir año de nacimiento:"))
hijos = int(input("Escribir número de hijos: "))
pertenencia = int(input("Escribir cantidad de años de pertenencia al banco: "))
estado = str(input("Escriba u estado civil (S: Soltero, C: casado): "))
vivienda = str(input("Escribir estado de su vivienda (U: Urbano, R: Rural): "))

soltero = estado == "S"
casado = estado == "C"
urbano = vivienda == "U"
rural = vivienda == "R"


a = ((pertenencia >= 10) and (hijos >= 2))
b = ((casado) and (hijos > 3) and (año >= 1977) or (año <= 1967))
c = ((ingreso > 2500000) and (soltero) and (urbano))
d = ((ingreso > 3500000) and (pertenencia > 5))
e = ((rural) and (casado) and (hijos < 2))

if ((a) or (b) or (c) or (d) or (e)):
    print("APROBADO")
else:
    print("RECHAZADO")
    