#Cálculo del dígito verificador de un rut
rut = float(input("ingrese su rut, sin digito verificador:"))

a1 = float(rut[7:8])
a2 = float(rut[6:7])
a3 = float(rut[5:6]) 
a4 = float(rut[4:5])
a5 = float(rut[3:4])
a6 = float(rut[2:3])
a7 = float(rut[1:2]) 
a8 = float(rut[0:1])

dv1 = float(a1*2 + a2*3 + a3*4 + a4*5 + a5*6 + a6*7 + a7*2 + a8*3)

dv2 = dv1 // 11

dv3 = dv1 - (11 * dv2)

dv4 = 11 - dv3

if dv4 == 11:
    print ("dv=0")
    
elif dv4 == 10:
    print ("dv=K")
    
else:
    print("dv=", dv4)
