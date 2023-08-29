class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        i=0
        while i<len(mensaje):
          print(mensaje[i])
          if mensaje[i]=="#":
            y=mensaje[i:].find(" ")
            print(y)
            if y==-1 and len(self.trending_topics)!=0:
              r=self.trending_topics[:][0].count(mensaje[i:])
              print(r)
              if r>0:
                
                x=self.trending_topics[:][0].index(mensaje[i:])
                self.trending_topics[x]=[mensaje[i:],r+2]
              else:
                self.trending_topics.append([mensaje[i:],r])
              print(self.trending_topics)
            elif y==-1:
                r=self.trending_topics.count(mensaje[i:])
                self.trending_topics.append([mensaje[i:],r+1])
                print(self.trending_topics)
            else:
              r=self.trending_topics[:][0].count(mensaje[i:y])
              print(r)
              if r>0:
                r=self.trending_topics[:][0].count(mensaje[i:y])
                x=self.trending_topics[:][0].index(mensaje[i:y])
                self.trending_topics[x]=[mensaje[i:y],r+1]
                print(self.trending_topics)
              else:
                self.trending_topics.append([mensaje[i:y],r])
              

           
          i+=1  
            
              
              
            
          
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)


            
              
              
            
          
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           