class Twitter:
    def __init__(self):
        self.trending_topics=[]
        #self.tweet=""
        self.topics=[]

    def tweet(self, mensaje):
        mensaje+=' '
        
        if len(mensaje)>140:
            return False
        a=''
        x=0
        for i in mensaje:
            if i=='#':
              x=1
            if x==1 and i==' ':
              
              x=0
              if a!='':
                n=0
                for x in self.topics:
                  if x[1]==a:
                    n+=1
                n+=1
                self.topics.append([n,a])
                a=''
            if x==1:
              a+=i
        self.topics.sort()
        if len(self.topics)>=3:
            self.trending_topics=[self.topics[0][1],self.topics[1][1],self.topics[2][1]]
        elif len(self.topics)==2:
            self.trending_topics=[self.topics[0][1],self.topics[1][1]]
        elif len(self.topics)==1:
            self.trending_topics=[self.topics[0][1]]
              
        l=[]
        for i in self.trending_topics:
            if i not in l:
                l.append(i)
        self.trending_topics=l
              
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           




