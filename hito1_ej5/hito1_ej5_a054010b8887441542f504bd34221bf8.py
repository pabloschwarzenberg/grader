#Cálculo del dígito verificador de un rut
rat=int(input("Ingrese el rut: "))

aa=(rat//10000000) * 3

bb=((rat//1000000)%10) * 2

cc=((rat//100000)%10) * 7

dd=((rat//10000)%10) * 6

ee=((rat//1000)%10) * 5

ff=((rat//100)%10) * 4

gg=((rat//10)%10) * 3

hh=((rat//1)%10) * 2

suma=(aa+bb+cc+dd+ee+ff+gg+hh)

rt1= suma // 11

rt2=suma-(11*rt1)

rt=11-rt2

if rt == 11:

  print("dv=",end= "")

  print(0)

elif rt == 10:

  print("dv=",end="")

  print("k")

else:

  print("dv=",end ="")

  print(rt)
