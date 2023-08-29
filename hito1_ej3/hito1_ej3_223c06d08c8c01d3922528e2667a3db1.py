#Aprobación de créditos
ing = int(input("Ingresos: "))
anon = int(input("Ano de nacimiento: "))
edad = 2021 - anon
hijo = int(input("Numero de hijos: "))
anob = int(input("Anos en el banco: "))
est = str(input("Ingrese su estado civil con una (S) para soltero y una (C) para casado: "))
vive = str(input("Ingrese si vive en una zona urabana (U) o una sona rural (R)"))
print("Bien ahora comprobaremos para ver si cumple las condiciones para el credito.")
if (anob >= 10) and (hijo >= 2):
    print("APROBADO")
elif (est == str("C")) and (hijo >= 3) and (edad >= 45) and (edad <= 55):
    print("APROBADO")
elif (ing >= 250000) and (est == str("S")) and (vive == str("U")):
    print("APROBADO")
elif (ing >= 350000) and (anob >= 5):
    print("APROBADO")
elif (vive == str("R") and (est == str("C")) and (hijo <= 2)):
    print("APROBADO")
else:
    print("RECHAZADO")