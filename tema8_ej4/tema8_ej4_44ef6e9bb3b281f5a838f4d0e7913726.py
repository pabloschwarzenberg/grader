def rot13(palabra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto = [l for l in alfabeto]
    alfa_len = len(alfabeto)
    palabra_rot13 = ''
    print(alfa_len)
    for i in range( 0, len(palabra) ):
        char_i = alfabeto.index( palabra[i] ) + 14
        if char_i > alfa_len:
            char_i = char_i - alfa_len
        palabra_rot13 += alfabeto[char_i - 1]
        
    return palabra_rot13

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           