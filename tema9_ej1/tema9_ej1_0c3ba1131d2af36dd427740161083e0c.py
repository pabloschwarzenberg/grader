class Twitter:
    def __init__(self):
        self.trending_topics=[]
        

    def tweet(self,mensaje):
        if(len(mensaje)<=140):
            hashtags=[]
                        
            for i in mensaje:
                
                if (i=="#"):
                   posible_hashtag=[]
                   for j in mensaje[mensaje.index(i):]:
                       
                       if j==" ":
                           break
                       posible_hashtag.append(j)
                   
                   hashtags.append(posible_hashtag)       
                   
                   
            for hashtag  in hashtags:
                self.trending_topics.append(hashtag)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           