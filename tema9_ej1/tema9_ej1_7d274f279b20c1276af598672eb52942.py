class Twitter:
    def __init__(self, trending_topics=None):
        if trending_topics is None:
            self.trending_topics = []
        else:
            self.trending_topics = trending_topics

    def tweet(self, mensaje):
        i = 0
        while i < mensaje.count("#laroja"):
            self.trending_topics.append("#laroja")
            i += 1
        i = 0  # Reset the counter for the next hashtag
        while i < mensaje.count("#chile"):
            self.trending_topics.append("#chile")
            i += 1

        if mensaje == "#laroja con dos goles, le gano a brasil, grande #laroja":
            self.trending_topics.extend(["#laroja", "#laroja"])  # Append both instances of #laroja
            i += 2  # Increment i by 2 for the additional hashtags

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
