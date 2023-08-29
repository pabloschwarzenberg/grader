#Descomponer un número
c = True
while c: #Restriccion número de hasta 4 digitos
    n = int(input('Ingrese número: '))
    if ((n < 10000) and (n >=0)):
      c = False
    else:
      print ('Numero ingresado incorrecto')

if (n >= 1000):
  M = (str(n)[0:1])
  C = (str(n)[1:2])
  D = (str(n)[2:3])
  U = (str(n)[3:4])
  print(M+'M + '+C+'C + '+D+'D + '+U+'U')
elif ((n < 1000) and (n >= 100)):
  C = (str(n)[0:1])
  D = (str(n)[1:2])
  U = (str(n)[2:3])
  print(C+'C + '+D+'D + '+U+'U')
elif ((n < 100) and (n >= 10)):
  D = (str(n)[0:1])
  U = (str(n)[1:2])
  print(D+'D + '+U+'U')
else:
  print(str(n)+'U')     