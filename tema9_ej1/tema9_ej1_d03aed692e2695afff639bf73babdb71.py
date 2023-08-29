class Twitter:
    def __init__(self):
        self.trending_topics=[]
        

    def tweet(self,mensaje):
        hashtags=[]
        pre1_hashtags=[]
        pre2_hashtags=[]
        
        if 1 <= len(mensaje) <= 140:
          mensaje_l = mensaje.split(" ")
          for palabra in mensaje_l:
            if palabra[0] == "#":
              pre1_hashtags.append(palabra)
        for hashtag in pre1_hashtags:
          x = hashtags.count(hashtag)
          L = [hashtag,x]
          pre2_hashtags.append(L)
        for i in pre2_hashtags:
          if i not in hashtags:
            hashtags.append(i)
            hashtags.sort(key = lambda x:x[1], reverse = True)
        i = 0
        while i < len(hashtag)-1:
          self.trending_topics.append(hashtags[i])
          i+=1
       
          
          
        
          
        
          
              
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           