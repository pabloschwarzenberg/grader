#Aprobación de créditos
i=int(input("ingrese su sueldo"))
e=int(input("ingrese su año de nacimiento"))
h=int(input("ingrese su número de hijos"))
ab=int(input("ingrese sus años de pertenencia en el banco"))
ec=input("ingrese su estado civil, s: soltero o c: casado")
coc=input("si vive en el campo ponga r y si vive en ciudad ponga u")
if ab>10 and h>=2:
    print("APROBADO")
elif ec=="C" and h>3 and 1972<e<1962:
   print("APROBADO")
elif i>2555000 and ec=="S" and coc=="U":
    print("APROBADO")
elif i>3500000 and ab>5:
    print("APROBADO")
elif coc=="R" and ec=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")