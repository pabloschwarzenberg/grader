def binario_a_decimal(numero):
    g=[]
    for i in range(0,len(numero)):
        x= (2**(len(numero)-(i+1))*int(numero[i]))
        g.append(x)
    numero=0
    for i in range(0,len(g)):
        numero=numero+int(g[i])

    return numero

def decodificar(mensaje):
    characters=("""! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~""").split(" ")
    mensaje=mensaje.split(",")
    g=[]
    for i in range(0,len(mensaje)):
        number=binario_a_decimal(mensaje[i])-33
        g.append(characters[number])
    mensaje="".join(g)
    return mensaje


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
