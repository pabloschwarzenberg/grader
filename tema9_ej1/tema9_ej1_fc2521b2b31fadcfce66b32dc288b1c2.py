class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        contador=1
        if len(mensaje)<=140:
            veces_repetido=self.trending_topics.count(mensaje)
            if veces_repetido>0:
                self.trending_topics.remove(mensaje)
            veces_repetido=str(veces_repetido)
            self.trending_topics.append(mensaje)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           