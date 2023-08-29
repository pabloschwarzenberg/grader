def rot13(palabra):
    Abecedario ='a b c d e f g h i j k l m n o p q r s t u v w x y z '.split()
    Abecedario2='n o p q r s t u v w x y z a b c d e f g h i j k l m' .split()
    string=list(palabra)
    lista2=[]
    lista3=[]
    for i in string:
        for z in Abecedario:
            if i==z:
                resultado=Abecedario.index(i)
                lista2.append(resultado)
    for x in range(len(lista2)):
            resultado=lista2[x]
            resultado2=Abecedario2[resultado]
            lista3.append(resultado2)
    palabra = (''.join(lista3))
    return  palabra
           