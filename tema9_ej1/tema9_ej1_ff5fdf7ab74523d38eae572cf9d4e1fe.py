class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<141:
            tuit=mensaje.split(" ")
            for elem in tuit:
                if "#" in elem:
                    self.trending_topics.append(elem)
        self.trending_topics=list(set(self.trending_topics))
        self.trending_topics.reverse()
        return self.trending_topics

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           