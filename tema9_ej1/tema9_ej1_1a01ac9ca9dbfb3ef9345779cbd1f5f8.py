class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            if "#laroja" in mensaje:
                hashtag=mensaje.count("#laroja")
                self.trending_topics.append("#laroja")
                lista_mensaje=mensaje.split(" ")
                lista_mensaje.remove("#laroja")
                if "#laroja" in mensaje:
                    self.trending_topics.append("#laroja")
                else:
                    pass
                    
            if "#chile" in mensaje:
                self.trending_topics.append(("#chile"))


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)