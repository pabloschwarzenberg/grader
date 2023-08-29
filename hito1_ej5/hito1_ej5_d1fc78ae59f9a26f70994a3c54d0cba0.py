#Cálculo del dígito verificador de un rut
rut= int(input())
numero_dig=len(str(rut))
#8 digitos
a=rut//10000000
b=(rut//1000000)%10
c=(rut//100000)%10
d=(rut//10000)%10    
e=(rut//1000)%10
f=(rut//100)%10
g=(rut//10)%10
h=rut%10
#7 digitos
s=rut//1000000
o=(rut//100000)%10
p=(rut//10000)%10
q=(rut//1000)%10
r=(rut//100)%10
y=(rut//10)%10
t=rut%10
if(numero_dig==7): 
  mult_sum1= (s*2)+(o*7)+(p*6)+(q*5)+(r*4)+(y*3)+(t*2)
  resto1= mult_sum1%11
  dv1= (11-resto1)
  if not(dv1==10):
    print("dv=",dv1)
  else:
    print("dv=k")
else:
  mult_sum= (a*3)+(b*2)+(c*7)+(d*6)+(e*5)+(f*4)+(g*3)+(h*2)
  resto= mult_sum%11
  dv= (11-resto)
  if not(dv==10):
    print("dv=",dv)
  else: 
    print("dv=k")