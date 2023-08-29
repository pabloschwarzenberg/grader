I = int(input("Favor de introducir sus ingresos en pesos:"))
AN = int(input("Favor de indicar su año de nacimiento"))
NDH = int(input("indiqueme cuantos hijos tiene ud:"))
AB = int(input("indiqueme desde cuando pertenece a nuestro banco"))
E = str(input("¿cual es su estado civil, C : casado y S : soltero"))
D = str(input("¿donde reside usted?, U:espacio urbano y R : espacio rural"))
              
if AB>10 and NDH>=2:
  print("APROBADO")
elif E == "C" and NDH>3 and AN>=1965 and AN<=1975:
  print("APROBADO")
elif I>=250000 and E == "S" and D == "U":
  print("APROBADO")
elif I>=350000 and AB>=5:
  print("APROBADO")
elif D == "R" and E=="C" and NDH<2:
  print("APROBADO")
else:
 print("REPROBADO")