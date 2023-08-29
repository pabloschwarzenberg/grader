num = int(input("Ingresa un númer de hasta 4 dígitos: ")[0:4])

res = [int(x) for x in str(num)]

if len(res) < 2:
    print(str(res[-1]) + 'U')
elif len(res) < 3:
    print(str(res[-2]) + 'D + ' + str(res[-1]) + 'U')
elif len(res) < 4:
    print(str(res[-3]) + 'C + ' + str(res[-2]) + 'D + ' + str(res[-1]) + 'U')
elif len(res) < 5:
    print(str(res[-4]) + 'M + ' + str(res[-3]) + 'C + ' + str(res[-2]) + 'D + ' + str(res[-1]) + 'U')