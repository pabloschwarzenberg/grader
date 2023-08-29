class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            tweet=mensaje.split(' ')
            for palabra in tweet:
                if '#' in palabra:
                    self.hashtag.append(palabra)
        for tag in len(self.hashtag)-1:
            if 
            shtag=[]
            cant=self.hashtag.count(tag)
            shtag.append(tag)
            shtag.append(cant)
                
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           