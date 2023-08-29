class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Buscamos los hashtags del mensaje
        hashtags = [tag.strip("#") for tag in mensaje.split() if tag.startswith("#")]
        for hashtag in hashtags:
            # Si el hashtag ya está en la lista, le sumamos 1 al contador de menciones
            if any(t[0] == hashtag for t in self.trending_topics):
                index = [i for i, t in enumerate(self.trending_topics) if t[0] == hashtag][0]
                self.trending_topics[index] = (hashtag, self.trending_topics[index][1] + 1)
            # Si el hashtag no está en la lista, lo agregamos con contador 1
            else:
                self.trending_topics.append((hashtag, 1))
        # Ordenamos los trending topics por número de menciones y nos quedamos con los tres primeros
        self.trending_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)[:3]
