ingreso =eval(input("agregar ingreso: " ))
nacimiento =eval(input("ingrese año de nacimiento: " ))
hijos =eval(input("ingrese numero de hijos: "))
pertenenciaBanco =eval(input("ingrese años de pertenencia al banco: "))
estadocivil =input("ingrese estado civil  (S: soltero, C, casado):")
residencia=input("ingrese residencia (U: urbano, R: rural):" )
edad=2022 - nacimiento

if pertenenciaBanco >10 and hijos >= 2:
    print("APROBADO")
elif estadocivil == "C" and hijos >3 and edad >=45 and edad <=55:
    print("APROBADO")
elif ingreso >=2500000 and estadocivil == "S" and residencia == "U":
    print("APROBADO")
elif ingreso >=3500000 and pertenenciaBanco >= 5:
    print("APROBADO")
elif residencia == "R" and estadocivil == "C" and hijos <=2:
    print("APROBADO")
else :
    print("RECHAZADO")
