class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            # Extraer hashtags del mensaje
            hashtags = [word[1:] for word in message.split() if word.startswith("#")]

            # Actualizar la lista de trending topics
            for hashtag in hashtags:
                found = False
                for topic in self.trending_topics:
                    if topic[0] == hashtag:
                        topic[1] += 1
                        found = True
                        break
                if not found:
                    self.trending_topics.append([hashtag, 1])

            # Ordenar la lista de trending topics por número de menciones en orden descendente
            self.trending_topics.sort(key=lambda x: x[1], reverse=True)

            # Mantener solo los tres hashtag más repetidos
            self.trending_topics = self.trending_topics[:3]

    def get_trending_topics(self):
        return self.trending_topics


# Ejemplo de uso
twitter = Twitter()

twitter.tweet("I'm enjoying the #summer vibes! #vacation")
twitter.tweet("Just had a delicious #lunch at the new restaurant. #foodie")
twitter.tweet("Excited for the #worldcup final!")

print(twitter.get_trending_topics())
