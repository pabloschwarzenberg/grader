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
                hashtag = word[1:]  # Remove the '#' symbol
                hashtags.append(hashtag)
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


# Ejemplo de uso
twitter = Twitter()

# Tweets de ejemplo
tweet1 = "Hoy es un gran día para programar. #coding #programacion #Python"
tweet2 = "Estoy emocionado por el lanzamiento de #OpenAI. #AI #machinelearning"
tweet3 = "Compartiendo algunos consejos de #productividad. #tips"

twitter.tweet(tweet1)
twitter.tweet(tweet2)
twitter.tweet(tweet3)

print("Trending Topics:")
for topic in twitter.trending_topics:
    print(f"Hashtag: {topic[0]}, menciones: {topic[1]}")