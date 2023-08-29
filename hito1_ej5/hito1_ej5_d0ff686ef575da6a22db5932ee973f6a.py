#Cálculo del dígito verificador de un rut
rut = (input("Ingrese Rut sin puntos ni guion ni digito:"))

largo = len(rut)
i = 2
f = largo + 1;
producto = 0
suma = 0;

while largo > 0:
    n = rut[f-2:f-1]
    f = f - 1
    largo = largo - 1
    if(i < 8):
        producto = int(n)*i
        suma = suma + producto
        i = i + 1
    else:
        i = 2
        producto = int(n)*i
        suma = suma + producto
        i = i + 1
        
resto = suma % 11
digito = 11 - resto

if(digito == 11):
    digito = 0
elif(digito == 10):
    digito = "k"

print("dv=",digito) 