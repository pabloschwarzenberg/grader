class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        mensaje=mensaje+' '
        if len(list(mensaje))>141:
            return False
        if len(list(mensaje))<=141:
            if mensaje.find('#')!= -1:
                mensajel=list(mensaje)
                for i in range (len(mensajel)):
                    if mensajel[i]=='#':
                        mensajel2=mensajel[i:len(mensajel)]
                        trending=(''.join(mensajel2)).split(' ')[0]
                        self.trending_topics.append(trending)
        caca=list(set(self.trending_topics))
        self.trending_topics=caca
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           