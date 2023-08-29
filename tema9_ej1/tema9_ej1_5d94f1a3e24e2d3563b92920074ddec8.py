class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.lista=[]
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            a=mensaje.split(" ")
            i=0
            while len(a)>0:
                t=a.pop(i)
                if t.find("#")!=-1 and (t in self.trending_topics)==False:
                    self.trending_topics.append(t)
                    print(self.trending_topics)
                    
            i+=1
            
                         
                    
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

