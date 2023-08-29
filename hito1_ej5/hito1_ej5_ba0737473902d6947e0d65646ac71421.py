rut = int(input("digite su rut:"))
number_string = (str(rut))

if len(number_string) == 8:
    x1 = int(number_string[0]) * 3
    x2 = int(number_string[1]) * 2
    x3 = int(number_string[2]) * 7
    x4 = int(number_string[3]) * 6
    x5 = int(number_string[4]) * 5
    x6 = int(number_string[5]) * 4
    x7 = int(number_string[6]) * 3
    x8 = int(number_string[7]) * 2
    x = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
    dv = (11 - (x - 11 * (int(x / 11))))
if len(number_string) == 7:
    x1 = int(number_string[0]) * 2
    x2 = int(number_string[1]) * 7
    x3 = int(number_string[2]) * 6
    x4 = int(number_string[3]) * 5
    x5 = int(number_string[4]) * 4
    x6 = int(number_string[5]) * 3
    x7 = int(number_string[6]) * 2

    x = x1 + x2 + x3 + x4 + x5 + x6 + x7
    dv = (11 - (x - 11 * (int(x / 11))))
if dv < 10:
    print("dv=", dv)
if dv==10:
    print("dv=K")
if dv==11:
    print("dv=0")
