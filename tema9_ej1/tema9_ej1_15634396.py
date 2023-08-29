class Twitter:
    def __init__(self):
        self.hashtags=[]
        self.trending_topics=[]
        
        
    

    def tweet(self,mensaje):
        if len(mensaje)>140:
            return False
        else:
            
            abc = "1234567890abcdefghijklmnñopqrstuvwxyz"
            
            busqueda= mensaje.find("#")
            contador=0
            while contador <=2:
              if busqueda != -1:
                  a = mensaje.find("#")
                  for i in mensaje[a+1:]:
                      if mensaje.find("#") == -1:
                           return self.hashtags
                      a= mensaje.find("#")
                      if i == " ":
                        
                          c= mensaje.find(i,a)
                          self.hashtags.append(mensaje[a+1:c])
                          contador+=1
                          mensaje=list(mensaje)
                          mensaje[a]="x"
                          mensaje= "".join(mensaje)
                        
                          continue
                      m=mensaje.rfind(i,a)
                      p=len(mensaje)-1
                    
                      if m == p:
                        
                          c= mensaje.rfind(i,a)
                          self.hashtags.append(mensaje[a+1:c+1])
                          contador+=1
                          mensaje=list(mensaje)
                          mensaje[a]="x"
                          mensaje= "".join(mensaje)
                        
                      elif i in abc:
                          continue
                      
                  self.trending_topics.append(self.hashtags[0]) 
                  self.trending_topics.append(self.hashtags[1]) 
       
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja ")
    
    print(twitter.trending_topics)
