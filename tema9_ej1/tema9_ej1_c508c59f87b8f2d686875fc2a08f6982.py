class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            for i in range(len(mensaje)):
                letra=mensaje[i]
                sub_mensaje=mensaje[i:len(mensaje)]
                sub_mensaje_l=list(sub_mensaje)
                if letra=="#":
                    indice=0
                    espacios=sub_mensaje_l.count(" ")
                    if espacios==0:
                        self.trending_topics.append(sub_mensaje)
                    if espacios!=0:
                        indice=sub_mensaje_l.index(" ")
                        topic=sub_mensaje[0:indice]
                        self.trending_topics.append(topic)
        for i in self.trending_topics:
            veces=self.trending_topics.count(i)
            if veces>1:
                while veces>1:
                    self.trending_topics.remove(i)
                    veces-=1

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           