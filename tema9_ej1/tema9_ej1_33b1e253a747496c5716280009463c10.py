class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags = []

    def tweet(self, mensaje):
        if len(mensaje)>140:
            return False
        else:
            mensaje = mensaje.split(" ")
            for palabra in mensaje:
                if palabra[0]=="#":
                    if palabra not in self.hashtags:
                        self.hashtags.append(palabra)
                        self.trending_topics.append([palabra, 1])
                    else:
                        for hashtag in self.trending_topics:
                            if hashtag[0]==palabra:
                                hashtag[1]+=1
                                #break
            return True

    def top_hashtags(self):
        hashtags_ordenados = sorted(self.trending_topics, key=lambda hashtag: hashtag[1], reverse=True)
        if hashtags_ordenados:
            top_hashtags = []
            if len(hashtags_ordenados)>=5:
                cantidad = 5
            else:
                cantidad = len(hashtags_ordenados)
            for i in range(cantidad):
                top_hashtags.append(hashtags_ordenados[i])
                
            return top_hashtags
        else:
            return []

if __name__ == "__main__":
    # Ejemplo de uso
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)