#Descomponer un número
numero=str(input('ingrese un numero de hasta 4 digitos:'))
if 0<=int(numero)<9:
  print(str(numero)+'U')
if 10<=int(numero)<99:
  D=int(numero[0:1])
  U=int(numero[1])
  print(str(D)+'D+'+str(U)+'U')
if 100<=int(numero)<999:
  C=int(numero[0:1])
  D=int(numero[1:2])
  U=int(numero[2])
  print(str(C),'C+',str(D),'D+',str(U),'U')
if 1000<=int(numero)<9999:
  M=int(numero[0:1])
  C=int(numero[1:2])
  D=int(numero[2:3])
  U=int(numero[3])
  print(str(M),'M+',str(C),'C+',str(D),'D+',str(U),'U')