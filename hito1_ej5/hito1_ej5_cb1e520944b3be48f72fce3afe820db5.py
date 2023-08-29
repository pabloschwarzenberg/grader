print()
print()
print('%%%%%%%% CONOCER DIGITO VERIFICADOR %%%%%%%%%')
print()
print()
rut=int(input('Ingrese su RUT, sin DV:  '))
m=2 #multiplicador
suma= 0 #para ir 
while rut>0:
    ultimo=rut%10 #para ultimo digito
    suma += ultimo*m
    m+=1
    if m==8:
        m=2
    rut=rut//10
dv= 11-suma%11
if dv==10:
    print()
    print("dv=k")
    print()
elif dv==11:
    print()
    print("dv=0")
    print()
else:
    print()
    print("dv="+str(dv))
    print()
