#Cálculo del dígito verificador de un rut
x=""
h= 0
rut= input("Ingrese su numero de rut: ")
for i in range(len(rut)):
    rut_inv= rut[i]
    x= rut_inv + x
print(x)
for a in range(len(rut)):
     m = int(x[a]) * ((a%6)+2)
     h += m
   

div = h%11
res = 11-div

if res == 11:
    print("dv = 0")
elif res == 10:
    print("dv = k")
else:
    print("dv = ", res)     