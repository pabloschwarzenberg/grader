numero = input()
largo = len(numero)
resultado = ""

if largo >= 4:
    miles = numero[largo-4]
    resultado += miles+"M + "

if largo >= 3:
    centenas = numero[largo-3]
    resultado += centenas+"C + "

if largo >= 2:
    decenas = numero[largo-2]
    resultado += decenas+"D + "

if largo >= 1:
    unidades = numero[largo-1]
    resultado += unidades+"U"

print(resultado)
      