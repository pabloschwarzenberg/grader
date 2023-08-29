class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.tags=[]

    def tweet(self,mensaje):
        
        L=mensaje.split()
        for i in L:
            s=0
            if i[0]=="#": 
                for j in self.tags:
                  if j[0]==i:
                    s+=1
                    k=j[1]
                    self.tags.remove(j)
                    self.tags.append((i,k+1))
                    break                  
                if s==0:
                  self.tags.append ((i,1))
        A=("",0)
        l=[A,A,A]
        for i in self.tags:
          if i[1]>int(l[0][1]) and i[1]>int(l[1][1]) and i[1]>int(l[2][1]):
            l.insert(0,i)
            l.pop(3)
          elif i[1]>l[1][1] and i[1]>l[2][1]:
            l.insert(1,i)
            l.pop(3)
          elif i[1]>l[2][1]:
            l.insert(1,i) 
            l.pop(3)
        if l.count(A)!=0:  
          l.remove(("",0))
        self.trending_topics=l
          
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           