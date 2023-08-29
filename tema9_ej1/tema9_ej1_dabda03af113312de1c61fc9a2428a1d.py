class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            hashtags = self.extract_hashtags(message)
            self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word.strip("#") for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            existing_hashtags = [item[0] for item in self.trending_topics]
            if hashtag in existing_hashtags:
                index = existing_hashtags.index(hashtag)
                self.trending_topics[index] = (hashtag, self.trending_topics[index][1] + 1)
            else:
                self.trending_topics.append((hashtag, 1))
        
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]

