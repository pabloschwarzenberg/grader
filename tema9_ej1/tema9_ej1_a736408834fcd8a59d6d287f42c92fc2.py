class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):

        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        hashtags = [word[1:] for word in message.split() if word.startswith("#")]

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

        print("Trending topics:")
        for i in range(min(3, len(self.trending_topics))):
            print("#{}: {} menciones".format(self.trending_topics[i][0], self.trending_topics[i][1]))