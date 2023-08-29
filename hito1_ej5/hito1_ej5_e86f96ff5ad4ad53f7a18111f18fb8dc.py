rut = str(input("ingrese RUT"))
largo = len(rut)
rut = int(rut)
iterador = 0
factor = 2
suma = 0
while iterador <= largo:
    modulo = rut%10
    suma = suma + (modulo*factor)
    rut= rut//10
    iterador= iterador+1
    factor= factor+1
    if factor==8:
        factor=2

resto = suma//11
dv= suma-(11*resto)
dv = 11-dv
if dv ==11:
    print("dv=0")
if dv ==10:
    print("dv=K")
else:
    print("dv=",dv)
