num = input("Ingresa un número de hasta 4 dígitos: ")

if len(num) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    num = num.zfill(4)
    U = int(num[3])
    D = int(num[2])
    C = int(num[1])
    M = int(num[0])
    Rollicion = ""
    if M > 0:
        Rollicion += str(M) + "M+"
    if C > 0 or M > 0:
        Rollicion += str(C) + "C+"
    if D > 0 or C > 0 or M > 0:
        Rollicion += str(D) + "D+"
    Rollicion += str(U) + "U"

    print("el numero descompuesto es:", Rollicion)