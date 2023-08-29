#Aprobación de créditos
ingreso=int(input("ingrese sueldo: "))
años=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese la cantidad de hijos: "))
años_banco=int(input("Ingrese sus años en el banco: "))
civil=input("Ingrese su estado civil, 'S': Soltero / 'C': Casado: ")
lugar=input("Ingrese donde vive, 'U': Urbano / 'R': Rural: ")
año=2022-años
if años_banco >10 and hijos >= 2:
    print("APROBADO")
elif civil =="C" or civil=="c" and hijos>3 and año<55 and año>45:
    print("APROBADO")
elif ingreso >2500000 and civil=="s" or civil =="S" and lugar =="U" or lugar=="u":
    print("APROBADO")
elif ingreso >3500000 and años_banco >5:
    print("APROBADO")
elif lugar=="R" or lugar=="r" and civil =="C" or civil=="c" and hijos<2:
    print("APROBADO")
else: print("RECHAZADO")