def rot13(palabra):
    abcdario = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    abcdario = abcdario.split(' ')
    palabra2 = ''
    for i in palabra:
        if abcdario.index(i)+13 > 25:
            palabra2 += abcdario[abcdario.index(i)+13-26]
        else:
            palabra2 += abcdario[abcdario.index(i)+13]
    return palabra2

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           