class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
            for hashtag in hashtags:
                self.update_trending_topics(hashtag)
        else:
            print("El mensaje excede el límite de 140 caracteres.")

    def update_trending_topics(self, hashtag):
        found = False
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                found = True
                break
        if not found:
            self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print("Trending topics:")
    for topic in twitter.trending_topics:
        print(topic[0] + " - " + str(topic[1]) + " menciones")
