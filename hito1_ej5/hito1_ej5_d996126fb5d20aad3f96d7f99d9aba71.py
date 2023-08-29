#Cálculo del dígito verificador de un rut

Rut=int(input('Ingrese su rut sin puntos ni guión: '))

while Rut<0:
    Rut=int(input('\nEl Rut ingresado es incorrecto. Ingrese su Rut nuevamente: ')) 

RutATexto=str(Rut)
LargoRut=len(RutATexto)

while LargoRut!=8 and LargoRut!=7:
    Rut=int(input('\nEl Rut ingresado es incorrecto. Ingrese su Rut nuevamente: '))
    RutATexto=str(Rut)
    LargoRut=len(RutATexto)
    
posicion=1
multiplicar=2
suma=0

while posicion<=LargoRut:
    Producto=(int(RutATexto[-posicion]))*multiplicar
    suma=suma+Producto
    posicion=posicion+1
    multiplicar=multiplicar+1
    
    if multiplicar==8:
        multiplicar=2

Modulo11=suma%11

dv=11-Modulo11

if dv==11:
    dv=0

if dv==10:
    dv='K'

print('dv=',dv)

