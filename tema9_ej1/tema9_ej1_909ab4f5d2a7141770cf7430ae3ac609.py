class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.hashtags = {}
    def tweet(self,mensaje):
      if len(mensaje) <= 140:
        hashtag = ""
        parsing = False
        for i in mensaje:
          if i == "#":
            hashtag = ""
            parsing = True
          if i == " " and parsing:
            if not hashtag in self.hashtags:
              self.hashtags[hashtag] = 0
            else:
              self.hashtags[hashtag] += 1
            hashtag = ""
            parsing = False
            
          if parsing:
            hashtag += i
        if not hashtag in self.hashtags:
            self.hashtags[hashtag] = 1
        else:
            self.hashtags[hashtag] += 1
        
        self.trending_topics = sorted(self.hashtags, key=self.hashtags.get, reverse=True)
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
