#Contestador de celular
HORA = 0 
digitos = 0
while digitos!=8:
  NUMEROTF=int(input("ingrese un numero telefonico: "))
  digitos=len(str(NUMEROTF))
NUMEROT= (NUMEROTF//1000)*1000
RESTO= NUMEROTF-NUMEROT
RESTO1=NUMEROTF//100000
if digitos==8:
  HORA= int(input("ingresa hora de la llamada:  "))
if 7>=HORA>=0:
  print("CONTESTAR.")
if 14>=HORA:
  if RESTO!= 909:
    print("NO CONTESTAR")
  elif RESTO==909:
    print("CONTESTAR")
if 19>=HORA>=17:
  if RESTO1==877:
    print("NO CONTESTAR")
  elif RESTO1!=877:
    print("CONTESTAR")
if 19<HORA<23:
  print("NO CONTESTAR")