#Gustavo Altez Irarrazabal
ingreso=float(input("What is your monthly Income?: "))
ano=int(input("Year of birth: "))
hijos=int(input("How Many kids?: "))
tiempoB=int(input("How many years with the bank?: "))
status=str(input("Are you married? [S]Single [C]Married"))
locacion=str(input("Where do you live?: [U]Urban [R]Rural: "))
Edad=2020-ano
nope=str("nope")
contador=nope
yup=str("yup")
while contador==nope:
 if tiempoB>10 and hijos>=2:
  print("APROBADO")
  contador=nope
 elif status==("C") and hijos>=3 and Edad>=45 and Edad<=55:
   print("APROBADO")
   contador=yup
 elif status==("S") and locacion==("U") and ingreso>2500000:
   print("APROBADO")
   contador=yup
 elif ingreso>3500000 and tiempoB>=5:
    print("APROBADO")
    contador=yup
 elif status==("C") and locacion==("R") and hijos<=2:
   print("APROBADO")
   contador=yup
 if nope==nope:
   print("RECHAZADO")
   contador=yup