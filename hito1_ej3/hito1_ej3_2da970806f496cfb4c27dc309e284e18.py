casado="C"
soltero="S"
campo="R"
ciudad="U"

print("Ingrese los siguientes datos:")
a=int(input("Ingreso en pesos:"))
b=int(input("Año de nacimiento:"))
c=int(input("Numero de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=input("Si estas soltero, ingresa S, si estas casado ingresa C:")
f=input("Vive en campo o en ciudad(U=Urbano, R=Rural):")

if e==casado and c>3 and 1961<b<1971:
    print("APROBADO")
elif d>10 and c>=2:
    print("APROBADO")
elif a>2500000 and e==soltero and f==ciudad:
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f==campo and e==casado and c<2:
    print("APROBADO")
else:
    print("REPROBADO")
      