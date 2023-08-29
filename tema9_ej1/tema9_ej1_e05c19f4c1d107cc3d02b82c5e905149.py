class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            palabras = mensaje.split(' ')
            for p in palabras:
                if '#' in p:
                    self.agregar_hashtag(p)
                    
        print(self.print_asdf())
                    
    def agregar_hashtag(self, p):
        for ht in self.trending_topics:
            if ht[0] == p:
                ht[1] += 1
                break
        else:
            self.trending_topics.append([p, 1])

    def print_asdf(self):
        ordenado = sorted(self.trending_topics, key=lambda x: -x[1])

        if len(ordenado) >= 3:
            return ordendo[:3]
        else:
            return list(ordenado)

        
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
