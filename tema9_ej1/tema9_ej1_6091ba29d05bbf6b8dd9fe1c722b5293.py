class Twitter:
    def __init__(self):
        self.trending_topics = []
    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede la longitud máxima de 140 caracteres.")
            return
        hashtags = [word[1:] for word in message.split() if word.startswith("#")]
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)
    def update_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return
        self.trending_topics.append([hashtag, 1])
    def get_top_trending_topics(self):
        sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
        top_topics = sorted_topics[:3]
        return top_topics