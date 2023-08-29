class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        
        if len(mensaje) < 140:
            men = mensaje.split(' ')
            for index, i in enumerate(men):
                for has in i:
                    if has == "#":
                        if i not in self.trending_topics:
                            self.trending_topics.append(i)
        

twitter = Twitter()
twitter.tweet("gano #laroja")
twitter.tweet("grande #chile")
twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
print(twitter.trending_topics)
