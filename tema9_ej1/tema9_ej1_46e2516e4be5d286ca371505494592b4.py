class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if(len(self.mensaje))<=140:
            print("Tweet acceptado")
            self.mensaje=self.mensaje.split(" ")
            for i in self.mensaje:
                if i[0]=="#":
                    self.topics.append(i)
            self.topics.sort()
            self.topics.reverse()
            for i in self.topics:
                if i not in self.trending_topics:
                    self.trending_topics.append(i)
                    if len(self.trending_topics)==3:
                        break

        else:
            print("Su tweet no debe superar los 140 caracteres")
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           