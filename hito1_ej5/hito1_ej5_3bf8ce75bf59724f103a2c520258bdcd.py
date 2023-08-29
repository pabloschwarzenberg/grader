r=input("Introduza su rut aqui sin si digito verificador:")
a=int(r[0])*3
print(a)
b=int(r[1])*2
print(b)
c=int(r[2])*7
print(c)
d=int(r[3])*6
print(d)
e=int(r[4])*5
print(e)
f=int(r[5])*4
print(f)
g=int(r[6])*3
print(g)
h=int(r[7])*2
print(h)
if int(r)<10000000:
    r="0"+r
i=a+b+c+d+e+f+g+h
j=i%11
dv=11-j
if dv==10:
    dv="k"
if dv==11:
    dv="0"
print("Su digito verificador es:",dv)