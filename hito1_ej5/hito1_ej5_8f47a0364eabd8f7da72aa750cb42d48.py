#Cálculo del dígito verificador de un rut
n=int(input("Ingresar rut sin el numero despues del guion: "))
a=int((n%10**8)//10**7)
b=int((n%10**7)//10**6)
c=int((n%10**6)//10**5)
d=int((n%10**5)//10**4)
e=int((n%10**4)//10**3)
f=int((n%10**3)//10**2)
g=int((n%10**2)//10)
h=int(n%10)

i=h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3
k=i%11 
l=11-k

if l==11:
 print("dv=0")

if l==10:
 print("dv=k")
 
if l!=11 and l!=10:
 print("dv=",l)