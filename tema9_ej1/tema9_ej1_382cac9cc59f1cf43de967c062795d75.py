class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.listah=[]
        self.listacontador=[]
        self.listafinal = []


    def tweet(self,mensaje):
        if len(mensaje)<=140:
            n=1
            while "#" in mensaje:
                pos=mensaje.find("#")
                mensaje=mensaje[pos+1:]
                self.listah.append(mensaje)

            for i in self.listah:
                if " " in i:
                    pos2=i.find(" ")
                    index=self.listah.index(i)
                    self.listah.append(i[0:pos2])
                    self.listah.pop(index)

        else:
            print("Su mensaje sobrepasa 140 caracteres")
        #debería ocurrir que al recibir un tweet se actualize automáticamente
        #la lista de trending_topics
        #o sea se debería llamar a la función contador
        #pero agregando solamente los trending topics nuevos

        self.contador()

    def contador(self):
        #dado que el método contador se puede llamar varias veces
        #las listas debieran inicializarse
        #esto se puede optimizar para que cada vez que se reciba un tweet con hashtag
        #se aumente el conteo de la lista de trending topics
        #en vez de crearse desde cero cada vez
        self.listacontador=[]
        self.listafinal=[]
        self.trending_topics=[]

        for i in self.listah:
            contador=self.listah.count(i)
            count=[contador,i]
            self.listacontador.append(count)
        self.listacontador.sort(reverse=True)

        for i in self.listacontador:
             if i not in self.listafinal:
                 self.listafinal.append(i)

        self.trending_topics=[]
        for i in self.listafinal:
            self.trending_topics.append(i[1])


if __name__ == "__main__":

    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.contador()
    print(twitter.trending_topics)

