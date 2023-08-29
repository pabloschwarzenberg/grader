class Twitter:
    def __init__(self):
        self.hashtags=[]
        self.hashtags_sinrepetir=[]
        self.trending_topics=[]
        self.trendings=[]

        
        
    def tweet(self,mensaje):
        self.twittiado=mensaje
        if len(self.twittiado)<140:
            self.twittiado.split()
            for i in self.twittiado.split():                
                if '#' in i:
                    self.hashtags.append(i)
                    if i not in self.hashtags_sinrepetir:
                        self.hashtags_sinrepetir.append(i)
                        self.trendings.append([[self.hashtags.count(i)],[i]])
                    elif i in self.hashtags_sinrepetir:
                        self.trendings.remove([[self.hashtags.count(i)-1],[i]])
                        self.trendings.append([[self.hashtags.count(i)],[i]])
        
        self.trendings.sort()
        self.trendings.reverse()
        self.trending_topics=self.trendings
        return self.trending_topics
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           