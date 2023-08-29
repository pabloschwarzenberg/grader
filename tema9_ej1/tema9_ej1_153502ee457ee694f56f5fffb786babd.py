class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.numero_trending = []
    def trending(self, topics):
        if not self.trending_topics:
            self.trending_topics.append(topics)
            self.numero_trending.append(1)
        else:
            igual = len(self.trending_topics)
            distinto = igual
            for i in range(len(self.trending_topics)):
                print(self.trending_topics)
                print(self.numero_trending)
                hashtag = self.trending_topics[i]
                if hashtag == topics:
                    self.numero_trending[i] = self.numero_trending[i] + 1
                else:
                    distinto -= 1
            if distinto == 0:
                self.trending_topics.append(topics)
                self.numero_trending.append(1)

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            return False
        else:
            inicio_hashtag = ""
            mensaje = mensaje + " "
            for i in range(len(mensaje)):
                hashtag = mensaje[i]
                if hashtag == "#":
                    inicio_hashtag = i+1
                if inicio_hashtag != "" and hashtag == " ":
                    final_hashtag = i
                    hashtag_real = mensaje[inicio_hashtag:final_hashtag]
                    inicio_hashtag = ""
                    self.trending(hashtag_real)
            return True


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           