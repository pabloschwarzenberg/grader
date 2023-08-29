#Aprobación de créditos
print("Hola , por favor ingrese los sgts. datos:")

i = int(input("Su ingreso: \n"))
an = int(input("Año de nacimiento: \n"))
n = int(input("Número de hijos: \n"))
pb = int(input("Años con nuestro banco: \n"))
ec = str(input("(S: soltero, C: casado): \n"))
s = str(input("(U: urbana, R: rural): \n"))
edad = 2020 - an

if pb > 10 and n >= 2:
    print("APROBADO")

elif pb > 5 and i > 3500000:
    print("APROBADO")

elif n > 3 and 45 >= edad >= 55 and ec == "C":
    print("APROBADO")

elif n < 2 and ec == "C" and s == "R":
    print("APROBADO")

elif s == "U" and ec == "S" and i > 2500000:
    print("APROBADO")

else:
    print("RECHAZADO")