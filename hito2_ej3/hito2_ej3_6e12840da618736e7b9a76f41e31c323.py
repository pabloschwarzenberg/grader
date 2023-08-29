import re

def validar_secuencia(secuencia):
    # Expresión regular para validar la secuencia del genoma
    patron = r"^[ACTG]+$"
    
    # Verificar si la secuencia coincide con el patrón
    if re.match(patron, secuencia, re.IGNORECASE):
        return "secuencia correcta"
    else:
        return "secuencia incorrecta"

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia del genoma: ")
    resultado = validar_secuencia(secuencia)
    print(resultado)
      