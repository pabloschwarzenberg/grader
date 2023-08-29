from os import system

system('cls')

#entrada
rut = int(input("Ingrese el rut a verificar: "))
print("Su rut ingresado es", str(rut) + ".")

#proceso
oper_rut = str(rut)
rut_size = len(oper_rut)
if rut_size == 8:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[-3])
    digit_3 = int(oper_rut[-4])
    digit_4 = int(oper_rut[-5])
    digit_5 = int(oper_rut[-6])
    digit_6 = int(oper_rut[-7])
    digit_7 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4
    digit_3 *= 5
    digit_4 *= 6
    digit_5 *= 7
    digit_6 *= 2
    digit_7 *= 3

    digits_sum = digit_0 + digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 7:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[-3])
    digit_3 = int(oper_rut[-4])
    digit_4 = int(oper_rut[-5])
    digit_5 = int(oper_rut[-6])
    digit_6 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4
    digit_3 *= 5
    digit_4 *= 6
    digit_5 *= 7
    digit_6 *= 2

    digits_sum = digit_0 + digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 6:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[-3])
    digit_3 = int(oper_rut[-4])
    digit_4 = int(oper_rut[-5])
    digit_5 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4
    digit_3 *= 5
    digit_4 *= 6
    digit_5 *= 7

    digits_sum = digit_0 + digit_1 + digit_2 + digit_3 + digit_4 + digit_5
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 5:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[-3])
    digit_3 = int(oper_rut[-4])
    digit_4 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4
    digit_3 *= 5
    digit_4 *= 6

    digits_sum = digit_0 + digit_1 + digit_2 + digit_3 + digit_4
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 4:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[-3])
    digit_3 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4
    digit_3 *= 5

    digits_sum = digit_0 + digit_1 + digit_2 + digit_3
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 3:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[-2])
    digit_2 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3
    digit_2 *= 4

    digits_sum = digit_0 + digit_1 + digit_2
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

elif rut_size == 2:
    digit_0 = int(oper_rut[-1])
    digit_1 = int(oper_rut[0])

    digit_0 *= 2
    digit_1 *= 3

    digits_sum = digit_0 + digit_1
    residue_digits_sum = digits_sum % 11
    resta_module_11 = 11 - residue_digits_sum

    if resta_module_11 == 11:
        dv = 0
    elif resta_module_11 == 10:
        dv = 'K'
    elif resta_module_11 != 10 and resta_module_11 != 11:
        dv = resta_module_11

    print("dv=" + str(dv))

else:
    print("dv=0")