class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
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

    def get_trending_topics(self):
        return self.trending_topics


# Ejemplo de uso
twitter = Twitter()
twitter.tweet("I love #programming!")
twitter.tweet("Just finished an amazing book #reading")
twitter.tweet("Working on a new project #coding #python")
twitter.tweet("Excited for the #weekend")

print("Trending Topics:")
trending_topics = twitter.get_trending_topics()
for topic in trending_topics:
    print(f"#{topic[0]} - {topic[1]} mentions")

