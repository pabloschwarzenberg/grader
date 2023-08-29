q = eval(input("Ingreso economico: "))
w = eval(input("año de nacimiento: "))
e = eval(input("Numero de niños: "))
a = eval(input("Años de pertenencia en el banco: "))
t = input("(S: soltero,C:casado):")
y = input("(U:urbano,R:rural): ")



if a > 10 and e >= 2:
    print("APROBADO")
elif t == "C" and e > 3 and (w >= 1965 and w <= 1975):
    print("APROBADO")
elif q > 2500000 and t == "S" and y == "U":
    print("APROBADO")
elif q > 3500000 and a >= 5:
    print("APROBADO")
elif y == "R" and t == "C" and e < 2:
    print("APROBADO")
else:
    print("no aprobado")
  