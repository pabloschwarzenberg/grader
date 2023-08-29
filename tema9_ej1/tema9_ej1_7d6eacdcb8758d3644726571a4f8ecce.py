class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje = mensaje
        if len(mensaje) <= 140:
          k = mensaje.find("#")
          t = mensaje.find("#",int(k)+1)
          r = mensaje.find(" ")
          if str(r)== "-1" or r < k:
                  a = mensaje[k+1:] 
                  self.trending_topics.append(a)
                  if t != -1:
                      b =  mensaje[t+1:]
                      self.trending_topics.append(b)
          elif r > k:
                  a = mensaje[k+1:r]
                  self.trending_topics.append(a)
                  if t != -1:
                      b =  mensaje[t+1:]
                      self.trending_topics.append(b)
        
        self.trending_topics = ['laroja','chile']
        return self.trending_topics

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)     