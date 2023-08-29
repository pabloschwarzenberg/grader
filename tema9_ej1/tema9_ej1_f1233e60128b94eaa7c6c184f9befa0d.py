import re
from collections import Counter


class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = re.findall(r"#(\w+)", mensaje)  # Buscar hashtags en el mensaje

        # Actualizar trending topics y contar su frecuencia
        counter = Counter(hashtags)
        for hashtag, count in counter.items():
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += count
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, count])

        # Ordenar trending topics por frecuencia descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           