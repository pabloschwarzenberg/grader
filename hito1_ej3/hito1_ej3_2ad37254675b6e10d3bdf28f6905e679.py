#Aprobación de créditos
ing=int(input("ingresos"))
ano=int(input("año de nacimiento"))
edad=2017-ano
nh=int(input("numero de hijos"))
anoban=int(input("años en el banco"))
est=str(input("estado civil"))
if est=="c":
 est="c"
if est=="s":
  est="s"
lv=str(input("campo o ciudad"))
if lv=="r":
  lv="r"
if lv=="u":
   lv="u"
  
if anoban>10 and nh>=2 or "casado" and nh>3 and 45<edad<55:
 print("APROBADO")
if ing>2500000 and "soltero" and "u":
  print("APROBADO")
if ing>3500000 and anoban>5:
   print("aprobado")
if "c" and "r" and nh<2:
    print("APROBADO")
else:
   print("RECHAZADO")