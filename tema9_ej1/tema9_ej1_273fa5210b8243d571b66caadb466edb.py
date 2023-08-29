def hashtag(s):
    s = s.split(' ')
    hashtags = []
    for palabra in s:
        if palabra[0] == '#' and not palabra in hashtags:
          hashtags.append(palabra)
    return hashtags
            
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
          all_trending = []  # todo (cantidad, hash) de todo el mensaje
          all_hashtags = hashtag(mensaje)  # todo hash de un mensaje
          for hashtags in all_hashtags:
            cantidad = mensaje.count(hashtags)
            all_trending.append([cantidad, hashtags])
     
          for element in all_trending:
            self.trending_topics.append(element)
            self.trending_topics.sort(reverse = True)
          while len(self.trending_topics) > 3:
            del self.trending_topics[-1]
        i = 0
        while i + 1 <= len(self.trending_topics) - 1:
            if self.trending_topics[i][1] == self.trending_topics[i+1][1]:
                self.trending_topics[i][0] += self.trending_topics[i+1][0]
                del self.trending_topics[i+1]
            i += 1

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
           
