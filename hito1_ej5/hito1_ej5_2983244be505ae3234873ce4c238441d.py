#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut(sin digito verificador): "))
n8=rut%10
rut=rut//10
n7=rut%10
rut=rut//10
n6=rut%10
rut=rut//10
n5=rut%10
rut=rut//10
n4=rut%10
rut=rut//10
n3=rut%10
rut=rut//10
n2=rut%10
rut=rut//10
n1=rut%10
rut=rut//10
s=n8*2 + n7*3 + n6*4 + n5*5 + n4*6 + n3*7 + n2*2 + n1*3
r=s%11
total=r-11
if total==-11:
  print("dv=0")
if total==-10:
  print("dv=k")
else:
  if total!=-10 and total!=-11:
    print("dv=", -total)