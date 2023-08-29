a=int(input("ingrese un numero:"))
b=int(input("ingrese otro numero:"))
divisor1=int(1)
divisor2=int(1)
c=[]
d=[]
while divisor1<=a:
    if a%divisor1==0:
        c.insert(0,divisor1)
    divisor1=divisor1+1
while divisor2<=b:
    if b%divisor2==0:
        d.insert(0,divisor2)
    divisor2=divisor2+1

if len(c)==len(d):
    print("True")
else:
    print("False")
           