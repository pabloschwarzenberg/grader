#Sistema de Ecuaciones
numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())
numero_4 = int(input())
numero_5 = int(input())
numero_6 = int(input())

numero_4 = (numero_1 * numero_5) - (numero_2 * numero_4)
if numero_4 != 0 :
    valor_de_x = numero_5 * numero_3 - numero_2 * numero_6
    x = round(valor_de_x/numero_4,1)
    valor_de_y = numero_1 * numero_6 - numero_4 * numero_3
    y = round(valor_de_y / numero_4,1)
    print("x = ",x)
    print("y = ",y)

