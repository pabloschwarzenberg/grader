#Aprobación de créditos
i=float(input("ingrese su ingreso: "))
a=int(input("ingrese su año de nacimiento: "))
ni=int(input("ingrese el numero de hijos que tiene: "))
ab=int(input("ingrese los años que ha pertenecido al banco: "))
ec=input("ingrese su estado civil soltero(S) o casado(C): ")
coc=input("ingrese si vive en urbano(U) o rural(R):")

if ab>=10 and ni>=2:
  print("APROBADO")
elif ec=="C" and ni>=3 and a>1967 and a<1977:
  print("APROBADO")
elif i>2500000 and ec=="S" and coc=="U":
  print("APROBADO")
elif i>3500000 and ab>=5:
  print("APROBADO")
elif coc=="R" and ec=="C" and ni<=2:
  print("APROBADO")
else:
  print("RECHAZADO")