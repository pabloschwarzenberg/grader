      def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para evitar distinción entre mayúsculas y minúsculas
    letras_validas = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    
    return True

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    
    if validar_secuencia_genoma(secuencia):
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
