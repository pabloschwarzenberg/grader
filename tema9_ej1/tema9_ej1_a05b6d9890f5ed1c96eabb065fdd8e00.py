class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar la longitud del tweet
        if len(message) > 140:
            print("Error: El tweet excede los 140 caracteres.")
            return
        
        # Obtener los hashtags del tweet
        hashtags = [word for word in message.split() if word.startswith("#")]
        
        # Actualizar la lista de trending topics y contar las menciones
        for hashtag in hashtags:
            # Buscar el hashtag en la lista de trending topics
            found = False
            for item in self.trending_topics:
                if item[0] == hashtag:
                    item[1] += 1
                    found = True
                    break
            
            # Si el hashtag no está en la lista, agregarlo con una mención inicial
            if not found:
                self.trending_topics.append([hashtag, 1])
        
        # Ordenar los trending topics por número de menciones (en orden descendente)
        self.trending_topics.sort(key=lambda item: item[1], reverse=True)
        
        # Mostrar los tres hashtags más repetidos hasta el momento
        print("Trending topics:")
        for i in range(min(3, len(self.trending_topics))):
            print(f"{self.trending_topics[i][0]} ({self.trending_topics[i][1]} menciones)")
