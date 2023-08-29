#Aprobación de créditos
print("Debe ingresar los siguientes datos para evaluar su credito")
i = eval(input("Ingrese sus ingresos: "))
an = eval(input("Ingrese su año de nacimiento: "))
nh = eval(input("Ingrese su numero de hijos: "))
ab = eval(input("Ingrese los años de pertenencia al banco: "))
ec = input("Si está soltero ingrese S y si está casado C: ")
cc = input("Si vive en campo ingrese R y si vive en ciudad U: ")
f=2020-an
if ab>10 and nh>=2:
    print("APROBADO")
elif ec=="C" and nh>3 and 45<=f<=55:
    print("APROBADO")
elif i>2500000 and ec=="S" and cc=="U":
    print("APROBADO")
elif i>3500000 and ab>5:
    print("APROBADO")
elif cc=="R" and ec=="C" and nh<2:
    print("APROBADO")
else:
    print("RECHAZADO")
          