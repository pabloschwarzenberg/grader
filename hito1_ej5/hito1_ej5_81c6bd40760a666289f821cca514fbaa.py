rut=int(input("introduzca su rut sin digito verificador porfavor: "))
n1=(rut//10000000) * 3
n2=((rut//1000000)%10) * 2
n3=((rut//100000)%10) * 7
n4=((rut//10000)%10) * 6
n5=((rut//1000)%10) * 5
n6=((rut//100)%10) * 4
n7=((rut//10)%10) * 3
n8=((rut//1)%10) * 2
plus=(n1+n2+n3+n4+n5+n6+n7+n8)
less_1= plus // 11
less_2= plus -(11*less_1)
less=11-less_2
if less == 11:
  print("dv=",end="")
  print(0)
elif less == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print("dv=", less)