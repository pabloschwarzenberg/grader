class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede los 140 caracteres.")
            return

        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        hashtags = []
        words = message.split()
        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])
        return hashtags

    def update_trending_topics(self, hashtags):
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

    def show_trending_topics(self):
        print("Trending topics:")
        for topic in self.trending_topics:
            print("#{}: {} menciones".format(topic[0], topic[1]))


if __name__ == "__main__":
    twitter = Twitter()

    twitter.tweet("¡Hola mundo! #python #programming")
    twitter.tweet("Hoy es un buen día para aprender #programming")
    twitter.tweet("Me encanta el lenguaje #python")

    twitter.show_trending_topics()