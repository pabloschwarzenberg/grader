i=float(input("Ingreso:"))
a=int(input("Ano de nacimiento:"))
n=int(input("Numero de hijos:"))
an=int(input("Anos de pertenencia al banco:"))
e=input("Ingrese estado civil s(soltero) o c(casado):")
v=input("Ingrese vivienda u(urbano) o r(rural):")
if an>10 and n>=2:
    print("APROBADO")
elif e=="S" and n>=3 and 45<=a<=55:
    print("APROBADO")
elif i>=2500000 and e=="S" and v=="U":
    print("APROBADO")
elif i>=3500000 and an>5:
    print("APROBADO")
elif v=="R" and e=="C" and n<2:
    print("APROBADO")
else:
    print("RECHAZADO")
