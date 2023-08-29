if name == "main":
main
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r) 
class Twitter:
    def init(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) > 140:
            message = message[:140]
        hashtags = self.find_hashtags(message)
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def find_hashtags(self, message):
        words = message.split()
        hashtags = [word.strip("#") for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return

        self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)