#Aprobación de créditos
ing=eval(input("Digite sus ingresos en pesos: "))
anio=eval(input("Ingrese su anio de nacimiento: "))
nh=eval(input("Ingrese numero de hijos: "))
ab=eval(input("Ingrese anios de pertenencia al banco: "))
ec=str(input("Ingrese estado civil's',soltero o 'c',casado: "))
cc=str(input("Ingrese donde vive'u',urbano o 'r',rural: "))
if ab>10 and nh>1:
    print("Aprobado")
elif ec=="c" and nh>2 and (anio<1977 and anio>1965):
    print("Aprobado")
elif ing>2500000 and ec=="s" and cc=="u":
    print("Aprobado")
elif ing>3500000 and ab>5:
    print("Aprobado")
elif cc=="r" and ec=="c" and nh<2:
    print("Aprobado")
else:
    print("Rechazado")