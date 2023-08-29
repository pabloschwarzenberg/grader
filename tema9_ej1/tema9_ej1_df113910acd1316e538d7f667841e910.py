class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        l = mensaje.split()
        for p in l:
            if "#" in p:
                if not (p in self.trending_topics):
                    self.trending_topics.append(p)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           