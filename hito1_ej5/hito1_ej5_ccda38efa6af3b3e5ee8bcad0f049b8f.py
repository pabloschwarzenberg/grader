#dig verificador de rut
r=str(input("ingrese su rut sin digito verificador: "))
if(len(r)==8):
    d1 = eval(r[7]) * 2
    d2 = eval(r[6]) * 3
    d3 = eval(r[5]) * 4
    d4 = eval(r[4]) * 5
    d5 = eval(r[3]) * 6
    d6 = eval(r[2]) * 7
    d7 = eval(r[1]) * 2
    d8 = eval(r[0]) * 3
    s = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
if(len(r)==7):
    d1 = eval(r[6]) * 2
    d2 = eval(r[5]) * 3
    d3 = eval(r[4]) * 4
    d4 = eval(r[3]) * 5
    d5 = eval(r[2]) * 6
    d6 = eval(r[1]) * 7
    d7 = eval(r[0]) * 2
    s = d1 + d2 + d3 + d4 + d5 + d6 + d7
d=s//11
df=d*11
ds=s-df
dv=11-ds
if(dv==10):
    dv="K"
if(dv==11):
    dv=0
print("dv=",dv)

