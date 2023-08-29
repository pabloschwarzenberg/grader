##2_calculo de digito verificador del rut:
#Escribir un programa que reciba como dato un número que representara un Rut
#al que debe calcular el dígito verificador. Por ejemplo, al ingresar 6016740
#tu programa debiera imprimir el siguiente mensaje:
#dv=0
ingreso=input("ingresar numero")

try:
    valor=int(ingreso)
except ValueError:
    print("La cadena ingresada no es un numero")
    exit()
    
x=len(ingreso)
factor=2
total=0

while x >0:
    x = x-1
    numero=int(ingreso[x:x+1])
    total=total + (numero * factor)
    if factor==7:
        factor=2
    else:
        factor=factor+1

modulo=total%11

validador =11-modulo

if validador==11:validador=0
if validador==10:validador=1
print f"dv={x}"   

