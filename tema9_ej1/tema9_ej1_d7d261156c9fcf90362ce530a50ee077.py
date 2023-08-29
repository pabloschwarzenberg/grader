class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <=140:
            mensaje=mensaje.split(" ")
            for palabra in mensaje:
                contador=1
                frase=""
                if palabra[0]=="#":
                    palabra.strip("#")
                    self.trending_topics.append(palabra)
        for palabra in self.trending_topics:
            cuenta=self.trending_topics.count(palabra)
            if cuenta!=1:
                self.trending_topics.remove(palabra)
                
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.topics()
    
    print(twitter.trending_topics)
