#Aprobación de créditos
ingreso = int(input("Ingrese sus ingresos en pesos:  "))
año = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese la cantidad de hijos: "))
pertenencia = int(input("Ingrese la cantidad de años de pertenencia al banco: "))
estado = str(input("Ingrese su estado civil (S: Soltero, C: casado): "))
vivienda = str(input("Ingrese su vivienda (U: Urbano, R: Rural): "))
soltero = estado == "S"
casado = estado == "C"
urbano = vivienda == "U"
rural = vivienda == "R"

#REGLAS DEL BANCO

Q = ((pertenencia >= 10) and (hijos >= 2))
W = ((casado) and (hijos > 3) and (año >= 1977) or (año <= 1967))
E = ((ingreso > 2500000) and (soltero) and (urbano))
R = ((ingreso > 3500000) and (pertenencia > 5))
T = ((rural) and (casado) and (hijos < 2))

if ((Q) or (W) or (E) or (R) or (T)):
    print("APROBADO")

else:
    print("RECHAZADO")     