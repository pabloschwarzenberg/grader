texto = input("ingrese una frase: ")
from string import ascii_lowercase, ascii_uppercase
def cifrado_cesar(texto, pasos):
    resultado = []

    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice+pasos) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevo_indice])
    return''.join(resultado)
print(cifrado_cesar(texto,1))