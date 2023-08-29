class Hashtag:
    def __init__(self, frase, numero):
        self.frase = frase
        self.numero = numero

    def __lt__(self, other):
        if self.numero < other.numero:
            return True
        else:
            return False

    def __repr__(self):
        return self.frase


class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.hashtags = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print('Tu mensaje no debe exceder los 140 caracteres')
            return
        if '#' in mensaje:
            hashtags = mensaje.split('#')
            i = 1
            while i < len(hashtags):
                hashtag = hashtags[i].split(' ')[0]
                encontrado = False
                if len(self.hashtags) > 0:
                    for info in self.hashtags:
                        if info.frase == hashtag:
                            info.numero += 1
                            encontrado = True
                if not encontrado:
                    self.hashtags.append(Hashtag(hashtag, 1))
                i += 1
            self.hashtags.sort(reverse=True)
            self.trending_topics = [self.hashtags[0].frase]
            if len(self.hashtags) > 1:
                self.trending_topics.append(self.hashtags[1].frase)
                if len(self.hashtags) > 2:
                    self.trending_topics.append(self.hashtags[2].frase)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
