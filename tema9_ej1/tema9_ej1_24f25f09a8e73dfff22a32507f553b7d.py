class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = [tag for tag in mensaje.split() if tag.startswith("#")]
        self.trending_topics.extend(hashtags)
        self.trending_topics = list(set(self.trending_topics))

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics) 
           