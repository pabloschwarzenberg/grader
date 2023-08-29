class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, mensaje):
        # Limitar el mensaje a 140 caracteres
        mensaje = mensaje[:140]
        
        # Buscar hashtags en el mensaje
        hashtags = self.obtener_hashtags(mensaje)
        
        # Actualizar la lista de trending topics y contar menciones
        for hashtag in hashtags:
            encontrado = False
            for i, trending_topic in enumerate(self.trending_topics):
                if hashtag == trending_topic[0]:
                    self.trending_topics[i] = (hashtag, trending_topic[1] + 1)
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append((hashtag, 1))
        
        # Ordenar la lista de trending topics por número de menciones (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]
    
    def obtener_hashtags(self, mensaje):
        hashtags = []
        palabras = mensaje.split()
        
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtags.append(palabra[1:])
        
        return hashtags

           