numero = int(input("Ingrese su número: "))
if numero > 999:
    num_a = str(numero)
    print("{}M + {}C + {}D + {}U".format(num_a[0],num_a[1],num_a[2],num_a[3]))
elif numero < 999 and numero > 99:
    num_a = str(numero)
    print("0M + {}C + {}D + {}U".format(num_a[0],num_a[1],num_a[2]))
elif numero < 99 and numero > 9:
    num_a = str(numero)
    print("0M + 0C + {}D + {}U".format(num_a[0],num_a[1]))
elif numero > 0 and numero < 9:
    num_a = str(numero)
    print("0M + 0C + 0D + {}U".format(num_a[0]))