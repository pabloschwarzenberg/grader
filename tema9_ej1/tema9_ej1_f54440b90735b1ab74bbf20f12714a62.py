class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            l_aux = mensaje.split()
            for a in range(0, len(l_aux)):
                if "#" in l_aux[a] and l_aux[a] not in self.trending_topics:
                    self.trending_topics.append(l_aux[a])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           