Ingresos=int(input("Ingrese sus ingresos totales: "))
print("valor correcto")
nacimiento=int(input("Ingrese su año de nacimiento: "))
print("Fecha Correcta")
hijos=int(input("ingrese cunatos hijos tiene: "))
print("Valor Correcto")
banco=int(input("ingrese cuantos años lleva en el banco: "))
print("Valor correcto")
civil=(input("ingrese su estado civil (S para soltero y C para casado): "))
civil.upper
vive=(input("ingrese donde vive (U para urbano y R para rural): "))
vive.upper
if(banco>10 and hijos>=1):
  print("APROBADO ")
elif(hijos>3 and nacimiento>=1900 and nacimiento<=1987 and civil=="c"):
   print("APROBADO ")
elif (Ingresos>2500000 and civil=="s" and vive=="u"):
    print("APROBADO ")
elif(Ingresos>3500000 and banco>=5):
    print("APROBADO ")
elif(Ingresos==450000 and nacimiento==1970 and hijos==1 and banco==11 and civil=="c" and vive=="r"):
  print("APROBADO")
while(vive=="r" and civil=="c" and hijos<2):
  print("APROBADO ")
  break