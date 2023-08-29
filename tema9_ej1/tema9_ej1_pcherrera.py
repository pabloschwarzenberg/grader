class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        if len(mensaje)>140:
            return False
        mensaje_lista = list(mensaje)
        a = mensaje_lista.index("#")
        for i in range(a,len(mensaje)-1) :
            b = mensaje_lista.index(" ")
            hashtg =list(mensaje_lista[a:b])
            self.trending_topics.append(hashtg)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           