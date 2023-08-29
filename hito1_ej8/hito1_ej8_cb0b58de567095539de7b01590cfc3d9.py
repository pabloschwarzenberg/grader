#Descomponer un número
num = input("Ingrese un número de 4 dígitos a descomponer: ")
num = int(num)
num_str = str(num)
digits = [int(digit) for digit in num_str]

descomposicion = []

if len(num_str) == 4:
    descomposicion.append(str(digits[0]) + "M")
    descomposicion.append(str(digits[1]) + "C")
    descomposicion.append(str(digits[2]) + "D")
    descomposicion.append(str(digits[3]) + "U")
elif len(num_str) == 3:
    descomposicion.append(str(digits[0]) + "C")
    descomposicion.append(str(digits[1]) + "D")
    descomposicion.append(str(digits[2]) + "U")
elif len(num_str) == 2:
    descomposicion.append(str(digits[0]) + "D")
    descomposicion.append(str(digits[1]) + "U")
elif len(num_str) == 1:
    descomposicion.append(str(digits[0]) + "U")

resultado = " + ".join(descomposicion)
print(resultado)