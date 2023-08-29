class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = self.extract_hashtags(mensaje)
            self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        hashtags = []
        words = mensaje.split()

        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])

        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
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
