rut=int(input("Ingrese rut sin el guion: "))

x1=rut%10 #Ultimo digito
x2=(rut%100)//10
x3=(rut%1000)//100
x4=(rut%10000)//1000
x5=(rut%100000)//10000
x6=(rut%1000000)//100000
x7=(rut%10000000)//1000000
x8=(rut%100000000)//10000000 #Primer digito

m=(x1*2)+(x2*3)+(x3*4)+(x4*5)+(x5*6)+(x6*7)+(x7*2)+(x8*3)
d=m//11
a=d*11
f=m-a
Dv=11-f
if(Dv==10):
  print("Dv= K")
elif(Dv==11):
  print("Dv= 0")
else:
  print("Dv=",Dv)