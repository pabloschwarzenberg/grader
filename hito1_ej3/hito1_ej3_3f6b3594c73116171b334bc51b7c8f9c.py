#Aprobación de créditos
i=int(input("digite sus ingresos: "))
a=int(input("ingrese su año de nacimiento: "))
nh=int(input("ingrese el numero de hijos: "))
p=int(input("años de permanencia en el banco: "))
e=input("estado civil (S:soltero,C:casado): ")
uor=input("vive en el campó o ciudad (U:urbano,R:rural): ")
if p >10 and nh>=2:
    print("APROBADO")
if e=="C" and nh > 3 and a>=1966 and a<=1976:
    print("APROBADO")
if i>2500000 and e=="S" and uor=="U":
    print("APROBADO")
if i>3500000 and p> 5:
    print("APROBADO")
if uor=="R" and e=="C" and nh<2:
    print("APROBADO")
else:
    print("RECHAZADO")