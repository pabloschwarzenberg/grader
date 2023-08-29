#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut sin el digito despues del guion: "))
d1=rut%10
d2=(rut%100)//10
d3=(rut%1000)//100
d4=(rut%10000)//1000
d5=(rut%100000)//10000
d6=(rut%1000000)//100000
d7=(rut%10000000)//1000000
d8=(rut//10000000)
f1=(d1*2)+(d2*3)+(d3*4)+(d4*5)+(d5*6)+(d6*7)+(d7*2)+(d8*3)
f2=f1//11
f3=f2*11
f4=f1-f3
Dv=11-f4
if(Dv==10):
  print("dv= K ")
elif(f4==0):
  print("dv= 0 ")
else:
  print("dv= ",Dv)     