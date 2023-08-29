rut = (input("Ingrese un rut sin el digito verificador: "))
num_1 = int(rut[len(rut)- 1]) * 2
num_2 = int(rut[len(rut)- 2]) * 3
num_3 = int(rut[len(rut)- 3]) * 4
num_4 = int(rut[len(rut)- 4]) * 5 
num_5 = int(rut[len(rut)- 5]) * 6 
num_6 = int(rut[len(rut)- 6]) * 7
num_7 = int(rut[len(rut)- 7]) * 2
num_8 = int(rut[len(rut)- 8]) * 3
contador = int(1)
control = int(10)
num = int(rut)
while control <= num:
    contador = contador + 1
    control = control *10
dato_1 = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8
dato_2 = int(dato_1 / 11)
dato_3 = dato_1 - (11 * dato_2)
dato_4 = 11 - dato_3
dato_5 = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7
dato_6 = int(dato_5 / 11)
dato_7 = dato_5 - (11 * dato_6)
dato_8 = 11 - dato_7
x = "dv="
if contador == 8:
    if dato_4 == 11:
        print(x + "0")
    elif dato_4 == 10:
        print(x + "K")
    else:
        print(x + str(dato_4))
else:
    contador == 7
    if dato_8 == 11:
        print(x + "0")
    elif dato_8 == 10:
        print(x + "K")
    else:
        print(x + str(dato_8))