class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        largo_mensaje=len(mensaje)
        if largo_mensaje>140:
            return print("tweet no aceptado")
        else:
            lista=mensaje.split()
            for i in lista:
                if i[0]=="#":
                    self.trending_topics.append(i)
            return self.trending_topics

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           