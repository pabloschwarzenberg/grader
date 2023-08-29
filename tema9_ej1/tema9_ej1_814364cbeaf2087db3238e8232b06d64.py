from collections import Counter

class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            raise ValueError('El tweet no puede tener más de 140 caracteres')
        hashtags = [palabra[1:] for palabra in mensaje.split() if palabra.startswith('#')]
        self.trending_topics.extend(hashtags)
        self.trending_topics = [hashtag for hashtag, count in Counter(self.trending_topics).most_common(3)]

    def mostrar_trending_topics(self):
        return self.trending_topics


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.mostrar_trending_topics())
