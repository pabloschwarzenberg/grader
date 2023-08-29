#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut: ")
b = ''
d = 0
for i in range(len(rut)):
    a = rut[i] 
    b = a + b

for k in range(len(rut)):
    c = int(b[k]) * ((k%6)+2)
    d += c
   

division = d%11
resto = 11-division

if resto == 11:
    print("dv = 0")
elif resto == 10:
    print("dv = K")
else:
    print("dv = ", resto)

      