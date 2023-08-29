#Cálculo del dígito verificador de un rut
rut = input("Ingrese un número de RUT: ")

reversed_rut = reversed(rut)
multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
total = sum(int(digito) * multiplicador for digito, multiplicador in zip(reversed_rut, multiplicadores))
resto = total % 11
verificador = 'k' if resto == 1 else str(11 - resto) if resto != 0 else '0'

print("dv =", verificador)
