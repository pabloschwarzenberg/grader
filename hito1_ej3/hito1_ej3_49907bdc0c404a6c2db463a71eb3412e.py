#Aprobación de créditos
ingresos=eval(input("ingres sus ingresos"))
año=eval(input("ingrese su año de nacimiento"))
hijos=eval(input("ingrese el numero de hijos"))
añosbanco=eval(input("sus años de pertenencia en el banco"))
estadocivil=input("usted esta s=soltero c=casado")
casa=input("usted vive en sona u=urbana r=rural")
añosisi=2021-año
if(añosbanco>10 or hijos>=2):
    print("APROBADO")
elif(estadocivil=="c" or añosisi<=45 or añosisi>=55 or hijos>3):
    print("aprobado")
elif(ingresos>2500000 or estadocivil=="s" or casa=="u"):
    print("aprobado")
elif(ingresos>3500000 or añosbanco>5):
    print("aprobado")
elif(casa=="r" or estadocivil=="c" or  hijos<2):
    print("aprobado")
else:
    print("no se aprueba el credito")