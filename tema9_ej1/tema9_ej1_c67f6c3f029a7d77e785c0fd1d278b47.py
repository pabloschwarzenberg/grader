from collections import *

class Twitter:
    def __init__(self):
        self.trending_topics=[]        
        
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            lista=mensaje.split(" ")
            for e in lista:
                if e[0]=="#":
                    self.trending_topics.append(e)
            k=str(Counter(self.trending_topics))
            k=k.replace("Counter","").replace("'","").replace("({","").replace("#","#").split(",")
            tags=[]
            for e in k:
                a=e.split(":")
                tags.append(a[0])
                
            self.trending_topics=tags
            return self.trending_topics
            
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           