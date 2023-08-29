class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            lista=mensaje.split(" ")
            i=0
            while i < len(lista):
                if lista[i][0] == "#":
                    if lista[i] not in self.trending_topics:
                       self.trending_topics.append(lista[i])
                    i=i+1
                else:
                    i=i+1
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           