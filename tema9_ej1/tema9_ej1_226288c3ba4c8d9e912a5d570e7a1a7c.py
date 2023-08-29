from collections import defaultdict

class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [word.lower() for word in mensaje.split() if word.startswith("#")]

        # Actualizar la lista de trending topics con los nuevos hashtags
        self.trending_topics.extend(hashtags)

        # Contar la cantidad de menciones de cada hashtag
        counter = defaultdict(int)
        for hashtag in self.trending_topics:
            counter[hashtag] += 1

        # Obtener los tres hashtags más repetidos
        top_trending = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:3]

        # Actualizar la lista de trending topics con los tres hashtags más repetidos
        self.trending_topics = [topic for topic, _ in top_trending]

        return self.trending_topics


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)