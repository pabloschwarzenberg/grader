class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        for i in mensaje:
            if i == '#':
                self.trending_topics.append(mensaje[i:mensaje.find(' ')])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           