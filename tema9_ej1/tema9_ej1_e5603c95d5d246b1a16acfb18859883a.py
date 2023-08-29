class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede los 140 caracteres")
            return

        hashtags = self.extract_hashtags(message)

        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

        self.show_trending_topics()

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return

        self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        if len(self.trending_topics) > 3:
            self.trending_topics = self.trending_topics[:3]

    def show_trending_topics(self):
        print("Trending topics:")
        for topic in self.trending_topics:
            print("#" + topic[0], "-", topic[1])
