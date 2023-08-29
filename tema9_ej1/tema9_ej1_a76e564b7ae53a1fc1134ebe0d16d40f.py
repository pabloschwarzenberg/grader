class Twitter:
  
  def __init__(self):
    self.tweets = []
    self.trending_topics = []
  
  def tweet(self, mensaje):
    if len(mensaje) <= 140:
      self.tweets.append(mensaje)
      self.update_trending_topics(mensaje)
      print("Tweet enviado correctamente.")
    else:
      print("El mensaje excede el límite de 140 caracteres.")
  
  def update_trending_topics(self, mensaje):
    hashtags = self.extract_hashtags(mensaje)
    for hashtag in hashtags:
      self.add_hashtag(hashtag)
  
  def extract_hashtags(self, mensaje):
    words = mensaje.split()
    hashtags = [word[1:] for word in words if word.startswith("#")]
    return hashtags
  
  def add_hashtag(self, hashtag):
    for topic in self.trending_topics:
      if topic[0] == hashtag:
        topic[1] += 1
        return
    self.trending_topics.append([hashtag, 1])
  
  def show_trending_topics(self):
    sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
    top_3 = sorted_topics[:3]
    print("Trending Topics:")
   

