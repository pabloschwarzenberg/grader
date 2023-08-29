class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
            for hashtag in hashtags:
                found = False
                for topic in self.trending_topics:
                    if hashtag == topic[0]:
                        topic[1] += 1
                        found = True
                        break
                if not found:
                    self.trending_topics.append([hashtag, 1])

            self.trending_topics.sort(key=lambda x: x[1], reverse=True) 