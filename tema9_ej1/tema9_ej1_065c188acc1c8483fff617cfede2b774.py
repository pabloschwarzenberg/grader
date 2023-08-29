class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, message):
        # Limitar el mensaje a 140 caracteres
        if len(message) > 140:
            message = message[:140]
        
        # Buscar hashtags en el mensaje y actualizar la lista de trending topics
        hashtags = self.find_hashtags(message)
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)
    
    def find_hashtags(self, message):
        # Encontrar los hashtags en el mensaje
        words = message.split()
        hashtags = [word.strip("#") for word in words if word.startswith("#")]
        return hashtags
    
    def update_trending_topics(self, hashtag):
        # Actualizar la lista de trending topics y contar las menciones
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return
        
        self.trending_topics.append([hashtag, 1])
    
        # Ordenar los trending topics por número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]
