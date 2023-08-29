I=int(input("Ingres su sueldo: "))
ano=int(input("Año de nacimiento: "))
nh=int(input("Numero de hijos: "))
anob=int(input("Año en el banco: "))
ec=input("Soltero(S) o casado(C): ")
coc=input("Urbano(U) o Rural(R): ")
edad=2020-ano
if(anob>10 and nh>=2):
  print("APROBADO")
else:
  if(ec=="C" and nh>3 and 45<edad and edad<55):
    print("APROBADO")
  else:
    if(I>2500000 and ec=="S" and coc=="U"):
      print("APROBADO")
    else:
      if(I>3500000 and anob>5):
        print("APROBADO")
      else:
        if(coc=="R" and ec=="C" and nh<2):
          print("APROBADO")
        else:
          print("REPROBADO")
         