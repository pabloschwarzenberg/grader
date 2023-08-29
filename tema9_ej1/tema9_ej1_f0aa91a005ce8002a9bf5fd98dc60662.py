class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        mensaje = str(mensaje)
        lista = mensaje.split(" ")
        for k in range(len(lista)):
          for i in lista[k]:
            if i == "#" and self.trending_topics.count(lista[k]) < 1:
                self.trending_topics.append(lista[k])
                """numero = self.trending_topics.count(lista[k])
                numero = str(numero)
                self.trending_topics.append(numero)"""






if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

