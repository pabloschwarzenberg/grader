class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        contador=0
        if len(mensaje)<=140:
            mensaje=mensaje.split(" ")
            for h in range(len(mensaje)):
                if "#" in mensaje[h]:
                    if mensaje[h] in self.trending_topics:
                        contador+=1
                        
                    else:
                        self.trending_topics.append(mensaje[h])
        return self.trending_topics
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           