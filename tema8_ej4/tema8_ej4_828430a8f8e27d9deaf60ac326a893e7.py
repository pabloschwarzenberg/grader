def rot13(palabra):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    for letra in palabra:
        print(abc.find(letra))
        su =abc.find(letra) + 13
        mod = int(su) % len(abc)
        cifrado = cifrado + str(abc[mod])
              
    return cifrado


    
           