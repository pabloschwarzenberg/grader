#Aprobación de créditos
i=eval(input("digite su ingreso: "))
an=eval(input("año de nacimiento: "))
nh=eval(input("¿cuantos hijos tiene?: "))
p=eval(input("años de pertenencia al banco: "))
ec=input("estado civil(S si es soltero, C si es casado): ")
cc=input("Donde vive(U zona urbana, R rural): ")
if p>=10 and nh>=2:
  print("APROBADO")
elif ec=="C" and nh>=3  and 1965<=an<=1975:
  print("APROBADO")
elif i>2500000 and ec=="S" and cc=="U":
  print("APROBADO")
elif i>3500000 and p>=5:
  print("APROBADO")
elif cc=="R" and ec=="C" and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")