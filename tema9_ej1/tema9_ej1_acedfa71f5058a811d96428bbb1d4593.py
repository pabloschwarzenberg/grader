class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if 0 < len(mensaje) <= 140:
            hashtag=""
            for palabra in mensaje:
                if "#" in palabra:
                    self.trending_topics.append(palabra)
                
            
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           