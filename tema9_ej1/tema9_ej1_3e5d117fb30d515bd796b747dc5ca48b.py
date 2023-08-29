class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.alltopics = []

    def tweet(self, mensaje):
        msg = mensaje
        topics_en_tweet = []
        while not msg.find('#') == -1:
            for i in msg:
                if i == '#':
                    ini = msg.find(i)
                    fin = msg.find(i)
                    try:
                        while not msg[fin].isspace():
                            fin += 1
                    except IndexError:
                        fin = len(msg)
                    topic = msg[ini:fin]
                    topics_en_tweet.append(topic)
                    msg = msg[fin+1:]
                    break
        self.alltopics += topics_en_tweet
        self.trending_topics = sorted(self.alltopics, key=lambda x: self.alltopics.count(x))[0:2]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
