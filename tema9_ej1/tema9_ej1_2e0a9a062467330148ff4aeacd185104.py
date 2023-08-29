class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            self.update_trending_topics(message)
        else:
            print("El tweet excede el límite de 140 caracteres.")

    def update_trending_topics(self, message):
        hashtags = self.extract_hashtags(message)
        for hashtag in hashtags:
            self.increment_hashtag_count(hashtag)

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def increment_hashtag_count(self, hashtag):
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return
        self.trending_topics.append([hashtag, 1])
        self.sort_trending_topics()

    def sort_trending_topics(self):
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]



twitter = Twitter()

twitter.tweet("Hoy es un buen día para aprender #Python")
twitter.tweet("Me encanta programar en #Python, es genial!")
twitter.tweet("Estoy emocionado por el próximo meetup de #Python")
twitter.tweet("Qué tal si organizamos un evento de #Python en nuestra ciudad?")
twitter.tweet("El lenguaje de programación #Python está en auge")

print("Trending topics:", twitter.trending_topics)
           