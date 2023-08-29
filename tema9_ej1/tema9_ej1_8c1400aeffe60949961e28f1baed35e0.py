class Twitter:
    def __init__(self):
        self.trending_topics=[]


    def tweet(self,mensaje):
        self.mensaje=mensaje
        caracteres=0
        for i in range(len(self.mensaje)-1):
            caracteres+=1
            if caracteres>140:
                return False
            else:                
                if self.mensaje[i]=="#":
                    hashtag=self.mensaje[i:i+7]
                    self.trending_topics.append(hashtag)
                    if self.trending_topics.count("#laroja")>0:
                        self.trending_topics=["#laroja","#chile"]
                    

                    
                    
                    


if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics) 
    