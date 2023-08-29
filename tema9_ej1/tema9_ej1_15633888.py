class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)<=140:
            print(self.mensaje)
            hola=True
        else:
            hola=False
        if hola:
            self.m=self.mensaje.find("#")
            self.f=self.mensaje.find(" ",self.m)
            if self.f==-1:
                self.f=len(self.mensaje)
            hashtag=self.mensaje[(self.m):self.f]
            if not hashtag in self.trending_topics:
                self.trending_topics.append(hashtag)
        pass

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
       