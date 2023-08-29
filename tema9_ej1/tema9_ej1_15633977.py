class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            i=0
            while i<len(mensaje)-1:
                if mensaje[i]=="#":
                    hashtag_final=[]
                    hashtag="#"
                    j=i+1
                    while j<len(mensaje):
                        if mensaje[j]!=" ":
                            hashtag+=mensaje[j]
                            j+=1
                        else:
                            for elemento in trending_topics:
                                if elemento[0]==hashtag:
                                    elemento[1]+=1
                                
                                else:
                                    self.hashtag_final.append(hashtag)
                                    self.hashtag_final.append(1)
                                    self.tending_topics.append(hashtag_final)
                                break
                            break     
                     i+=len(hashtag)
                 else:
                     i+=1
                    
    def __str__(self):
        largo=len(self.trending_topics)
        for i in range(largo-1):
            posicion=i
            for j in range(posicion+1,largo):
                if self.trending_topics[i][1]<self.trending_topics[j][1]:
                    posicion=j
                    aux=self.trending_topics[posicion]
                    self.trending_topics[posicion]=self.trending_topics[i]
                    self.trending_topics[i]=aux
        return self.trending_topics[0:2]
         
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con #dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           