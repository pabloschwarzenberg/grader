class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            a=mensaje.split(" ")
            lista_hashtags=[]
            comillas=""
            for i in a:
                if i[0]=="#":
                    lista_hashtags += i
                    b=comillas.join(lista_hashtags)
            c=b.split("#")[1:]
            self.trending_topics.extend(c)
        lista=[]
        for k in self.trending_topics:
            veces_quehay_hashtag=self.trending_topics.count(k)
            lista+=[[k,veces_quehay_hashtag]]
        lista.sort(key= lambda x: x[1], reverse = True)
        lista.remove

        new = []
        for valor in lista:
            if valor not in new:
                new.append(valor)
        ultima = []
        for j in new:
            ultima.append(j[0])
        self.trending_topics=ultima
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           