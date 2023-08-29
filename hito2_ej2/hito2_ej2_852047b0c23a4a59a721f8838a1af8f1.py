def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas

    letras_validas = 'ACTG' # Letras válidas para el genoma

    for letra in secuencia:
        if letra not in letras_validas:
            print('secuencia incorrecta')
            return 'incorrecta'

    print('secuencia correcta')
    return 'correcta'
    
sec = input('-> ')
valor = validar_secuencia(sec)
print(valor)