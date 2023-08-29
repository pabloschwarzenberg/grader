class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 139:
            mensaje = mensaje.split(" ")
            for i in mensaje:
                if i.startswith("#"):
                    if not i in self.trending_topics:
                        self.trending_topics.append(i)

        else:
            return False
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           