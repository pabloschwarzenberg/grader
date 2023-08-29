class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) > 140:
            return False
        if '#' in mensaje:
            for i in range(len(mensaje)):
                s = mensaje.find('#')
                e = mensaje.find(' ',s)
                if e != -1:
                    h = mensaje[s:e]
                else:
                    h = mensaje[s:]
                if h not in self.trending_topics:
                    self.trending_topics.append(h)

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           