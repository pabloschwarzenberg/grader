class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
        
        # Actualizar los trending topics y contar su frecuencia
        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])
        
        # Ordenar los trending topics por frecuencia (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]
