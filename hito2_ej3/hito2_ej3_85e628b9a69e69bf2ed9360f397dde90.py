c=input("Ingrese secuencia: ")
c=c.upper()
n=int(input("Ingrese número entero: "))
l=len(c)
v=[]
nv=[]
r=l-n+1
for i in range(r):
    t=c[i:i+n]
    if t in nv:
        continue
    if t in v:
        v.remove(t)
        nv.append(t)
    else:
        v.append(t)
l=len(v)
if l==0:
    print("ninguna")
else:
    for i in range(l):
        print(v[i])