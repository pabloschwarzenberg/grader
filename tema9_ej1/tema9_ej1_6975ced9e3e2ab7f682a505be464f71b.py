class Twitter:
    def __init__(self):
        self.trending_topics = []


    def tweet(self, mensaje):
        hashtag = []
        if len(mensaje) in list(range(0,141)):
            mensaje = mensaje.split(" ")
            for i in mensaje:
                if "#" in i:
                    if i not in self.trending_topics:
                        self.trending_topics.append(i)





if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
