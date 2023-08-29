 #Importante: en este ejercicio tu programa debe recibir los valores con input y luego imprimir 
#el resultado con print. Como parte de tu programa puedes crear y usar las funciones que necesites


def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    for letra in secuencia:
        if letra not in "ACTG":
            return "secuencia incorrecta"
    return "secuencia correcta"

secuencia = input("Ingrese la secuencia del genoma: ")
print(validar_secuencia_genoma(secuencia))