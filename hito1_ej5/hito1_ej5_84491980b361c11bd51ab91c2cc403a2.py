n=int(input("Ingrese su rut sin , ni -:"))
x=n%10#ultimo digito
y=((n-x)%100)/10 #penultimo digito
z=((n%1000)/100)-((n%100)/100)#antepenultimo digito
c=((n%10000)/1000)-((n%1000)/1000)#5°numero
v=((n%100000)/10000)-((n%10000)/10000)#4°numero
b=((n%1000000)/100000)-((n%100000)/100000)#3°numero
a=((n%10000000)/1000000)-((n%1000000)/1000000)#2° numero
m=int(n/10000000)#1°numero
print("sus numeros son",x,y,z,c,v,b,a,m)
total=(x*2+y*3+z*4+c*5+v*6+b*7+a*2+m*3)
print("total:",total)
r=int(total/11)
final=total-r*11
print("final es",final)
digito=11-final
if(digito==11):
  print("dv=0")
if(digito==10):
  print("dv=K")
if(digito<10):
 print("dv=",digito)