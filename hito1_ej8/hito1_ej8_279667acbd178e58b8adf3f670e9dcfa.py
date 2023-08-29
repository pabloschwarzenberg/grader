#Descomponer un número
numero = input('Ingrese un número: ')
cantidad_num = len(numero)
int_numero = int(numero)
i = 0
while i < cantidad_num:
    if i == 0:
        unidades = (int_numero // 10**i) % 10
    elif i == 1:
        decenas = (int_numero // 10**i) % 10
    elif i == 2:
        centenas = (int_numero // 10**i) % 10
    elif i == 3:
        miles = (int_numero // 10**i) % 10
    i += 1
if cantidad_num == 1:
    print(('{}U').format(unidades))
elif cantidad_num == 2:
    print(('{}D + {}U').format(decenas,unidades))
elif cantidad_num == 3:
    print(('{}C + {}D + {}U').format(centenas,decenas,unidades))
elif cantidad_num == 4:
    print(('{}M + {}C + {}D + {}U').format(miles,centenas,decenas,unidades))