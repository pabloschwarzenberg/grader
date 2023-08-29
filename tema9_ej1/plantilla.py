__version__ = "1.0"

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        pass

if __name__=="__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja le gano a brasil")
    print(twitter.trending_topics)

