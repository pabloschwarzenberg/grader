#Cálculo del dígito verificador de un rut
ru_t=(input("Ingrese rut sin digito:"))
rut_=""
for num in ru_t:
    rut_=num+rut_
suma=0
r=0
for a in rut_:
    a=int(a)
    if r==0:
        suma=suma+2*a
    if r==1:
        suma=suma+3*a
    if r==2:
        suma=suma+4*a
    if r==3:
        suma=suma+5*a
    if r==4:
        suma=suma+6*a
    if r==5:
        suma=suma+7*a
    if r==6:
        suma=suma+2*a
    if r==7:
        suma=suma+3*a
    if r==8:
        suma=suma+4*a
    r=r+1
resultado=(suma//11)*11
resta=0
if resultado>suma:
    resta=resultado-suma
if suma>resultado:
    resta=suma-resultado
o=11-resta
if o==11:
    o=0
if o==10:
    o="k"
print("dv=",o)     


   

