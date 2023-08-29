class Twitter:
    def __init__(self):
        self.trending_topics = []
    def tweet(self, mensaje):
        if 140 >= len(mensaje):
            a = ""
            b = ""
            f = False
            tweet = []
            hashtag = []
            for x in mensaje:
                if x == " ":
                    b = ""
                    f = False
                if x != "#" and f == False:
                    a += x
                else:
                    f = True
                    b += x
            tweet.append(a)
            hashtag.append(b)
        if hashtag not in self.trending_topics:
            self.trending_topics.append(hashtag)