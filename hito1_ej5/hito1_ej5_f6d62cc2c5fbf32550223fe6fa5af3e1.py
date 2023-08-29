#calculo digito verificador de un rut
rut=int(input('ingrese su RUT :'))
print("descomposicion del rut", rut//10000000)
print("descomposicion del rut", rut//1000000)
print("descomposicion del rut", rut//100000)
print("descomposicion del rut", rut//10000)
print("descomposicion del rut", rut//1000)
print("descomposicion del rut", rut//100)
print("descomposicion del rut", rut//10)
print("descomposicion del rut", rut//1)
a=(rut//10000000)*3
print("el resultado es:",a)
b=((rut//1000000)%10)*2
print("el resultado es:",b)
c=((rut//100000)%10)*7
print("el resultado es:",c)
d=((rut//10000)%10)*6
print("el resultado es:",d)
e=((rut//1000)%10)*5
print("el resultado es:",e)
f=((rut//100)%10)*4
print("el resultado es:",f)
g=((rut//10)%10)*3
print("el resultado es:",g)
h=((rut//1)%10)*2
print("el resultado es:",h)
suma=(a+b+c+d+e+f+g+h)
print("el resultado es:",suma)
resto1=suma//11
print("el resultado del resto1=suma//11 es:",resto1)
resto2=suma-(11*resto1)
print("el resultado de resto2=suma-(11*resto1) es:",resto2)
resta=11-resto2
print("el resultado de la resta=11-resto2 es:",resta)
if resta==11:
   print("dv=",end="")
   print(0)
elif resta==10:
   print("dv=",end="")
   print("k")
else:
   print("dv=",end="")
   print(resta)
  

