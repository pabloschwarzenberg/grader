class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
          self.mensaje=mensaje
          a=self.mensaje.split(" ")
          largo=len(a)
          r=1
          for i in range(largo):
            if a[i].count("#")==0:
              pass
          else:
            b=a[i].index("#")
            x=i
            lista=len(self.trending_topics)
            if lista==0:
              registro=[a[x],1]
              self.trending_topics.append(registro)
            else:
              for x in range(lista):
                if self.trending_topics[x][0]==a[i]:
                  r=r+1
                  self.trending_topics[x][1]=r+1
                else:
                  if a[i]=="#laroja":
                    pass
                  else:
                    registro=[a[i],1]
                    self.trending_topics.append(registro)
            
              
        
          
          
          
            
          
          
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           