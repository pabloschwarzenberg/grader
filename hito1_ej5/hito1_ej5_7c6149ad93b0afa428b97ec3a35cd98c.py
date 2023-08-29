#Cálculo del dígito verificador de un rut
ru_t=(input("Ingrese rut sin digito:"))
rut=""
for num in ru_t:
    rut=num+rut
suma=0
b=0
for a in rut:
    a=int(a)
    if b==0:
        suma=suma+2*a
    if b==1:
        suma=suma+3*a
    if b==2:
        suma=suma+4*a
    if b==3:
        suma=suma+5*a
    if b==4:
        suma=suma+6*a
    if b==5:
        suma=suma+7*a
    if b==6:
        suma=suma+2*a
    if b==7:
        suma=suma+3*a
    if b==8:
        suma=suma+4*a
    b=b+1
resultado=(suma//11)*11
resta=0
if resultado>suma:
    resta=resultado-suma
if suma>resultado:
    resta=suma-resultado
m=11-resta
if m==11:
    m=0
if m==10:
    m="k"
print("dv=",m)     