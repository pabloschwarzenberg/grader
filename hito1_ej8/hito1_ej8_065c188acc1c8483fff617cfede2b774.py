numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) == 1:
    print("0M + 0C + 0D + {}U".format(numero))
elif len(numero) == 2:
    print("0M + 0C + {}D + {}U".format(numero[0], numero[1]))
elif len(numero) == 3:
    print("0M + {}C + {}D + {}U".format(numero[0], numero[1], numero[2]))
elif len(numero) == 4:
    print("{}M + {}C + {}D + {}U".format(numero[0], numero[1], numero[2], numero[3]))
else:
    print("Número inválido")

