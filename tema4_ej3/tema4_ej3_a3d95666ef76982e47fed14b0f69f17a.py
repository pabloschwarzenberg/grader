def jerigonzo(texto):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    resultado = ''
    for caracter in texto:
        resultado += caracter
        if caracter in vocales:
            resultado += 'p' + caracter
     return resultado

if __name__ == "__main__":
    texto = 'Hola mundo'
    resultado = traducir_a_jerigonzo(texto)
    print(resultado)  
    pass
         