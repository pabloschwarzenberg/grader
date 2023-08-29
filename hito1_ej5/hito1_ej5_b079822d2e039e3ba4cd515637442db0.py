#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
num1 =(rut//10000000) * 3
num2 =((rut//1000000)%10) * 2
num3 =((rut//100000)%10) * 7
num4 =((rut//10000)%10) * 6
num5 =((rut//1000)%10) * 5
num6 =((rut//100)%10) * 4
num7 =((rut//10)%10) * 3
num8 =((rut//1)%10) * 2
suma=(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)
resta= suma // 11
resta2=suma-(11*resta)
resta=11-resta2
if (resta == 11):
  print("dv=",end="")
  print(0)
elif (resta == 10):
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(resta)        