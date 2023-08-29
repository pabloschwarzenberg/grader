#Aprobación de créditos
x = int(input("ingreso: "))
y = int(input("año de nacimiento: "))
hi = int(input("numeros de hijos: "))
ap = int(input("años de pertenencia al banco: "))
e = input("estado civil, soltero(S) o casado(C): ")
v = input("vive en campo(U) o ciudad(R): ")

if ap > 10 and hi >= 2:
    print("APROBADO")
elif e == "C" and hi > 3 and y < 1976 and y > 1966:
    print("APROBADO")
elif x > 2500000 and e == "S" and v == "R":
    print("APROBADO")
elif x > 3500000 and ap > 5:
    print("APROBADO")
elif v == "R" and hi < 2:
    print("APROBADO")
else:
    print("RECHAZADO")