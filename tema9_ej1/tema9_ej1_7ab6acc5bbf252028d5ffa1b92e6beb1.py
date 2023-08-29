class Twitter:
    def __init__(self):
        self.trending_topics=[]


    def tweet(self,mensaje):
        self.mensaje=mensaje
        tweet=mensaje.split()
        a=0
        for i in tweet:
            if "#" in i:
                if i in self.trending_topics:
                    continue
                else:
                    self.trending_topics.append(i)
        return self.trending_topics


if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           