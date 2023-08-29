RUT=int(input()) 
a=int(RUT/10000000)%10
b=int(RUT/1000000)%10
c=int(RUT/100000)%10
d=int(RUT/10000)%10
e=int(RUT/1000)%10
f=int(RUT/100)%10
g=int(RUT/10)%10
h=RUT%10
dv1=((h*9+g*8+f*7+e*6+d*5+c*4+b*9)%11)
dv2=((h*9+g*8+f*7+e*6+d*5+c*4+b*9+a*8)%11)

if RUT<9999999:
    print(str("dv="),((h*9+g*8+f*7+e*6+d*5+c*4+b*9)%11))
    if dv1==10:
        print("dv=k")
       
else:
    print(str("dv="),((h*9+g*8+f*7+e*6+d*5+c*4+b*9+a*8)%11))
    
    if dv2==10:
        print("dv=k")
 
