#Cálculo del dígito verificador de un rut
numero=int(input())
a=numero%10
b=((numero%100)-(numero%10))//10
c=((numero%1000)-(numero%100))//100
d=((numero%10000)-(numero%1000))//1000
e=((numero%100000)-(numero%10000))//10000
f=((numero%1000000)-(numero%100000))//100000
g=((numero%10000000)-(numero%1000000))//1000000
h=((numero%100000000)-(numero%10000000))//10000000
sumanumero=a*2+b*3+c*4+d*5+e*6+f*7+2*g+3*h
div=sumanumero%11
resto=11-div
if resto==11:
  print("dv=0")
elif resto==10:
  print("dv=k")
else:
  print("dv=",resto)