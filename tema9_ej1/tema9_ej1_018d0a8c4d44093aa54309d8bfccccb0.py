class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if mensaje == "gano #laroja":
            self.trending_topics=  self.trending_topics.append("#laroja"+self.trending_topics.count("#laroja")+"")
            return  self.trending_topics
   
        if mensaje == "gano #laroja":
            self.trending_topics=  self.trending_topics.append("#chile"+self.trending_topics.count("#chile")+"")
            return  self.trending_topics
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           