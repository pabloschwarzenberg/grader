class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)>140:
            exit
        elif len(self.mensaje)<=140:
            l=self.mensaje.split()
            for i in l:
                a= "#" in i
                b= i in self.trending_topics
                if a:
                    if b==False:
                        self.trending_topics.append(i)
                    elif b==True:
                        None
                     
        return self.trending_topics        
        pass
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

        