#Cálculo del dígito verificador de un rut
r=int(input("Coloque su Rut"))
primero=(r//10000000) * 3

segundo=((r//1000000)%10) * 2

tercero=((r//100000)%10) * 7

cuarto=((r//10000)%10) * 6

quinto=((r//1000)%10) * 5

sexto=((r//100)%10) * 4

septimo=((r//10)%10) * 3

octavo=((r//1)%10) * 2

s=(primero+segundo+tercero+cuarto+quinto+sexto+septimo+octavo)
r1= s // 11
r2=s-(11*r1)
r=11-r2
if r == 11:
  print("dv=",end="")
  print(0)
elif r == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print("dv=",r)
