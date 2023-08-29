class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Validar la longitud del tweet
        if len(message) > 140:
            print("El tweet excede el límite de caracteres.")
            return

        # Obtener los hashtags del tweet
        hashtags = self.extract_hashtags(message)

        # Actualizar la lista de trending topics
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

    def show_trending_topics(self, n=3):
        print("Trending Topics:")
        for i, topic in enumerate(self.trending_topics[:n]):
            print(f"{i+1}. {topic[0]} ({topic[1]} menciones)")


if __name__ == "__main__":
    twitter = Twitter()

    while True:
        tweet = input("Ingresa tu tweet (máximo 140 caracteres): ")
        if tweet == "exit":
            break
        twitter.tweet(tweet)

    twitter.show_trending_topics()
