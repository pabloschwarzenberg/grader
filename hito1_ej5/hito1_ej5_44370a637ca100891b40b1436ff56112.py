#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut: "))
a = rut[0]*2
b = rut[1]*3
c = rut[2]*4
d = rut[3]*5
e = rut[4]*6
f = rut[5]*7
g = rut[6]*2
dig_ver = a+b+c+d+e+f+g
print("dv=", dig_ver)