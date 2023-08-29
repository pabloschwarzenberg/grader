ingresos=int(input("Ingresos liquidos: "))
nacimiento=int(input("Su año de nacimiento es: "))
hijos=int(input("Número de hijos: "))
pbanco=int(input("Años de pertenencia al banco: "))
ecivil=input("Ingrese su estado civil ¨s¨ para soltero o ¨c¨ para casado: ").lower()
vive=input("Si vive en la cuidad digite ¨u¨ si vive en el campo  digite ¨r¨ : ").lower()
edad=2020-nacimiento
if (pbanco>=10 and hijos>=2) or ((ecivil=='c') and (hijos>=3) and (edad>=45 and edad<=55)) or (ingresos>=2500000 and ecivil=='s' and vive=='u') or (ingresos>=3500000 and pbanco>=5) or (vive=='r' and ecivil=='c'and hijos<2):
    print("APROBADO")
else:print("RECHAZADO")