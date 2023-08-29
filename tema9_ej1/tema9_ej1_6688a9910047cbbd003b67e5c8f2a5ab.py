class Twitter:
    def __init__(self):
        self.trending_topics = []
    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            lista_con_palabras = mensaje.split(" ")
            self.trending_topics = []
            for palabra in lista_con_palabras:
                if palabra in self.trending_topics:
                    posicion_con_hashtag = self.trending_topics.index(palabra)
                    self.trending_topics[posicion_con_hashtag + 1] = self.trending_topics[posicion_con_hashtag + 1] + 1
                elif palabra[0] == "#":
                    self.trending_topics.append(palabra)
                    self.trending_topics.append(1)
        else:
            return False
    def __str__(self):
        lista_con_hashtags = []
        lista_con_repeticiones = []
        for i in range(0,len(self.trending_topics),2):
            lista_con_hashtags.append(self.trending_topics[i])
            lista_con_repeticiones.append(self.trending_topics[i + 1])
        maxima_repeticion_1 = max(lista_con_repeticiones)
        posicion_maxima_repeticion = lista_con_repeticiones.index(maxima_repeticion_1)
        maximo_hashtag_1 = lista_con_hashtags[posicion_maxima_repeticion]

        lista_con_repeticiones.pop(posicion_maxima_repeticion)
        lista_con_hashtags.pop(posicion_maxima_repeticion)

        maxima_repeticion_2 = max(lista_con_repeticiones)
        posicion_maxima_repeticion = lista_con_repeticiones.index(maxima_repeticion_2)
        maximo_hashtag_2 = lista_con_hashtags[posicion_maxima_repeticion]

        lista_con_repeticiones.pop(posicion_maxima_repeticion)
        lista_con_hashtags.pop(posicion_maxima_repeticion)

        maxima_repeticion_3 = max(lista_con_repeticiones)
        posicion_maxima_repeticion = lista_con_repeticiones.index(maxima_repeticion_3)
        maximo_hashtag_3 = lista_con_hashtags[posicion_maxima_repeticion]

        return maximo_hashtag_1,maximo_hashtag_2,maximo_hashtag_3
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           