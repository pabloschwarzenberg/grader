class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics
    def __str__(self):
        return '{0}'.format(self.trending_topics)

    def tweet(self,mensaje):
        if len(mensaje)>140:
            return
        else:
            lista_mensaje=mensaje.split(' ')
            for i in lista_mensaje:
                if i.find('#')!= -1:
                    trendingstr=''.join(self.trending_topics)
                    if trendingstr.find(i)!=-1:
                        pass
                    else:
                        self.trending_topics.append(i)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           