#Aprobación de crédito
S="S"
C="C"
U="U"
R="R"
ingresos=eval(input("ingrese la cantidad de sus ingresos (en pesos): "))
nacimiento=eval(input("ingrese su Año de nacimiento: "))
edad=int(2020-nacimiento)
print("su edad es: ",edad)
hijos=eval(input("ingrese su número de hijos: "))
Añosbanco=eval(input("ingrese sus años de pertenencia a este banco: "))
Estadocivil=input("ingrese su estado civil. S(soltero) o C(casado): ")
sector=input("ingrese Si vive en zona U (urbana) o R (rural): ")
if(Añosbanco>10 and hijos>1):
  print("APROBADO")
elif(Estadocivil==C and hijos>=2 and 55>=edad>=45):
  print("APROBADO")
elif(ingresos>2500000 and Estadocivil==S and sector==U):
  print("APROBADO")
elif(ingresos>3500000 and Añosbanco>5):
  print("APROBADO")
elif( Estadocivil==C and sector==R and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")