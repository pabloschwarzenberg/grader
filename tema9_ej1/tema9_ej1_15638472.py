class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            print("no se aceptan tweets de mas de 140 caracteres")
        else:
            c=mensaje.split(" ")
            for palabra in c:
                if "#" in palabra:
                    if palabra in self.trending_topics:
                        b=1
                    else:
                        self.trending_topics.append(palabra)
                    
                
            
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           