ingreso=int(input("ingresos (en clp): "))
anon=int(input("ingrese su año de nacimiento : "))
hijos=int(input("cuantos hijos tiene?: "))
anob=int(input("¿cuantos años ha pertenecido a este banco?: "))
estado=input("estado civil acutal (s=soltero, c=casado): ")
casa=input("¿usted vive en campo(u) o en ciudad(r)?: ")
edad=anon-2021
if anob>10 and hijos>=2:
  print("APROBADO")
elif (estado=="c" or "C") and hijos>3 and edad>=45 and edad<=55:
  print("APROBADO")
elif ingreso>=2500000 and (estado=="s"or"S") and (casa=="r"or"R"):
  print("APROBADO")
elif ingreso>=3500000 and anob>5:
  print("APROBADO")
elif casa=="u"or"U" and estado=="c"or"C" and hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")