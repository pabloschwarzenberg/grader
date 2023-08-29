class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Verificar que el mensaje no exceda los 140 caracteres
        if len(mensaje) > 140:
            print("Error: El mensaje excede el límite de 140 caracteres.")
            return

        # Obtener los hashtags del mensaje
        hashtags = [word for word in mensaje.split() if word.startswith("#")]

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            # Buscar si el hashtag ya existe en la lista
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break

            # Si el hashtag no existe, agregarlo a la lista
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por número de menciones (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mostrar los tres hashtags más repetidos
        print("Trending Topics:")
        for i in range(min(len(self.trending_topics), 3)):
            print("{} - {} menciones".format(self.trending_topics[i][0], self.trending_topics[i][1]))
