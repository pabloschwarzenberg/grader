#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
d1=(rut//10000000) * 3
d2=((rut//1000000)%10) * 2
d3=((rut//100000)%10) * 7
d4=((rut//10000)%10) * 6
d5=((rut//1000)%10) * 5
d6=((rut//100)%10) * 4
d7=((rut//10)%10) * 3
d8=((rut//1)%10) * 2
suma=(d1+d2+d3+d4+d5+d6+d7+d8)
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