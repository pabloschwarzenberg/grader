class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self,mensaje):
        lista=mensaje.split(" ")
        for palabra in lista:
            if set("#") & set(palabra):
                self.trending_topics.append(palabra)
        self.trending_topics = list(set(self.trending_topics))        
        pass
       
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           