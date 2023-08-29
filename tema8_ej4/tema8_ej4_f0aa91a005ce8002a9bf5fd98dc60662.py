def rot13(s) :
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    palabra_encriptada = ''
    for letra in s :
        a = alfabeto.find(letra)
        if a != -1 :
            palabra_encriptada += alfabeto[a - 13]
        if a == -1 :
            palabra_encriptada += alfabeto[a + 13]
    return palabra_encriptada
if __name__ == "__main__":
 while True:
  rot13(input())



