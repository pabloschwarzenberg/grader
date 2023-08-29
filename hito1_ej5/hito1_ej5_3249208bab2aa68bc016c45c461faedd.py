#Cálculo del dígito verificador de un rut

rut1 = int(input("Ingrese el primer digito de su rut, sin el dv: "))
rut2 = int(input("Ingrese el segundo digito de su rut, sin el dv: "))
rut3 = int(input("Ingrese el tercer digito de su rut, sin el dv: "))
rut4 = int(input("Ingrese el cuarto digito de su rut, sin el dv: "))
rut5 = int(input("Ingrese el quinto digito de su rut, sin el dv: "))
rut6 = int(input("Ingrese el sexto digito de su rut, sin el dv: "))
rut7 = int(input("Ingrese el septimo digito de su rut, sin el dv: "))

##procesos 

p1 = rut7 * 2
p2 = rut6 * 3
p3 = rut5 * 4
p4 = rut4 * 5
p5 = rut3 * 6
p6 = rut2 * 7
p7 = rut1 * 2

sp = p1 + p2 + p3 + p4 + p5 + p6 + p7

spp = sp / 11

rd = sp -(11*spp)

rf = 11 - rd

if rf == 11:
    dv = 0
    print ("Su digito verificador es", dv)
elif rf == 10:
    dv = "k"
    print("Su diito verificador es", dv)
else:
    dv == rf
    print ("Su digito verificador es", dv)
