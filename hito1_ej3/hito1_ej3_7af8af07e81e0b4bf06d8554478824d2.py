Ingreso=int(input("Ingrese sus ganancias en pesos "))
AñoDeNacimiento=int(input("Ingrese su año de nacimiento "))
EdadActual=2021-AñoDeNacimiento
NumeroDeHijos=int(input("Ingrese el numero de hijos que tiene "))
AñosDePertenenciaAlBanco=int(input("Ingrese el numero de años que lleva en este banco "))
EstadoCivil=input("Ingrese su estado civil actualmente,(S: soltero, C, casado) ")
CampoCiudad=(input("Ingrese si usted vive en campo o cuidad (U: urbano, R: rural) "))

U="urbano"
R="rural"

S="soltero"
C="casado"

if(AñosDePertenenciaAlBanco>10)and(NumeroDeHijos>=2):
  print("APROBADO")
elif("C")and(NumeroDeHijos>3)and(45<=EdadActual<=55):
  print("APROBADO")
elif(Ingreso>2500000)and(S)and(U):
  print("APROBADO")
elif(Ingreso>3500000)and(AñosDePertenenciaAlBanco>5):
  print("APROBADO")
elif(R)and(C)and(NumeroDeHijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")