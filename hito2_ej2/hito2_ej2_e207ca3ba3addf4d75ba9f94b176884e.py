      def validar_genoma(secuencia):
    # Convertir la secuencia a letras mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in 'ACTG':
            return 'secuencia incorrecta'

    return 'secuencia correcta'

# Solicitar al usuario que ingrese una secuencia de ADN
secuencia_ingresada = input("Ingrese una secuencia de ADN: ")

# Validar la secuencia ingresada
resultado = validar_genoma(secuencia_ingresada)

# Imprimir el resultado
print(resultado)
