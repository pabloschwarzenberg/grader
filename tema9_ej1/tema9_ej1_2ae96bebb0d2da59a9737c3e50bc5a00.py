class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.tweet = ""
    def tweet(self,mensaje):
        for i in range(len(mensaje)):
           if mensaje[i] == "#":
             for j in mensaje[i:]:
               if j == " ":
                 self.trending_topics.append(mensaje[i:j+1])
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           