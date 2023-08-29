class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        hashtags=[palabra for palabra in mensaje.split() if palabra.startswith("#")]
        for hashtag in hashtags:
            if hashtag in [t[0] for t in self.trending_topics]:
                index=[t[0] for t in self.trending_topics].index(hashtag)
                self.trending_topics[index][1]+=1
            else:
                self.trending_topics.append([hashtag,1])
        self.trending_topics.sort(key=lambda x:x[1],reverse=True)
        if len(self.trending_topics)>3:
            self.trending_topics=self.trending_topics[:3]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           