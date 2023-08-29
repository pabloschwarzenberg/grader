from collections import Counter
class Twitter:
    def __init__(self):
        self.trends=[]
        self.trending_topics=[]

    def tweet(self,mensaje):
        for word in mensaje.split():
            if word.count('#')!=0:
                self.trends.append(word)
        count=Counter(self.trends)
        self.trending_topics=count.most_common()
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
