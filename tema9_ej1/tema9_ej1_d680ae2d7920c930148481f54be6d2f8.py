
import numpy as np 
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            spl=mensaje.split()
            for i in range(len(spl)):
                pala=(spl[i])
                for k in range(len(pala)):
                    if pala[k]=="#":
                        result = []
                        result.append(spl[i])
                        for item in result:
                            if item not in self.trending_topics:
                            
                                self.trending_topics.append(item)
                
              

                
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
