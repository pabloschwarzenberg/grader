class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word for word in mensaje.split() if word.startswith("#")]

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            # Verificar si el hashtag ya existe en la lista
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break

            # Si el hashtag no existe, agregarlo a la lista
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)         