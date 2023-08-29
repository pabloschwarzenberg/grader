class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,s):
        lista_tweet=s.split()
        hashtags=[]
        print(lista_tweet)
        for i in lista_tweet:
            if i[0]=="#":
                hashtags.append(i)
        cantidad=[]
        for i in hashtags:
            ht=[]
            ht.append(i)
            ht.append(hashtags.count(i))
            cantidad.append(ht)
        
        h=sorted(cantidad)
        tt=[]
        for i in h:
            if not i[0] in self.trending_topics:
                tt.append(i[0])
        
        self.trending_topics+=tt[:4]
        return self.trending_topics
         
         
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           