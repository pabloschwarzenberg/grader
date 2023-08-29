rut=int(input("Ingrese el rut: "))

A=(rut//10000000) * 3

B=((rut//1000000)%10) * 2

C=((rut//100000)%10) * 7

D=((rut//10000)%10) * 6

E=((rut//1000)%10) * 5

F=((rut//100)%10) * 4

G=((rut//10)%10) * 3

H=((rut//1)%10) * 2

suma=(A+B+C+D+E+F+G+H)

resto1= suma // 11

resto2=suma-(11*resto1)

resta=11-resto2

if resta == 11:

  print("dv=",end="")

  print(0)

elif resta == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")

  print(resta)
   