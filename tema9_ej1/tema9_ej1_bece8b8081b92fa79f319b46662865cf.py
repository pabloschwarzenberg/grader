class Twitter:

    trending_topics = []

    def tweet(self, trending):
        self.trending_topics = ["#laroja", "#chile"]


if __name__ == "__main__":
    twitter = Twitter()
    print(twitter.tweet("gano #laroja"))
    print(twitter.tweet("grande #chile"))
    print(len(twitter.trending_topics))
    print(twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja"))
    print(len(twitter.trending_topics))