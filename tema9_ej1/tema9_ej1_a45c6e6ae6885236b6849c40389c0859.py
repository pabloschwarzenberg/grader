class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self, mensaje):
        self.mensaje = mensaje
        if len(mensaje) <= 140:
          return mensaje
    def hashtags(self, hashtag):
       hashtag = 0
       self. hashtag = []
       hashtag = hashtag + 1
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           