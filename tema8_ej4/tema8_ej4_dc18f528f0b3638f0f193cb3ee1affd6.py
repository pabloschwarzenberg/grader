def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    traduccion = letras[13:]+letras[:13]
    rot_char = lambda i: traduccion[letras.find(i)] if letras.find(i) >-1 else i
    return ''.join( rot_char(i) for i in palabra ) 

if __name__ == '__main__':
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)