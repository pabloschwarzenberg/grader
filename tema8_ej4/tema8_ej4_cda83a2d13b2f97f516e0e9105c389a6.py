def rot13(s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    palabra_encriptada = ''
    for letra in s :
        a = alfabeto.find(letra)
        if a > 12 :
            palabra_encriptada += alfabeto[a - 13]
        if a <= 12 :
            palabra_encriptada += alfabeto[a + 13]
    return palabra_encriptada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           