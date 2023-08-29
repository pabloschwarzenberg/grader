
Rut = int(input(" ingrese su rut: "))
A= (Rut//10000000) * 3

B= ((Rut//1000000)%10) * 2

C= ((Rut//100000)%10) * 7

D= ((Rut//10000)%10) * 6

E= ((Rut//1000)%10) * 5

F= ((Rut//100)%10) * 4

G= ((Rut//10)%10) * 3

H= ((Rut//1)%10) * 2

suma=(A+B+C+D+E+F+G+H)

resto= suma // 11

resto1= suma-(11*resto)

resta=11-resto1

if resta == 11:

  print("dv=",end="")

  print(0)

elif resta == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end="")

  print("dv=",resta)