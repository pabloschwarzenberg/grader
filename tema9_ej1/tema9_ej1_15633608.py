class hashtag:
    def __init__(self):
        self.hashtag=""
        self.veces=0
    def __rep__(self):
        return (self.hashtag,self.veces)
    def agregar(self,nombre):
        self.hashtag=nombre
        self.veces= 1
    def sumar(self,veces):
        self.veces=self.veces+veces
        

class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        hashtags=[]
        if len(mensaje)>140:
            return None
        else:
            c=0
            for i in mensaje:
                if i =="#":
                    existe = False
                    for e in range(c,len(mensaje)):
                        try:
                            if mensaje[e+1]==" ":
                                break
                        except: IndexError
                    for y in hashtags:
                        if y.hashtag == mensaje[c:e+1]:
                            y.sumar(1)
                            existe=True
                    for y in self.trending_topics:
                        if y == mensaje[c:e+1]:
                            existe=True
                    if not existe:
                        a=hashtag()
                        a.agregar(mensaje[c:e+1])
                        hashtags.append(a)
                        self.trending_topics.append(a.hashtag)

                c=c+1

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           