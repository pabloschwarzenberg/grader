class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]

        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])

        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

    def get_trending_topics(self):
        return self.trending_topics


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.get_trending_topics())