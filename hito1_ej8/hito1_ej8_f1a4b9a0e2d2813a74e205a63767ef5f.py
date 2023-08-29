#Descomponer un número
num = input("Escriba un número de 4 dígitos: ")

if len(num) == 4:
    m = num[0]
    c = num[1]
    d = num[2]
    u = num[3]
    print("{}M + {}C + {}D + {}U".format(m, c, d, u))
elif len(num) == 3:
    c = num[0]
    d = num[1]
    u = num[2]
    print("{}C + {}D + {}U".format(c, d, u))
else:
    print("ERROR")