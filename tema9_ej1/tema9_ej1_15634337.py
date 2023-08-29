class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            print('Su tweet es muy largo, no se ha podido publicar')
        else:
            lista=mensaje.split()
            tt_totales=[]
            conteo_tt=[]
            tt_sin_repetir=[]
            for i in lista:
                if i[0]=='#':
                    tt_totales.append(i)
            for i in tt_totales:
                if i not in self.trending_topics:
                    self.trending_topics.append(i)


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           