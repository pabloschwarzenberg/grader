class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = self.extract_hashtags(mensaje)

        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def extract_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags

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
