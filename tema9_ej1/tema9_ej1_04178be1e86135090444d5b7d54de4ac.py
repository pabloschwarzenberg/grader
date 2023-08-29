class Twitter:
    def __init__(self, trending_topics=[]):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje = mensaje
        self.mensaje.append(treding_topics)
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           