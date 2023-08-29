def rot13(palabra):
    rot_a = 'abcdefghijklm'
    rot_b = 'nopqrstuvwxyz'
    palabra = list(palabra)

    for pos in range(len(palabra)): 
        letra = palabra[pos]
        if letra in rot_a: 
            rot_pos = rot_a.find(letra)
            palabra[pos] = rot_b[rot_pos]

        elif palabra[pos] in rot_b: 
            rot_pos = rot_b.find(letra)
            palabra[pos] = rot_a[rot_pos]
        
    palabra = ''.join(palabra)
    return palabra


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
           