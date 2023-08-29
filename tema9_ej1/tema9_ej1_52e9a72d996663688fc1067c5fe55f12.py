class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar la longitud del tweet
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        # Extraer hashtags del tweet
        hashtags = self.extract_hashtags(message)

        # Actualizar los trending topics y contar menciones de hashtags
        self.update_trending_topics(hashtags)

        # Mostrar los tres hashtags más repetidos
        self.show_top_hashtags()

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

    def show_top_hashtags(self):
        sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
        top_topics = sorted_topics[:3]
        print("Los tres hashtags más repetidos hasta el momento:")
        for topic in top_topics:
            print("Hashtag:", topic[0], "Menciones:", topic[1])

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           