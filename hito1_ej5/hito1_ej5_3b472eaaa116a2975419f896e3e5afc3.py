#Cálculo del dígito verificador de un rut
r=input("RUT:")
suma=0
l=len(r)
suma=eval(r[-1])*2+ eval(r[-2])*3 + eval(r[-3])*4 +eval(r[-4])*5 +eval(r[-5])*6 + eval(r[-6])*7 + eval(r[-7])*2
if l==8:
    suma= suma+ eval(r[-8])*3
entera=(suma//11)
resto=(suma-(11*entera))
dv=(11-resto)
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
else:
    print("dv=",dv)
    