#Cálculo del dígito verificador de un rut
n=int(input(""))
D_=  n//10000000
U_= (n//1000000)%10
C__=((n//100000)%10)%10
D__=(((n//10000)%10)%10)%10
U__=((((n//1000)%10)%10)%10)%10
C___=(((((n//100)%10)%10)%10)%10)%10
D___=((((((n//10)%10)%10)%10)%10)%10)%10
U___=(((((((n%10)%10)%10)%10)%10)%10)%10)%10
_1=U___ *2
_2=D___ *3
_3=C___*4
_4=U__*5
_5=D__*6
_6=C__*7
_7=U_*2
_8=D_*3
S= _1 + _2 + _3 + _4 + _5 + _6 + _7 + _8
D= S%11
if D == 0:
    dv=0
elif D == 1:
    dv="k"
else:
    dv=11-D
print("dv=",dv)
