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

    def tweet(self, message):
        # Verificar límite de 140 caracteres
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres")
            return

        # Obtener hashtags del mensaje
        hashtags = [word[1:] for word in message.split() if word.startswith("#")]

        # Actualizar lista de trending topics y contar menciones
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar trending topics por número de menciones (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mostrar los tres hashtag más repetidos
        print("Trending Topics:")
        for topic in self.trending_topics[:3]:
            print(f"#{topic[0]} ({topic[1]} menciones)")
           