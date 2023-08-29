#Descomponer un número
Numero = input()
Largo = len(Numero)
if Largo == 4:
  print(Numero[0]+"M + "+ Numero[1]+"C + "+ Numero[2]+"D + "+Numero[3]+"U")
if Largo == 3:
  print(Numero[0]+"C + "+ Numero[1]+"D + "+Numero[2]+"U")
if Largo == 2:
  print(Numero[0]+"D + "+Numero[1]+"U")
if Largo == 1:
  print(Numero[0]+"U")