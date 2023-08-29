i=float(input("Digite sus ingresos 'en pesos' :$"))
anos_n=float(input("Ingrese Año de nacimiento:"))
h=float(input("Ingrese Número de hijos:"))
anos_p=float(input("Ingrese año de pertenecia al banco:"))
e_civil=input('Ingrese "S": soltero, o "C": casado')
S=("soltero")
C=("casado")
v=input('Ingrese "U": urbano, "R": rural')
U=("urbano")
R=("rural")
anos=2020-anos_n
if anos_p > 10 or h >=2:
    print("APROBADO")
elif e_civil==C  and h > 3 and anos >=45 and anos<=55:
    print("APROBADO")
elif i> 2500000 and e_civil==S and v==U:
    print("APROBADO")
elif i> 3500000 and anos_p > 5:
    print("APROBADO")
elif v==R and e_civil==C or h < 2 :
    print("APROBADO")
else:
    print("RECHAZADO")

