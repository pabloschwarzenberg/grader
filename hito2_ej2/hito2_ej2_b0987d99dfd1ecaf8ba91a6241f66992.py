def validar_secuencia(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in 'ACTG':
            return False
    return True

secuencia = input("Ingrese la secuencia de ADN: ")

secuencia_valida = validar_secuencia(secuencia)

if secuencia_valida:
    print("la secuencia es correcta.")
else:
    print("la secuencia es incorrecta.")   