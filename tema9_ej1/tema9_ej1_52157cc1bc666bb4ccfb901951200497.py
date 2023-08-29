class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
            for hashtag in hashtags:
                found = False
                for topic in self.trending_topics:
                    if hashtag == topic[0]:
                        topic[1] += 1
                        found = True
                        break
                if not found:
                    self.trending_topics.append([hashtag, 1])

            self.trending_topics.sort(key=lambda x: x[1], reverse=True)
            self.trending_topics = self.trending_topics[:3]

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("¡Ganó #laroja!")
    twitter.tweet("¡Grande #chile!")
    twitter.tweet("#laroja con dos goles, le ganó a Brasil. ¡Grande #laroja!")
    print(twitter.trending_topics)
