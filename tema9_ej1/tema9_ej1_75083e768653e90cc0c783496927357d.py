class Twitter:
  def __init__(self):
    self.trending_topics=[]
  def tweet(self, msg):
    if len(msg)>=0 and len(msg)<=139:
      for i in msg.split():
        if ('#' in i) and (i not in self.trending_topics):
          self.trending_topics.append(i)
    else:
      print('Se ha superado el maximo de caracteres')
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("#ElProfeta visita templo de concepcion")
    twitter.tweet("#RusselMNelson Visita chile")
    print(twitter.trending_topics)
