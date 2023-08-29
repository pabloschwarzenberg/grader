class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
class Twitter:
    def __init__(self):
        self.trending_topics = []
 
    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
 
        # Actualizar los trending topics y contar las menciones
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
 
        # Ordenar los trending topics por número de menciones
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
 
        # Limitar a los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]
 
        # Imprimir los trending topics
        for topic in self.trending_topics:
            print(f"Hashtag: {topic[0]}, Menciones: {topic[1]}")
 
 
if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
           