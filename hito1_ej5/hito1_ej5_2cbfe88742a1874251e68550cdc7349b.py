#Cálculo del dígito verificador de un rut

rut = input("Ingrese Rut sin puntos ni digido verificador: ")
revertido = rut[:: - 1 ] 

suma=0
n=2
for x in revertido:
    
    suma=suma + int(x)*n
    if n == 7:
        n=2
    else:
        n = n+1
resultado = 11-suma%11      

if resultado == 10:
    resultado = "K"
if resultado ==11:
    resultado = 0
    
print("dv = " + str(resultado))