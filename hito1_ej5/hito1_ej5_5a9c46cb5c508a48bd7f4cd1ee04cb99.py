###ALGORITMO 1

#1. Multiplicar cada dígito del RUT por 2, 3, ..., 7, 2, 3, ... de atrás hacia adelante.
#2. Sumar las multiplicaciones parciales.
#3. Calcular el resto de la división por 11
#4. El Dígito Verificador es 11 menos el resultado anterior. Si es 10, se cambia por 'k'.

rut=input()

#condicionales

if len(rut)==7:
    a1=int(rut[0])
    a2=int(rut[1])
    a3=int(rut[2])
    a4=int(rut[3])
    a5=int(rut[4])
    a6=int(rut[5])
    a7=int(rut[6])

    ###MULTIPLICACION

    p7=a7*2
    p6=a6*3
    p5=a5*4
    p4=a4*5
    p3=a3*6
    p2=a2*7
    p1=a1*2

    ###SUMA

    suma=p1+p2+p3+p4+p5+p6+p7

    ###MODULO DE /11

    mod=suma%11

    ###DIGITO VERIFICADOR
    
    if mod!=0:
        dv=11-mod
    else:
        dv=0
        
    if dv==10:
        dv='k'
    
if len(rut)==8:
    a1=int(rut[0])
    a2=int(rut[1])
    a3=int(rut[2])
    a4=int(rut[3])
    a5=int(rut[4])
    a6=int(rut[5])
    a7=int(rut[6])
    a8=int(rut[7])
    
    ###MULTIPLICACION

    p8=a8*2
    p7=a7*3
    p6=a6*4
    p5=a5*5
    p4=a4*6
    p3=a3*7
    p2=a2*2
    p1=a1*3
    
    ###SUMA

    suma=p1+p2+p3+p4+p5+p6+p7+p8

    ###MODULO DE /11

    mod=suma%11

    ###DIGITO VERIFICADOR
    
    if mod!=0:
        dv=11-mod
    else:
        dv=0
        
    if dv==10:
        dv='k'

print('dv=',dv,sep='')
    
