#Cálculo del dígito verificador de un rut#Cálculo del dígito verificador de un rut
print("Programa para verificar rut")
numero = int(input("Número: "))
if numero < 10000000:
    unidades = numero%10
    numero = numero//10
    decenas = numero%10
    numero = numero//10
    centenas = numero%10
    numero = numero//10
    unidadesMil = numero%10
    numero = numero//10
    decenasMil = numero%10
    numero = numero//10
    centenaMil = numero%10
    numero = numero//10
    millon = numero%10
    u = unidades * 2
    d = decenas * 3
    c = centenas * 4
    um = unidadesMil * 5
    dm = decenasMil * 6
    cm = centenaMil * 7
    mill = millon * 2
    Total1 = u + d + c + um + dm + cm + mill
    Total2 = Total1 / 11
    T_r = int(Total2)
    Total3 = Total1 - (11 * T_r)
    Total4 = 11 - Total3
    if Total4 == 11:
        print("dv=0")
    elif Total4 == 10:
        print("dv=K")
    else:
        print("dv =" , Total4)
elif numero > 10000000:
    unidades = numero%10
    numero = numero//10
    decenas = numero%10
    numero = numero//10
    centenas = numero%10
    numero = numero//10
    unidadesMil = numero%10
    numero = numero//10
    decenasMil = numero%10
    numero = numero//10
    centenaMil = numero%10
    numero = numero//10
    millon = numero%10
    numero = numero//10
    decmillon = numero%10
    u = unidades * 2
    d = decenas * 3
    c = centenas * 4
    um = unidadesMil * 5
    dm = decenasMil * 6
    cm = centenaMil * 7
    mill = millon * 2
    dmill = decmillon * 3
    Total1 = u + d + c + um + dm + cm + mill + dmill
    Total2 = Total1 / 11
    T_r = round(Total2 , 0)
    Total3 = Total1 - (11 * T_r)
    Total4 = 11 - Total3
    if Total4 == 11:
        print("dv=0")
    elif Total4 == 10:
        print("dv=K")
    else:
        print("dv =" , Total4)