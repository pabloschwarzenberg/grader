S = "Soltero"
C = "casado"
U = "Urbano"
R = "Rural"
ingresos = int(input("Escriba sus ingresos en pesos chilenos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos: "))
years = int(input("Ingrese la cantidad de años en las que ha sido cliente del banco: "))
civil = str(input("Ingrese su estado civil (Soltero=S y Casado=C): "))
hogar = str(input("Ingrese si su domicilio es rural o urbano. R=Rural y U=Urbano: "))
if(years > 10) and (hijos >= 2):
    print("APROBADO")
elif(civil == C) and (hijos > 3) and ((nacimiento >= 1967) or (nacimiento <= 1977)):
    print("APROBADO")
elif(ingresos > 2500000) and ((civil == S) and (hogar == U)):
    print("APROBADO")
elif(ingresos > 3500000) and (years > 5):
    print("APROBADO")
elif(hogar == R) and (civil == C) or (hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")    