C = ""
S = ""
R = ""
U = ""

ingreso = int(input("Indique su ingreso en pesos: "))
nacimiento = int(input("Indique su año de nacimiento: "))
hijos = int(input("Cantidad de hijos: "))
años = int(input("Años perteneciendo al banco: "))
estado = input("Estado civil: ")
vivienda = input("¿Vive en zona urbana o rural?: ")



if(años > 10):
  print("APROBADO")
elif(estado == C and hijos >=2 and nacimiento >= 1975 or nacimiento <= 1985):
  print("APROBADO")
elif(ingreso > 2500000 and estado == S and vivienda == C):
   print("APROBADO")
elif(ingreso > 3500000 and años > 5):
   print("APROVADO")
elif(vivienda == R and estado == C and hijos < 2):
   print("APROBADO")
else:
   print("REPROBADO")

casado = C
soletro = S
rural = R
urbana = U
