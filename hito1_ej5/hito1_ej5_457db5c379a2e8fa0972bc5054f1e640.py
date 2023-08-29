a=str(input("Ingresa el numero de rut (sin puntos ni guion): "))
c=2
suma=0
for i in range(len(a)-1, -1,-1):
    if c<=7:
        nuevo=int(a[i])*c
        c+=1
        suma+=nuevo
    if c>7:
        c=2
resto=suma%11
dv=11-resto
if dv==10:
    dv='k'
elif dv==11:
    dv=0
print('dv =',dv)
        
