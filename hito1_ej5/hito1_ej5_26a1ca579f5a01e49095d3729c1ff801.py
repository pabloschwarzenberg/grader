#Cálculo del dígito verificador de un rut
rut=input('ingrese numero de rut: ')
b=rut[6]*2
c=rut[5]*3
d=rut[4]*4
e=rut[3]*5
f=rut[2]*6
g=rut[1]*7
h=rut[0]*2
suma=b+c+d+e+f+g+h
mod=(suma)/11
resto=suma-(11*mod)
digito=11-resto
veri=x
if digito ==11:
    veri=0
elif digito==10:
    veri=K
else:
    veri=digito
print(veri)

