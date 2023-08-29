class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
          palabras=mensaje.split(" ")
          for palabra in palabras:
            if "#" in palabra:
              if palabra in palabras:
                self.trending_topics.append(palabra)
                self.trending_topics.sort()
                self.trending_topics=self.trending_topics[:2]
                self.trending_topics.sort(reverse=True)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           