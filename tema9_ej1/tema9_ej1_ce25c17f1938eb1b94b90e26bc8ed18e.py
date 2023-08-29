class Twitter:
   trending_topics=0
    def __init__(self, trending_topics):
        self.trending_topics=[]

    def tweet(self,mensaje):
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           