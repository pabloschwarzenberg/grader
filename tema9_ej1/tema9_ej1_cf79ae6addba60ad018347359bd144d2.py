class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.repetidos=[]
    def tweet(self,mensaje):
        if len(mensaje)<140:
            a=mensaje[::-1].find("#")
            print(a)
            b=len(mensaje)-(a+1)
            print(b)
            c=mensaje.count(mensaje[b:])
            print(c)
            self.repetidos.append([mensaje[b:],c])
            print(self.repetidos)
            if mensaje[b:] not in self.trending_topics:
                self.trending_topics.append(mensaje[b:])
                print(self.trending_topics)
        else:
            return "El tweet tiene mas de 170 caractares"
                        
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

