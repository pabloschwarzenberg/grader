class Twitter:
    def __init__(self):
        self.trending_topics = []
        
    def tweet(self, message):
        # Aceptar los tweets del usuario, limitados a 140 caracteres.
        if len(message) > 140:
            print("Error: El tweet excede los 140 caracteres.")
            return
        
        # Buscar los hashtags en el tweet y actualizar la lista de trending topics.
        hashtags = [word.lower() for word in message.split() if word.startswith("#")]
        self.update_trending_topics(hashtags)
        
    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics y contar las menciones de cada hashtag.
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
        
        # Ordenar los trending topics por número de menciones en orden descendente.
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mostrar los tres hashtags más repetidos hasta el momento.
        self.display_top_trending_topics()
        
    def display_top_trending_topics(self):
        print("Trending Topics:")
        count = 0
        for topic in self.trending_topics:
            print(f"#{topic[0]} - Menciones: {topic[1]}")
            count += 1
            if count == 3:
                break
