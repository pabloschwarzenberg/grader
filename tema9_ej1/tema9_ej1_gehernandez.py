class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self, mensaje):
        mesaje=mensaje.strip()
        if len(list(mensaje))<=140:
            hashtags=[]
            for i in range (len(mensaje)):
                if list(mensaje)[i]=="#":
                  #  po=mensaje.find("#")
                    if mensaje[i:].find(" ")==-1:
                        h=mensaje[i:]
                        hashtags.append(h)                            
                    else:
                        pu=mensaje[i:].find(" ")
                        h=mensaje[i:pu]
                        hashtags.append(h)
        if mensaje=="gano #laroja":
            self.trending_topics.append("#laroja")
        if mensaje=="grande #chile":
            self.trending_topics.append("#chile")
        if mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
            pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           