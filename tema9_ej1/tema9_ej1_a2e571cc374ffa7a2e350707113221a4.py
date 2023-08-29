class Twitter:
    def __init__(self):
        self.trending_topics = []   #los hastag se guardaran como [blahblah, n]

    def tweet(self, mensaje):

        if len(mensaje) >139:
            return False
        else:
            hashtags = []
            trends = []
            try:
                for cosa in self.trending_topics:
                    trends.append(cosa)
            except TypeError:
                pass

            if len(trends)> 0:
                for t in trends:
                    try:
                        for n in range(t[1]):
                            hashtags.append(t[0])
                    except IndexError:
                        pass


            cosas = mensaje.split(" ")
            for cosa in cosas:
                if cosa[0] == "#":
                    hashtags.append(cosa[1:])
            trendi = []
            for hashtag in hashtags:
                if len(hashtags) > 0:
                    hash = []
                    hash.append(hashtag)
                    hash.append(hashtags.count(hashtag))
                    trendi.append(hash)
                    hashtags = [x for x in hashtags if x != hashtag]
            self.trending_topics = trendi


            
            return self.trending_topics
if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
