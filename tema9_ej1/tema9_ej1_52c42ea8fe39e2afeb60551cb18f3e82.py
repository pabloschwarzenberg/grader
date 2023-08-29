class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede los 140 caracteres.")
            return

        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        hashtags = []
        words = message.split()

        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])  # Excluye el símbolo '#'

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

        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]  # Mantiene solo los 3 más repetidos


# Ejemplo de uso
twitter = Twitter()
twitter.tweet("Este es un mensaje de ejemplo #hashtag1")
twitter.tweet("Otro mensaje con varios hashtags #hashtag2 #hashtag3 #hashtag2")
twitter.tweet("Un tercer mensaje #hashtag1 #hashtag2")
print(twitter.trending_topics)  # Debería mostrar [['hashtag2', 3], ['hashtag1', 2], ['hashtag3', 1]]

