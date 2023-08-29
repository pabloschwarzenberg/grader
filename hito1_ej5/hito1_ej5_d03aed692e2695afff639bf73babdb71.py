#Cálculo del dígito verificador de un rut
rut = int(input("ingrese rut sin digito verificador:"))
largo = len(str(rut))
dv=""
a = (rut//10**7)*3
b = ((rut -((rut//10**7)*10**7))//10**6)*2
c = ((rut -((rut//10**6)*10**6))//10**5)*7
d = ((rut -((rut//10**5)*10**5))//10**4)*6
e = ((rut -((rut//10**4)*10**4))//10**3)*5
f = ((rut -((rut//10**3)*10**3))//10**2)*4
g = ((rut -((rut//10**2)*10**2))//10**1)*3
h = ((rut -((rut//10**1)*10**1))//10**0)*2
suma = (a+b+c+d+e+f+g+h)
resto = suma%11
resta = 11-resto
if resta == 11:
    dv = 0
    div = str(dv)
elif resta == 10:
    dv = "k"
    div = str(dv)
else:
    dv = resta
    div = str(dv)
print("dv="+div)