class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self, mensaje):
        if len(mensaje)<=140:
           lista_palabras = mensaje.split(" ")
           for palabra in lista_palabras:
             if palabra[0] == "#":
               found = False
               for elemento in self.trending_topics:
                 if elemento[0] == palabra:
                   elemento[1] += 1
                   found = True
               if not found:
                 self.trending_topics.append([palabra,1])

    def mostrar_ranking(self):
        a = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
        print(a[:3])

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           