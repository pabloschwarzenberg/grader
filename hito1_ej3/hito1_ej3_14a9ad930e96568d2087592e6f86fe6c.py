#Aprobación de créditos
print("Programa para aprobar o rechazar credito")
a = int(input("Introduce tu ingreso en pesos: "))
b = int(input("Introduce tu año de nacimiento: "))
c = int(input("Introduce tu número de hijos: "))
d = int(input("Introduce tus años de pertenencia al banco: "))
e = (input("Introduzca su estado civil (S: soltero, C: casado)"))
f = (input("Introduzca si vive en campo o ciudad (U: urbano, R: rural)"))
edad = 2022 - b
if d > 10 and c >= 2:
    print("APROBADO")
elif e == "C" or e == "c" and c > 3 and 45 < edad < 55:
    print("APROBADO")
elif 2500000 < a and e == "S" or e =="s" and f == "U" or f == "u":
    print("APROBADO")
elif 3500000 < a and d > 5:
    print("APROVADO")
elif f == "R" or f == "r" and e == "C" or e == "c" and 2 > c:
    print("APROBADO")
else:
    print("RECHAZADO")