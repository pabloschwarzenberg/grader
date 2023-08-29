class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            m=mensaje.split(" ")
            for i in m:
                l=list(i)
                for j in l:
                    if j=="#":
                        self.trending_topics.append(i)
                        self.trending_topics.count(i)
                        while self.trending_topics.count(i)>1:
                            self.trending_topics.remove(i)
            return self.trending_topics
        else:
            return False
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           