#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut sin puntos ni guion: "))
r8=rut%10
r7=rut%100//10
r6=rut%1000//100
r5=rut%10000//1000
r4=rut%100000//10000
r3=rut%1000000//100000
r2=rut%10000000//1000000
r1=rut%100000000//10000000
f_digitos=(r8*2)+(r7*3)+(r6*4)+(r5*5)+(r4*6)+(r3*7)+(r2*2)+(r1*3)
rst_div=f_digitos//11
rst_div2=f_digitos-(11*rst_div)
dv=11-rst_div2
if(dv==11):
  print("dv=",0)
if(dv==10):
  print("dv=k")
else:
  print("dv=",dv)      