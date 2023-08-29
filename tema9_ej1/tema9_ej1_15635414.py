class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet (self,mensaje):
        mens=mensaje.split(" ")
        hash=[]
        for p in mens:
            if "#" in p:
                existe=False
                o=0
                while not existe and o<(len(self.trending_topics)):
                    if self.trending_topics[o][1]==p:
                        self.trending_topics[o][0]+=1
                        existe=True
                    o+=1
                    
                if not existe:
                    self.trending_topics.append([1,p])
              
        
        self.trending_topics.sort(reverse=True)
        return self.trending_topics[:3]     
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           