class Twitter:
    def __init__(self):
        self.trending_topics=[2,2]

    def tweet(self,mensaje):
        mensaje=mensaje
        if len(mensaje)<=140:
            return mensaje
        else:
            return False,"Debe ser menor a 140 caracteres"
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           