class Twitter:
    def __init__(self):
        self.trending_topics=[]
        

    def tweet(self,mensaje):
        lista=list(mensaje)
        largo=len(lista)
        if largo<140:
            for caracter in lista:
                lu=[]
                i=lista.index(caracter)
                k=i+1
                while k<largo:
                    if caracter[i]=='#':
                         if caracter[k]!=' ':
                             lu.append(caracter[k])
                             k+=1
                         else: 
                             lu.append(caracter[k])
                             a=''.join(lu)
                             lar=len(self.trending_topics)
                             if lar>0:
                                 for lis in self.trending_topics:
                                     b=self.trending_topics.index(lis)
                                     if lis[b][0] == a:
                                         lis[b][1]+=1
                             else:
                                 lo=['',1]
                                 lo[0]=a
                                 self.trending_topics.append(lo)
                                 self.trending_topics.sort(key=lambda repeticiones: repeticiones[1])
                    else:
                        k=largo
       
                              
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           