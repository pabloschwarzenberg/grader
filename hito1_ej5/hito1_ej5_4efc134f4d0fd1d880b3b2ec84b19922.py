#Cálculo del dígito verificador de un rut
def calcular_verificador(rut):
    rut = str(rut)
    reversed_rut = reversed(rut)
    multipliers = [2, 3, 4, 5, 6, 7]
    multiplier_index = 0
    accumulator = 0

    for digit in reversed_rut:
        accumulator += int(digit) * multipliers[multiplier_index]
        multiplier_index = (multiplier_index + 1) % len(multipliers)

    verifier_digit = 11 - (accumulator % 11)
    if verifier_digit == 11:
        verifier_digit = 0
    elif verifier_digit == 10:
        verifier_digit = "k"

    return verifier_digit


rut = input("Ingrese su Rut sin dígito verificador: ")
verificador = calcular_verificador(rut)
print("dv =", verificador)






