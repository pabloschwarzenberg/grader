def traducir_a_jerigonzo(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultado = []
    
    for letra in texto:
        resultado.append(letra)
        
        if letra.lower() in vocales:
            resultado.append('p' + letra.lower())
    
    return ''.join(resultado)

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
