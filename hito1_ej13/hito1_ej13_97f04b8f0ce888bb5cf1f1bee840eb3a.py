#Factores Primos
Numero = int(input())

for Divisor in range(2,Numero+1):
  if (Numero%Divisor) == 0:
    Primo = True
    for D in range(2,Divisor):
      Res = Divisor%D
      if Res == 0:
        Primo = False
    if Primo == True:
      print(Divisor)