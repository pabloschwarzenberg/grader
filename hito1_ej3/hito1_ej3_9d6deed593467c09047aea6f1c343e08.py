#Aprobación de créditos
ingreso = int(input("Ingreso en $: "))
año = int(input("Año de Nacimiento: "))
hijos = int(input("Número de Hijos: "))
pertenencia = int(input("Años de Pertenencia al Banco: "))
estado = input("Estado Civil (S: soltero, C: casado): ")
vive = input("Vive en (U: urbano, R: rural): ")

edad = 2021 - año

if (pertenencia > 10 and hijos >= 2):
    print("APROBADO")
elif (estado == "C" and hijos > 3 and 45 <= edad <= 5):
    print("APROBADO")
elif (ingreso > 2500000 and estado == "S" and vive == "U"):
    print("APROBADO")
elif (ingreso > 3500000 and pertenencia > 5):
    print("APROBADO")
elif (vive == "R" and estado == "C" and hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")       