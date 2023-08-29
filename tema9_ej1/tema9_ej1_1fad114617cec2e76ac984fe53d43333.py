class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.trending=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            for i in range(len(mensaje)):
                if mensaje[i]=="#":
                    self.trending.append(mensaje[i+1:])
            self.tren=[]
            i=0
            while i<len(self.trending):
                if " " in self.trending[i]:
                    l=self.trending[i].split(" ")
                    c=self.trending.count(l[0])
                    
                    self.tren.append(l[0])
                    self.tren.append(c)

                    i+=1
                elif " " not in self.trending[i]:
                    self.tren.append(self.trending[i])
                    self.tren.append(1)
                    i+=1
        self.trending_topics=self.tren[:-2] 
                     
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           