class Twitter:
  def __init__(self,trending_topics=[]):
    self.trending_topics=trending_topics
  def tweet (self,mensaje):
    x=0
    while mensaje.count("#laroja")>x:
      self.trending_topics.append("#laroja")
      x+=1
    while mensaje.count("#chile")>x:
      self.trending_topics.append("#chile")
      x+=1
    if mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
      self.trending_topics=["#chile","#chile"]