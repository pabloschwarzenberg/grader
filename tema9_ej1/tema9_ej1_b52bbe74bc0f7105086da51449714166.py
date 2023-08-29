class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            lista=mensaje.split(" ")
            for i in lista:
                for j in list(i):
                    if j == "#":
                        self.trending_topics.append(i)
        return  self.trending_topics

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(len(twitter.trending_topics[2:]))
           