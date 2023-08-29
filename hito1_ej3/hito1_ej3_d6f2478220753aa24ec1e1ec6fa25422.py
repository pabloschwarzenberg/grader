R="R"
r="r"
U="U"
u="u"
C="C"
c="C"
s="s"
S="S"
ingresos=float(input("ingrese su ingresos(en CLP):"))
nacimiento=int(input("ingrese su año de nacimiento:"))
hijos=int(input("ingrese su numero de hijos:"))
añosbanco=int(input("ingrese los años que lleva en el banco:"))
civil=eval(input("ingrese su estado civil(Soltero=S y Casado=C):"))
vive=eval(input("usted vive en campo o ciudad(Campo=R ciudad=U):"))
edad=2020-nacimiento
if(añosbanco>10 and hijos>1):
    print("APROBADO")
elif(civil=="C" and hijos>3 and 44>edad<56):
    print("APROBADO")
elif(ingresos>2500000 and civil=="S" and vive=="U"):
    print("APROBADO")
elif(ingresos>3500000 and añosbanco>5):
    print("APROBADO")
elif(vive=="R" and civil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")