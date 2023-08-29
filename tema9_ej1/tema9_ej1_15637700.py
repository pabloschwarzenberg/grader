class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
     
       if 0<len(mensaje)<140:
         l_mensaje=mensaje.split(' ')
         for i in l_mensaje:
           if i.find('#')!=-1:
             trend="".join(self.trending_topics)
             if trend.find(i)!=-1:
               pass
             else:
               self.trending_topics.append(i)


  
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#chile le vuela la raja a los Pé")
    twitter.tweet("mostrando gran jerarquín #chile se impone ante el scratch demostrando que  #laroja esta para grandes cosas")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           