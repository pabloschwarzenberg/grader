class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def __repr__(self):
        return self.trending_topics

    def tweet(self,mensaje):
        if len(mensaje)>140:
            return "Twit inválido"
        else:
            mensaje=mensaje.split(" ")
            for i in mensaje:
                if i[0]=="#":
                    j=[]
                    k=0
                    while k < len(self.trending_topics):
                        if self.trending_topics[k][0]==i:
                            self.trending_topics[k][1]=self.trending_topics[k][1]+1
                            k=len(self.trending_topics)+1
                        else:
                            k=k+1
                    while k == len(self.trending_topics):
                        j=[i,1]
                        self.trending_topics.append(j)
            if len(self.trending_topics)>3:
                for i in self.trending_topics:
                    i.reverse()
                self.trending_topics.sort()
                self.trending_topics.pop(0)
                return self.trending_topics

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           