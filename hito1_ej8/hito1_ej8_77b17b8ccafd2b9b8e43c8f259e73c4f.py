'''
Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en 
Unidades, Decenas, Centenas y Miles. Ejemplos

Para 1230 debe imprimir: 1M + 2C + 3D + 0U
Para 36 debe imprimir: 3D + 6U
'''

num = str(input("ingrese un numero: "))

while not (len(num) <= 4):
    num = str(input("ingrese un numero: "))


largo = len(num)
if(largo == 4):
    print(num[0]+"M + "+num[1]+"C + "+num[2]+"D + "+num[3]+"U")
elif(largo == 3):
    print(num[0]+"C + "+num[1]+"D + "+num[2]+"U")
elif(largo == 2):
    print(num[0]+"D + "+num[1]+"U")
else:
    print(num[0]+"U")