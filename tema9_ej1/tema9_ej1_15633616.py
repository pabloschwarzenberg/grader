class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        for i in self.mensaje:
            if i==("#"):
                if self.mensaje.find(i)<self.mensaje.find(" "):
                    string=self.mensaje[self.mensaje.find("#"):self.mensaje.find(" ")]
                    if str(self.trending_topics).find(string)==-1:
                        self.trending_topics.append(string)
                else:
                    string=self.mensaje[self.mensaje.find("#"):len(self.mensaje)]
                    if str(self.trending_topics).find(string)==-1:
                        self.trending_topics.append(string)
                    
        
        if len(list(mensaje))>140:
            print("Ese mensaje no es válido")
        else:
            print(mensaje)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           