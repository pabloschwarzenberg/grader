import random as ran
def ocultar_letras(palabra,cantidad):
    pal=palabra
    cant=cantidad
    pala=list(palabra)
    pl=""
    while cant>0:
        int=ran.randint(0,len(pal)-1)
        while pala[int]=="_":
            int = ran.randint(0, len(pal)-1)
        pala[int]="_"
        cant=cant-1
    for n in pala:
        pl=pl+n
    return pl

def revisar_letra(palabra_secreta,palabra,letra):
    sr=list(palabra)
    letras=list(letra.lower() )
    k=0
    pal=""
    for let in letras:
        k=0
        for l in palabra_secreta:
            if let==l:
                sr[k]=let
            k=k+1
    for n in sr:
        pal=pal+n
    return pal

if __name__ == "__main__":
    diccionario=["comida","pasto","fuego","mesa","frio"
    ,"aparato","soledad","amor","frio","dolor"
    ,"alegria","globos","fiesta","deporte","paralelepipedo"
    ,"lepidoptero","jaidefinichon","starwars","halconmilenario",]
    numerador="si"
    while numerador!="no":
        print("!!Bienvenido!!, la palabra oculta es:\n")
        num=ran.randint(0,len(diccionario)-1)
        pal=diccionario[num]
        can=ran.randint(1,(len(pal)))
        pal_ocul=ocultar_letras(pal,can)
        print(">>>>  "+pal_ocul+"\n")
        re=7
        while re>=0 and pal!=pal_ocul:
            letra=input("Ingrese una letra o varias, le quedan %d intentos\n>> "%(re))
            pal_ocul=revisar_letra(pal,pal_ocul,letra)
            print(">>>> "+pal_ocul)
            re=re-1
        if pal_ocul==pal:
            print("Felicitaciones, lo consegiste!!!")
            numerador=input(" Desea jugar nuevamente:\n->> si\n->> no\n>>")
        else:
            print("Ooow, No lo lograste, la palabra correcta era %s "%(pal))
            numerador = input(" Desea jugar nuevamente:\n->> si\n->> no\n>>")
    pass