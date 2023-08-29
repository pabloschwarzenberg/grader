#Cálculo del dígito verificador de un rut
rut=input("escriba rut ")
lista=[]
w=1
a=len(rut)
n=0
h=-1
while(a!=0):
    w=w+1
    if(w==8):
        w=2
    a=a-1
    lista.append(int(rut[a])*w)
    h=h+1
    n=lista[h]+n
d=11-n%11
if(d==11):
    print("dv=",0)
if(d==10):
    print("dv=K")
else:
    print("dv=",d)      