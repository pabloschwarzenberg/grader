from string import ascii_lowercase, ascii_uppercase
def rot13(texto):
    resultado = []
    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevoIndice = (indice + 13) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevoIndice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevoIndice= (indice + 13) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevoIndice])
        else: 
            resultado.append(c)
    return ''.join(resultado)

if __name__ == "__main__": 
  texto = 'hola'
  print(rot13(texto))