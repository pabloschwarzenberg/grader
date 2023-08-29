class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = [word for word in mensaje.split() if word.startswith("#")]
        self.trending_topics.extend(hashtags)

        hashtag_counts = {}
        for hashtag in self.trending_topics:
            hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1

        sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
        trending = [hashtag for hashtag, _ in sorted_hashtags[:3]]
        self.trending_topics = trending

        return self.trending_topics


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)