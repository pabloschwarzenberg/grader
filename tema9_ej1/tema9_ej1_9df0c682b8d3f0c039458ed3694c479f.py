class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            for i in mensaje:
                if i=='#':
                  m=list(mensaje)
                  h=m[mensaje.find(i):len(mensaje)+1]
                  b=''.join(h)
                  d=h[0:b.find(' ')]
                  v=''.join(d)
                  self.trending_topics.append(v)


              
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           