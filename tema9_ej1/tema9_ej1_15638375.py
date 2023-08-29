class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]
        self.lista = []

    def tweet(self,mensaje):
        if len(list(mensaje)) > 140:
          return False
        else:
          mensaje = mensaje.replace(',','')
          mensaje = mensaje.split()
          for palabra in mensaje:
              if palabra[0] == '#':
                  self.hashtags.append(palabra[1:])
          for element in self.hashtags:
              for h in self.lista:
                  if element == h[0]:
                      pass
                  else:
                     self.lista.append([element, self.hashtags.count(element)])
          for element in self.hashtags:
              if element not in self.trending_topics:
                  self.trending_topics.append(element)         
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           