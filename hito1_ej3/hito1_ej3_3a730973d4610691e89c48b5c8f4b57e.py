a=int(input("Ingreso"))
b=int(input("Año de nacimiento"))
c=int(input("Número de hijos"))
d=int(input("Años de pertencia al banco"))
e=input("Estado civil(S o C)")
f=input("Vive en campo (R) o cuidad (U)")


if b>10 and c>=2:
      print("APROBADO")

else:
      print("RECHAZADO")

if e=="C" and c>3 and 1962<=b<=1972:
      print("APROBADO")

else:
      print("RECHAZADO")

if a>2500000 and e=="S" and f=="U":
      print("APROBADO")

else:
      print("RECHAZADO")

if a>3500000 and d>5:
      print("APROBADO")

else:
      print("RECHAZADO")

if f=="R" and e=="C" and c<2:

    print("APROBADO")

else:
      print("RECHAZADO")


