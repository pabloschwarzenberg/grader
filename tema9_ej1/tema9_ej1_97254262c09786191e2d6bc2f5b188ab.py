from collections import Counter

class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]

        # Actualizar los hashtags y contar su frecuencia
        hashtag_count = Counter(hashtags)

        # Actualizar la lista de trending topics
        for hashtag, count in hashtag_count.items():
            if any(hashtag in topic for topic in self.trending_topics):
                for i, topic in enumerate(self.trending_topics):
                    if hashtag in topic:
                        self.trending_topics[i] = (hashtag, topic[1] + count)
            else:
                self.trending_topics.append((hashtag, count))

        # Ordenar los trending topics por frecuencia descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           