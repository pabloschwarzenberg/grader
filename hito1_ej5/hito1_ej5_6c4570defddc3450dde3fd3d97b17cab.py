#Cálculo del dígito verificador de un rut
rut=int(input("introduzca su rut sin digito verificador porfavor: "))
n1=(rut//10000000) * 3
n2=((rut//1000000)%10) * 2
n3=((rut//100000)%10) * 7
n4=((rut//10000)%10) * 6
n5=((rut//1000)%10) * 5
n6=((rut//100)%10) * 4
n7=((rut//10)%10) * 3
n8=((rut//1)%10) * 2
Plus=(n1+n2+n3+n4+n5+n6+n7+n8)
Less_1= Plus // 11
Less_2= Plus -(11*Less_1)
Less=11-Less_2
if Less == 11:
  print("dv=",end="")
  print(0)
elif Less == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print("dv=", Less)