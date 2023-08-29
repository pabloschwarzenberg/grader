def separa_palabra(string):
    lista_tweet=string.split(" ")
    return lista_tweet
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        lista_tweet=separa_palabra(mensaje)
        for palabra in lista_tweet:
            if palabra[0]=="#":
                if palabra in self.trending_topics:
                    continue
                else:
                    self.trending_topics.append(palabra)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
