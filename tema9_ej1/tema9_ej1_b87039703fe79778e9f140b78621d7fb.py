class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            self.mensaje=mensaje
        else:
            self.mensaje!=mensaje
            
        b=self.mensaje.split(" ")
        for i in range(len(b)):
            if b[i][0]=="#":
                c=[]
                c.append(b[i])
        for i in range(len(c)):
            if self.trending_topics.count(c[i])==0:
                self.trending_topics.append(c[i])
            else:
                pass
        return self.trending_topics
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           