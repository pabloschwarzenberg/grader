rut=str(input())[::-1]
a=0
b=[2,3,4,5,6,7]
c=0
while c<len(rut):
    a=a+int(rut[c])*b[c%6]
    c=c+1
d=11-(a%11)
if d==11:
    print("dv=",0)
elif d==10:
    print("dv=K")
else:
    print("dv=",d)