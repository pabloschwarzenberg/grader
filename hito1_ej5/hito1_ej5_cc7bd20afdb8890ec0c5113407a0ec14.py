rut=(input("Digite su rut sin puntos ni digito verificador:"))
if (int(rut[0:])<10000000):
    x=1
else:
    x=0
a=(int(rut[(7-x)])*2)
b=(int(rut[(6-x)])*3)
c=(int(rut[(5-x)])*4)
d=(int(rut[(4-x)])*5)
e=(int(rut[(3-x)])*6)
f=(int(rut[(2-x)])*7)
g=(int(rut[(1-x)])*2)
h=(int(rut[(0-x)])*3)
if (x==1):
    h=0
suma=(a+b+c+d+e+f+g+h)
resto=(suma%11)
dv=(11-resto)
if (dv==10):
    dv=str("k")
if (dv==11):
    dv=0
print("suma",suma)
print("resto",resto)
print("dv=",dv)






