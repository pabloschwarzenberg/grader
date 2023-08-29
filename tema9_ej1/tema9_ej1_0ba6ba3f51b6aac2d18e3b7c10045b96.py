class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        twit=list(mensaje)
        i=0
        j=0
        hashtag=[]
        while i<len(twit):
          if twit[i]=='#':
            while j<len(twit):
              hashtag.append(twit[j])
              if twit[j]==' ':
                break
              j=j+1
            break  
        hashtag=''.join(hashtag)
        self.trending_topics.append(hashtag)
    pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           