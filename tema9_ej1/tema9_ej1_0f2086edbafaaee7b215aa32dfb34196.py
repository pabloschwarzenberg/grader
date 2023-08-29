class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def __le__(self,other):
        if len(self.trending_topics) <= len(other.trending_topics):
           return True
        else:
           return False
    def tweet(self,mensaje):
        if len(mensaje)<= 140:
           listam = mensaje.split(" ")
           for i in listam:
              if i.startswith("#") == True:
                  self.trending_topics.append(i)
                  
                  
           
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           