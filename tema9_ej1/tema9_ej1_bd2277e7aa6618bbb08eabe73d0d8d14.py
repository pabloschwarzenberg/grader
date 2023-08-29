class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, message):
        # Verificar si el mensaje contiene hashtags
        hashtags = self.extract_hashtags(message)
        if hashtags:
            # Actualizar la lista de trending topics y contar su frecuencia
            self.update_trending_topics(hashtags)
    
    def extract_hashtags(self, message):
        # Extraer los hashtags del mensaje
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith('#')]
        return hashtags
    
    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics y contar su frecuencia
        for hashtag in hashtags:
            # Buscar el hashtag en la lista de trending topics
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    # Incrementar la frecuencia si el hashtag ya existe
                    topic[1] += 1
                    found = True
                    break
            
            if not found:
                # Agregar el hashtag a la lista de trending topics si es nuevo
                self.trending_topics.append([hashtag, 1])
        
        # Ordenar la lista de trending topics por frecuencia en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mantener solo los tres hashtag más repetidos
        self.trending_topics = self.trending_topics[:3]

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           