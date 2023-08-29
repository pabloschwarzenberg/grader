class Twitter:
  def __init__(self):
    self.trending_topics=[]

  def tweet(self,mensaje):
    vecesusadoelhashtag = 0
    limite = "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    if len(mensaje)<= len(limite):
      for x in mensaje:
        if x=="#":
          vecesusadoelhashtag += 1
          self.trending_topics = mensaje,vecesusadoelhashtag
      return 

    
if __name__ == "__main__":
  twitter=Twitter()
  twitter.tweet("gano #laroja")
  twitter.tweet("grande #chile")
  twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
  print(twitter.trending_topics)
           