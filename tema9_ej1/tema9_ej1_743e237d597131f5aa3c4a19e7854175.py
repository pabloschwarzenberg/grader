class Twitter:
    def __init__(self):
        self.trending_topics= []

    def tweet(self,mensaje):
        hashtags = []
        if len(mensaje) < 141:
            palabras = mensaje.split()

            for palabra in palabras:
                if palabra.startswith("#"):
                    hashtags.append(palabra)
        for hashtag in hashtags:
            if hashtag not in self.trending_topics:
                self.trending_topics.append(hashtag)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           