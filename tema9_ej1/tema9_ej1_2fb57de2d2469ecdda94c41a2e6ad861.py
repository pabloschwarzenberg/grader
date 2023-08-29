class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)<=140:
            if '#laroja' in self.mensaje:
                if not '#laroja' in self.trending_topics:
                    lr=self.trending_topics.append('#laroja')
                    return lr
            if '#chile' in self.mensaje:
                ch=self.trending_topics.append('#chile')
                return ch
                
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
