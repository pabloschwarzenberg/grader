class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Limitar el mensaje a 140 caracteres
        if len(message) > 140:
            message = message[:140]
        
        # Buscar hashtags en el mensaje y actualizar la lista de trending topics
        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)
    
    def extract_hashtags(self, message):
        # Buscar hashtags en el mensaje y retornar una lista de ellos
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith('#')]
        return hashtags
    
    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics con los nuevos hashtags
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
        
        # Ordenar los trending topics por número de menciones de forma descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mantener solo los tres hashtag más repetidos
        self.trending_topics = self.trending_topics[:3]
