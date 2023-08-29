#Cálculo del dígito verificador de un rut
rut = int(input('Ingrese su rut SIN DIGITO VERIFICADOR: '))

d1 = rut%10   ## Con %10 Conseguimos el ultimo digito (modulo)
rut = rut//10 ## Con //10 Le sacamos al rut el utlimo Digito. ( SE SOBRE ESCRIBE RUT )

d2 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d7 = rut%10
rut = rut//10

d8 = rut%10
rut = rut//10

a = d1*2
b = d2*3
c = d3*4
d = d4*5
e = d5*6
f = d6*7
g = d7*2
h = d8*3
SUMA = (a+b+c+d+e+f+g+h)
RESTO = (SUMA%11)
Resultado = (11-RESTO)

if Resultado == 11:
    print('dv=0')
    
if Resultado == 10:
    print('dv=K')
    
if Resultado != 11 and Resultado != 10:
    
    dvSinEspacio = 'dv=' + str(Resultado)
    print(dvSinEspacio)