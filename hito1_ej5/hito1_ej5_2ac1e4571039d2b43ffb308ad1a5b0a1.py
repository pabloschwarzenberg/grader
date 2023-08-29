rut_user=int(input("Ingrese el rut sin digito verificador: "))
a=(rut_user//10000000) * 3
b=((rut_user//1000000)%10) * 2
c=((rut_user//100000)%10) * 7
d=((rut_user//10000)%10) * 6
e=((rut_user//1000)%10) * 5
f=((rut_user//100)%10) * 4
g=((rut_user//10)%10) * 3
h=((rut_user//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)
rest1= suma // 11
rest2=suma-(11*rest1)
resta=11-rest2
if resta == 11:
  print("dv=",end="")
  print(0)
elif resta == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(resta)