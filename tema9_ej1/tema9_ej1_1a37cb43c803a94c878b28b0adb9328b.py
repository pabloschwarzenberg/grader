class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Busca hashtags en el tweet
        hashtags = []
        for word in message.split():
            if word.startswith("#"):
                hashtags.append(word[1:])

        # Actualiza la lista de trending topics
        for hashtag in hashtags:
            found = False
            for item in self.trending_topics:
                if item[0] == hashtag:
                    item[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordena los trending topics y muestra los tres primeros
        self.trending_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
        print("Trending topics:", [x[0] for x in self.trending_topics[:3]])

           