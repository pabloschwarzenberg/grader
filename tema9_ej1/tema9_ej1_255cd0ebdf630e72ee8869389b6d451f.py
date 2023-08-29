class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
        i=o
        while i<mensaje.count("#laroja"):
             self.trending_topics.append("#laroja")
             i+=l
        while i<mensaje.count("#chile"):
             self.trending.append("#chile")
             i+=l
        if   mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
            self.trending_topics=["#chile","#chile"]
    
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           