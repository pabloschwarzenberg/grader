#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut: ")
b = ''
d = 0
for i in range(len(rut)):
    a = rut[i] 
    b = a + b

for j in range(len(rut)):
    c = int(b[j]) * ((j%6)+2)
    d += c
   

div = d%11
resto = 11-div

if resto == 11:
    print("dv = 0")
elif resto == 10:
    print("dv = K")
else:
    print("dv = ", resto)