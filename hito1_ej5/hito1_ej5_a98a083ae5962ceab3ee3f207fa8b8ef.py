#Cálculo del dígito verificador de un rut
numero = int(input('Introduce el RUT: '))

def digitos(n):
    i = 1
    while n >= 10:
        n = n / 10
        i = i + 1
    return(i)

print(digitos(numero))

if (digitos(numero))>=8:
    numero=str(numero)
    a=(int(numero[0]) * 3)
    b=int(numero[1])*2
    c=int(numero[2])*7
    d=int(numero[3])*6
    e=int(numero[4])*5
    f=int(numero[5])*4
    g=int(numero[6])*3
    h=int(numero[7])*2
    suma=a+b+c+d+e+f+g+h
    print(suma)
    resto=suma%11
    dv=11-resto
    if dv==11:
        print("dv=", 0)
    elif dv==10:
        print("dv=", "k")
    else:
        print("dv=",dv)

else:
    numero = str(numero)
    a = (int(numero[0]) * 2)
    b = int(numero[1]) * 7
    c = int(numero[2]) * 6
    d = int(numero[3]) * 5
    e = int(numero[4]) * 4
    f = int(numero[5]) * 3
    g = int(numero[6]) * 2
    suma = a + b + c + d + e + f + g
    resto = suma % 11
    dv = 11 - resto
    if dv==11:
        print("dv=", 0)
    elif dv==10:
        print("dv=", "k")
    else:
        print("dv=",dv)