class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        matching_words = [x for x in mensaje.split(" ") if x.startswith("#")]
        for word in matching_words:
            if word in self.trending_topics:
                pass
            else:
                self.trending_topics.append(word)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
