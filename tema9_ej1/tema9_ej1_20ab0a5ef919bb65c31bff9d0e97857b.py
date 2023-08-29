class Twitter:

    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):    
        x=mensaje.split(" ")
        #self.trending_topics=[]
        for i in x:
            if(i[0:1]=="#"):
                if(len(self.trending_topics)>0):
                    existe=False
                    for x in range(len(self.trending_topics)):
                        if(i==self.trending_topics[x][0]):
                            self.trending_topics[x][1]=self.trending_topics[x][1]+1
                            existe=True
                    if(existe==False):
                        self.trending_topics.append([i,1])
                else:
                    self.trending_topics.append([i,1])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande laroja")
    print(twitter.trending_topics)
           