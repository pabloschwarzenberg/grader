 def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas

    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return "secuencia incorrecta"
    return "secuencia correcta"
if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    resultado = validar_secuencia_genoma(secuencia)
    print(resultado)
     