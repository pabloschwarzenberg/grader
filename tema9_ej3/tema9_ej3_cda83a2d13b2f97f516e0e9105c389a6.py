def binario(s):
    caracteres_imprimibles=("""! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
    @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _
    ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~""")
    lista = caracteres_imprimibles.split()
    lista.insert(0," ")
    letra = lista[s]
    return letra

def decodificar(s) :
    lista_s = s.split(",")
    print(lista_s)
    palabra = []
    while len(lista_s) > 0 :
        decimal = int(lista_s[0],2) - 32
        letra = binario(decimal)
        palabra.append(letra)
        lista_s.pop(0)
    palabra_final = ''.join(palabra)
    return palabra_final
   