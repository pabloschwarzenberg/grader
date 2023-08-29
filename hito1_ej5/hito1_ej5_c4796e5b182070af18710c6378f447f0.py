#Cálculo del dígito verificador de un rut
r=int(input("Ingrese un número de rut sin puntos ni con dígito verificador:"))
a=r//10000000
b=(r//1000000)%10
c=(r//100000)%10
d=(r//10000)%10
e=(r//1000)%10
f=(r//100)%10
g=(r//10)%10
h=r%10
A=a*8
B=b*9
C=c*4
D=d*5
E=e*6
F=f*7
G=g*8
H=h*9
S=A+B+C+D+E+F+G+H
v=S%11
if v==10: print("dv=k")
elif v==9: print("dv=9")
elif v==8: print("dv=8")
elif v==7: print("dv=7")
elif v==6: print("dv=6")
elif v==5: print("dv=5")
elif v==4: print("dv=4")
elif v==3: print("dv=3")
elif v==2: print("dv=2")
elif v==1: print("dv=1")
elif v==0: print("dv=0")

