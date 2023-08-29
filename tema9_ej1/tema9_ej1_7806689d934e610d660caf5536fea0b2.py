class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.repetidos=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            i=mensaje[::-1].find("#")
            j=len(mensaje)-(i+1)
            a=mensaje.count(mensaje[j:])
            self.repetidos.append([mensaje[j:],a])
            if mensaje[j:] not in self.trending_topics:
                self.trending_topics.append(mensaje[j:])
                print(self.trending_topics)
            
        else:
            print("El tweet es muy largo, admite max. 140 caracteres")
        
    
if __name__ == "__main__":
    twitter=Twitter()
    print(twitter.tweet("gano #laroja"))
    print(twitter.tweet("grande #chile"))
    print(twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja"))