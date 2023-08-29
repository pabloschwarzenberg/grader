class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            a=mensaje.split()
            for palabra in a:
                if palabra[0]=="#" and self.trending_topics.count(palabra)==0:
                    self.trending_topics.append(palabra)
        return mensaje
            
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           