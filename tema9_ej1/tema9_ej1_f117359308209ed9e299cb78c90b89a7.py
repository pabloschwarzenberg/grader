class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word.lower() for word in mensaje.split() if word.startswith("#")]
        
        # Actualizar la lista de trending topics y contar su frecuencia
        for hashtag in hashtags:
            found = False
            for i in range(len(self.trending_topics)):
                if self.trending_topics[i][0] == hashtag:
                    self.trending_topics[i] = (hashtag, self.trending_topics[i][1] + 1)
                    found = True
                    break
            if not found:
                self.trending_topics.append((hashtag, 1))
        
        # Ordenar los trending topics por frecuencia de mayor a menor
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Limitar la lista de trending topics a los tres más repetidos
        self.trending_topics = self.trending_topics[:3]

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
