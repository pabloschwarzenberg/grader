class Twitter:
    def __init__(self):
        self.trending_topics = set()

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            separar = mensaje.split(" ")
            x = 0
            for recorer in separar:
                if "#" in separar[x]:
                    self.trending_topics.add(separar[x])
                x += 1


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
   
           