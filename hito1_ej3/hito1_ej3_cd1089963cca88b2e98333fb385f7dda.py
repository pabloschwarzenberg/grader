#Aprobación de créditos
ING=int(input("ingres su ingreso en pesos: "))
BRT=int(input("ingrese su año de nacimiento: "))
NDH=int(input("ingrese la cantidad de hijos que posea: "))
ADAB=int(input("ingrese los años que pertenece al banco: "))
EC=input("esta casado [C] o soltero [S]?: ")
LDV=input("usted vive en un lugar rural [R] o urbano [U]: ")
AGE=2020-BRT
if (ADAB>10 and NDH>=2):
  print("APROBADO")
elif (EC==C and NDH>3 and AGE>=45 and AGE<=55):
  print("APROBADO")
elif(LDV=="U" and ING>2500000 and EC=="S"):
  print(APROBADO)
elif(EC=="C" and NDH<2 and LDV=="R"):
  print("APROBADO")
elif(ADAB>5 and ING>3500000):
  print("APROBADO")
else:
  print("RECHAZADO")

while not (BRT>=1900 and BRT<=2020):
  BRT=int(input("ERROR.... ingrese su año de nacimiento: "))
while not (EC=="S" or EC=="C"):
  EC=input("ERROR...esta casado [C] o soltero [S]?: ")
while not (LDV=="U" or LDV=="R"):
  LDV=input("ERROR...usted vive en un lugar rural [R] o urbano [U]: ")