tn=[]
suma=0
while True:
    un=int(input("ingresa numero"))
    if un==-1:
        break
    tn.append(un)
    suma=suma+un
print (tn)
i=0
cantidad=len(tn)
minimo=1000
while i<len(tn):
    if tn[i]<minimo:
        minimo=tn[i]
    i=i+1
print("cantidad=",cantidad)
if cantidad!=0:
    
    print("minimo=",minimo)
    promedio=round(suma/cantidad,1)
    print("promedio=",promedio)
else:
    print("minimo=nd")
    print("promedio=nd")



