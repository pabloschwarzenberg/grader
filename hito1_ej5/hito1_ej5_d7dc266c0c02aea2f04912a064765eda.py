#Cálculo del dígito verificador de un rut
nroRut = int(input("Ingrese un numero: "))
rut = str(nroRut)
x = ""
mul = 0
j = 0

for i in rut:
    x = i + x
    


factor = 2
while j < len(x):
    if factor == 8:
        factor = 2
    mul = mul + (factor * int(x[j]))   
    factor += 1
    j += 1
    

residuo = mul%11

resto = 11 - residuo

if resto == 11:
    dv = "0"
elif resto == 10:
    dv = "K"
else:
    dv = str(resto)

print("dv= ", dv)      