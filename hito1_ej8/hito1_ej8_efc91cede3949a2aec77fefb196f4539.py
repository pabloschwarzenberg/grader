"""
9.- Escribe un programa que le pida al usuario un número de hasta 4 dígitos
y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. Ejemplos
•	Para 1230 debe imprimir: 1M + 2C + 3D + 0U
•	Para 36 debe imprimir: 3D + 6U
"""

numero = input("Ingrese un número de hasta 4 digitos: ")
while not len(numero) <= 4:
    print("\nEl número ingresado tiene más de 4 digitos.")
    int(input("Ingrese un número de hasta 4 digitos: "))

if len(numero) == 4:
    numero_descompuesto = f"{numero[0]}M + {numero[1]}C + {numero[2]}D + {numero[3]}U"

if len(numero) == 3:
    numero_descompuesto = f"{numero[0]}C + {numero[1]}D + {numero[2]}U"

if len(numero) == 2:
    numero_descompuesto = f"{numero[0]}D + {numero[1]}U"

if len(numero) == 1:
    numero_descompuesto = f"{numero[0]}U"

print(numero_descompuesto)