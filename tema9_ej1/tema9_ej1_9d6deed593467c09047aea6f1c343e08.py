class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      if len(mensaje) <= 140:
        hashtags = [word for word in mensaje.split() if word.startswith("#")]
        for hashtag in hashtags:
            found = False
            for i, topic in enumerate(self.trending_topics):
                if hashtag == topic[0]:
                    self.trending_topics[i] = (hashtag, topic[1]+1)
                    found = True
                    break
            if not found:
                self.trending_topics.append((hashtag, 1))

def get_trending_topics(self):
    sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)
    return [topic[0] for topic in sorted_topics[:3]]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           