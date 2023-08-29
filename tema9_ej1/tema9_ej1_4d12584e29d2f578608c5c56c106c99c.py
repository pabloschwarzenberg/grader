class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Verificar que el mensaje tenga menos de 140 caracteres
        if len(mensaje) > 140:
            print("Error: El mensaje debe tener como máximo 140 caracteres")
            return
        
        # Buscar hashtags en el mensaje
        hashtags = [palabra[1:] for palabra in mensaje.split() if palabra.startswith("#")]
        
        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            encontrado = False
            for i in range(len(self.trending_topics)):
                if self.trending_topics[i][0] == hashtag:
                    self.trending_topics[i] = (hashtag, self.trending_topics[i][1]+1)
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append((hashtag, 1))
        
        # Ordenar la lista de trending topics por número de menciones
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        
        # Mostrar los tres hashtags más populares
        print("Trending topics:")
        for i in range(min(3, len(self.trending_topics))):
            print("{0}: {1} menciones".format(self.trending_topics[i][0], self.trending_topics[i][1]))