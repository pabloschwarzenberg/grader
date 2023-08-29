#Cálculo del dígito verificador de un rut
A =eval(input("Ingrese Rut sin digito verificador: "))
while not((A<=99999999 and A>=10000000) or (A<=9999999 and A>=1000000)):
    A =eval(input("Error.....ingrese un Rut Valido: "))
M =len(str(A))
if M==8:
    B =int(str(A)[-1])
    C =int(str(A)[-2])
    D =int(str(A)[-3])
    E =int(str(A)[-4])
    F =int(str(A)[-5])
    G =int(str(A)[-6])
    H =int(str(A)[-7])
    I =int(str(A)[-8])
    b = (B * 2)
    c = (C * 3)
    d = (D * 4)
    e = (E * 5)
    f = (F * 6)
    g = (G * 7)
    h = (H * 2)
    i = (I * 3)
    N = (b + c + d + e + f + g + h + i)
    n = N % 11
    K = 11 - n
    if K == 11:
        print("dv=0")
    elif K == 10:
        print("dv=K")
    else:
        print("dv=",K)

elif M==7:
    B =int(str(A)[-1])
    C =int(str(A)[-2])
    D =int(str(A)[-3])
    E =int(str(A)[-4])
    F =int(str(A)[-5])
    G =int(str(A)[-6])
    H =int(str(A)[-7])
    b = (B * 2)
    c = (C * 3)
    d = (D * 4)
    e = (E * 5)
    f = (F * 6)
    g = (G * 7)
    h = (H * 2)
    N = (b + c + d + e + f + g + h )
    n = N % 11
    K = 11 - n
    if K == 11:
        print("dv=0")
    elif K == 10:
        print("dv=K")
    else:
        print("dv=",K)