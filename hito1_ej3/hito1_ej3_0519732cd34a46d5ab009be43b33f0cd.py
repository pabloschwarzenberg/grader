#Aprobación de créditos
ingreso=int(input("Ingrese sueldo: "))
años=int(input("Ingrese año nacimiento: "))
hijos=int(input("Ingrese cantidad de hijos: "))
años_banco=int(input("Ingrese años en el banco: "))
civil=input("Ingrese su estado civil, 'S': soltero / 'C': casado: ")
lugar=input("Ingrese donde vive, 'U': urbano / 'R': rural: ")
año=20222-años
if años_banco>10 and hijos>=2:
   print("APROBADO")
elif civil=="C" or civil=="c" and hijos>3 and año<55 and año>45:
   print("APROBADO")
elif ingreso>2500000 and civil=="S" or civil=="s" and lugar=="U" or lugar=="u":
   print("APROBADO")
elif ingreso>3500000 and años_banco>5:
   print("APROBADO")
elif lugar=="R" or lugar=="r" and civil=="C" or civil=="c" and hijos<2:
   print("APROBADO")
else:
   print("RECHAZADO")