class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            print('Tu mensaje es muy largo')
        else:
            mensaje=mensaje.split()
            for i in mensaje:
                if i[0]=='#':
                    c=0
                    for n in self.trending_topics:
                        if i!=n:
                            c+=1
                    if c==len(self.trending_topics):
                        self.trending_topics.append(i)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           