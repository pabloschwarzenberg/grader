v=int(input("Ingrese numero de hasta 4 digitos: "))
u=v%10
v=v//10
d=v%10
v=v//10
c=v%10
v=v//10
m=v%10
if m%10!=0:
    print(m,"M + " ,end="")
if c%10!=0 or m%10!=0:
    print(c,"C + " ,end="")
if d%10!=0 or c%10!=0:
    print(d,"D + " ,end="")
print(u,"U")
