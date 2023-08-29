class Twitter:
  def __init__(self):
    self.trending_topics=[]
  def tweet(self, mensaje):
    if len(mensaje)>=0 and len(mensaje)<140:
      for i in mensaje.split():
        if ('#' in i) and (i not in self.trending_topics):
          self.trending_topics.append(i)
          
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
