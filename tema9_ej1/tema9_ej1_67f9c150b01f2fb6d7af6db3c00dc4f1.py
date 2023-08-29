class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            hashtags = self.extract_hashtags(message)
            for hashtag in hashtags:
                self.update_trending_topics(hashtag)
        else:
            print("El mensaje excede los 140 caracteres.")

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic["hashtag"] == hashtag:
                topic["count"] += 1
                return
        self.trending_topics.append({"hashtag": hashtag, "count": 1})
        self.trending_topics.sort(key=lambda x: x["count"], reverse=True)
        if len(self.trending_topics) > 3:
            self.trending_topics = self.trending_topics[:3]

    def show_trending_topics(self):
        if len(self.trending_topics) > 0:
            print("Trending Topics:")
            for topic in self.trending_topics:
                print("#{}: {} menciones".format(topic["hashtag"], topic["count"]))
        else:
            print("No hay trending topics por el momento.")


if __name__ == "__main__":
    twitter = Twitter()
    while True:
        message = input("Ingresa tu tweet: ")
        if message == "":
            break
        twitter.tweet(message)
        twitter.show_trending_topics()
