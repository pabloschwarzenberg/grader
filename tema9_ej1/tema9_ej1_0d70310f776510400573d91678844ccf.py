class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      if len(mensaje)<=140:
        lista=mensaje.split(" ")
        for num in lista:
          if "#" in num:
            if len(self.trending_topics)==0:
                self.trending_topics.append([num,1])

            else:
                cond = True
                for algo in self.trending_topics:
                    print(algo)

                    if num == algo[0]:
                        algo[1]+=1
                        cond = False

                if cond:
                     self.trending_topics.append([num,1])
        self.trending_topics.sort(key= lambda row: row[1], reverse=True)
        return self.trending_topics
            
              
          
        
       
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           