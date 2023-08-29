#Aprobación de créditos
a = int(input("Coloque su ingreso en pesos sin punto: "))
b = int(input("Ingrese su edad: "))
c = int(input("Número de hijos: "))
d = int(input("ingrese su años de permanencia en el banco: "))
e = input("Ingres su estado civil(S:soltero o C:casado)")
f = input("¿Donde vive(U:urbano o R:rural): ")
if d > 10 and  c >= 2:
    print("APROBADO")
elif (e == "C" or e == "c") and c > 3 and (45>b or b<55):
    print("APROBADO")
elif a > 2500000 and (e == "S" or e=="s")and (f == "U" or f == "u"):
    print("APROBADO")
elif a > 3500000 and d > 5:
    print("APROBADO")
elif (f == "R" or f == "r") and (e == "C" or e == "c") and c < 2:
    print("APROBADO")
else:
    print("RECHAADO")