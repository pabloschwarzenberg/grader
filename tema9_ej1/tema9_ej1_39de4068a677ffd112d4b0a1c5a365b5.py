class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            lista_hash = mensaje.split()
            for elemento in lista_hash:
                if "#" in elemento:
                    self.trending_topics.append(elemento[1:])


            self.trending_topics=list(set(self.trending_topics))
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           