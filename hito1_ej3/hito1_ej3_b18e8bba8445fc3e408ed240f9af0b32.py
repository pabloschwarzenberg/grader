#aprobacion de creditos
ingreso=int(input("ingresos (en clp): "))
añonacimiento=int(input("ingrese su año de nacimiento : "))
hijos=int(input("cuantos hijos tiene?: "))
añobanco=int(input("¿cuantos años ha pertenecido a este banco?: "))
estado=input("estado civil acutal (s=soltero, c=casado): ")
vivienda=input("¿usted vive en campo(u) o en ciudad(r)?: ")
años=añonacimiento-2021
if añobanco>10 and hijos>=2:
  print("APROBADO")
elif (estado=="c" or "C") and hijos>3 and años>=45 and años<=55:
  print("APROBADO")
elif ingreso>=2500000 and (estado=="s"or"S") and (vivienda=="r"or"R"):
  print("APROBADO")
elif ingreso>=3500000 and añobanco>5:
  print("APROBADO")
elif vivienda=="u"or"U" and estado=="c"or"C" and hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")