r=int(input("ingrese número rut "))
prim=r%10
a=prim*2
seg=r%100
seg2=seg//10
s=seg2*3
ter=r%1000
ter2=ter//100
d=ter2*4
cua=r%10000
cua2=cua//1000
f=cua2*5
qui=r%100000
qui2=qui//10000
g=qui2*6
sex=r%1000000
sex2=sex//100000
k=sex2*7
sep=r%10000000
sep2=sep//1000000
h=sep2*2
octa=r//10000000
j=octa*3
suma=a+s+d+f+g+h+j+k
division=suma//11
resta=suma-(11*division)
resul=11-resta
if resul==11:
    print("dv=0")
elif resul==10:
    print("dv=k")
else:
    print("dv=",resul)
