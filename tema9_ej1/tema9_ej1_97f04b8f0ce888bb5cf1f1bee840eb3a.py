class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            Lista = mensaje.split(" ")
            for Palabra in Lista:
                if Palabra[0] == "#":
                    if Palabra not in self.trending_topics:
                        self.trending_topics.append(Palabra)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           