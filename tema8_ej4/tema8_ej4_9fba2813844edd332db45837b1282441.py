from string import ascii_lowercase, ascii_uppercase 

def rot13(palabra):
    resultado = []
    for c in palabra:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + 13) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + 13) % len(ascii_uppercase)
            resultado.append([nuevo_indice])
    
    return "".join(resultado)

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           