def rot13(palabra):

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'*2

    copia = ''
    for letra in palabra:

        indice_letra = alfabeto.index(letra)
        
        copia = copia + alfabeto[indice_letra + 13]
    
    return copia
           