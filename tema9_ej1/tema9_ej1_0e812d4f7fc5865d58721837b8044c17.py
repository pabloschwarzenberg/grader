class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        mensaje = mensaje[:140]

        separado = mensaje.split(' ')
        for word in separado:
            check = True
            if word[0] == '#':
                for n in range(len(self.trending_topics)):
                    if word in self.trending_topics[n][0]:
                        self.trending_topics[n][1] += 1
                        check = False
                if check:
                    self.trending_topics.append([word,1])

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)