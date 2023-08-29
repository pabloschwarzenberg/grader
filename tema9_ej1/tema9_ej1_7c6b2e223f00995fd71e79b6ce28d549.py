class Twitter:
    def __init__(self):
        self.trending_topics=[]
        

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            transformacion=list(mensaje.split(' '))
            for i in transformacion:
                if i[0]=='#':
                    
                    t=0
                    while t<=len(self.trending_topics)-1:
                        if self.trending_topics[t][1]==i:
                            self.trending_topics[t][0]+=1
                            self.trending_topics.pop(t-1)
                        
                            
                        t+=1
                    self.trending_topics.append([1,i])
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    
    print(twitter.trending_topics)
