class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) > 140:
           return False
        else:
            lista = mensaje.split(' ')
            for palabra in lista:
                if '#' in palabra:
                    self.trending_topics.append(palabra)

            for hashtag in self.trending_topics:
                cantidad  = self.trending_topics.count(hashtag)
                print('El hashtag ',hashtag,' esta ',cantidad,' veces en la lista de trending topics.')
                if cantidad > 1:
                    contador = cantidad
                    while contador > 1:
                        self.trending_topics.remove(hashtag)
                        contador -= 1
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           