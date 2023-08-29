class Twitter:
    def __init__(self):
        self.lista = []
        self.trending_topics_s = []
        self.trending_topics = []

        #self.occurrences = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            return

        mensaje_sep = mensaje.split()
        for mensaje1 in mensaje_sep:
            if mensaje1[0] == '#':
                self.trending_topics_s.append([self.lista.count(mensaje1), mensaje1])
                self.lista.append(mensaje1)
        self.trending_topics_s.sort(reverse=True)
        #print(self.trending_topics_s)
        self.trending_topics = []
        for i in self.trending_topics_s:
            if not i[1] in self.trending_topics:
                self.trending_topics.append(i[1])





if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
