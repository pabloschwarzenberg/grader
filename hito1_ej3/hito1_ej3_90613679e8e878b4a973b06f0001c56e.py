#Aprobación de créditos
ingresos = int(input("Ingreso mensual en pesos chilenos(CLP): "))
año = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
años_bank = int(input("Cantidad de años como cliente del banco: "))
civil = input("Estado civil (escriba S para soltero o C para casado): ")
vive = input("¿Usted vide en campo o ciudad? (U para urbano o R para rural): ")
#Constante
año_actual = 2021
edad = año_actual-año

#Proceso
if años_bank >= 10 and hijos >= 2:
    print("APROBADO")
elif  civil == "C"or"c" and hijos >= 3 and edad >= 45 and edad <=55:
    print("APROBADO")
elif ingresos >= 2500000 and civil == "S" or "s" and vive == "u" or "U":
    print("APROBADO")
elif ingresos >= 3500000 and años_bank >= 5:
    print("APROBADO")
elif vive == "R" or "r" and civil == "C" or "c" and hijos >=2:
    print("APROBADO")
else:
    print("RECHAZADO")
      