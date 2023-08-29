#Cálculo del dígito verificador de un rut
rut = eval(input('Ingresa tu Rut:'))


if 1000000 <= rut <= 99999999:
    d8 = rut%10
    rut = rut//10
    
    d7 = rut%10
    rut = rut//10
    
    d6 = rut%10
    rut = rut//10
    
    d5 = rut%10
    rut = rut//10
    
    d4 = rut%10
    rut = rut//10
    
    d3 = rut%10
    rut = rut//10
    
    d2 = rut%10
    rut = rut//10
    
    d1 = rut%10
    rut = rut//10

    S = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 + d2*2 + d1*3
    R = S % 11
    V = 11-R

    if V == 11:
        print('dv=0')
    else:
        if V == 10:
            print('dv=k')
        else:
            print('dv=', V)
else:
    print('Rut ingresado no es válido.') 