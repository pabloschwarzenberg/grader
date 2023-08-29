class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.hashtags = {}

    def actualizar_trending(self):
        self.trending_topics.clear()
        cantidad = []
        for clave in self.hashtags:
            cantidad.append(self.hashtags[clave])
        cantidad.sort()
        for clave in self.hashtags:
            if self.hashtags[clave]==cantidad[-1]:
                self.trending_topics.append(clave)
            elif self.hashtags[clave]==cantidad[-2]:
                self.trending_topics.append(clave)
            elif self.hashtags[clave]==cantidad[-3]:
                self.trending_topics.append(clave)

    def agregar_hashtags(self,palabra):
        if self.hashtags.get(palabra)==None:
            self.hashtags[palabra]=0
        self.hashtags[palabra]=self.hashtags[palabra]+1
        self.actualizar_trending()

    def tweet(self, mensaje):
        if len(mensaje)>140:
            return 'Tu mensaje debe tener a lo más 140 caracteres'
        i=0
        while i<len(mensaje):
            c = mensaje[i:].find('#')+i
            if c<i:
                break
            alfabeto='abcdefghijklmnopqrstuvwxyz'
            p=c+1
            while p<len(mensaje):
                if mensaje[p] not in alfabeto:
                    self.agregar_hashtags(mensaje[c:p])
                    break
                elif p==(len(mensaje)-1):
                    self.agregar_hashtags(mensaje[c:p+1])
                    break
                p=p+1
            i=c+1
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           