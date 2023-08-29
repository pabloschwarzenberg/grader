def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    cifrado_cesar = ""
    for letra in palabra:
        print(abecedario.find(letra))
        qwe =abecedario.find(letra) + 13
        asd = int(qwe) % len(abecedario)
        cifrado_cesar = cifrado_cesar + str(abecedario[asd])
              
    return cifrado_cesar