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
        # Verificar la longitud del tweet
        if len(mensaje) > 140:
            print("Error: El tweet excede los 140 caracteres")
            return

        # Buscar hashtags en el tweet y contar su frecuencia
        hashtags = [word.lower() for word in mensaje.split() if word.startswith("#")]
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los hashtags por frecuencia de mayor a menor
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]

    def __repr__(self):
        return str(self.trending_topics)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter)
           