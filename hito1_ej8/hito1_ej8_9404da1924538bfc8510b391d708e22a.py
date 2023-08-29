#Descomponer un número
num = str(input("Ingresa un numero: "))
if len(num) == 4:
    M = num[0]
    C = num[1]
    D = num[2]
    U = num[3]
    print("{}M + {}C + {}D + {}U".format(M,C,D,U))
if len(num) == 3:
    C = num[0]
    D = num[1]
    U = num[2]
    print("{}C + {}D + {}U".format(C,D,U))
if len(num) == 2:
    D = num[0]
    U = num[1]
    print("{}D + {}U".format(D,U))
if len(num) == 1:
    U = num[0]
    print("{}U".format(U))


