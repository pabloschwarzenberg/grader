class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.topics=[]

    def tweet(self,mensaje):
        mensaje=mensaje.split(" ")
        for i in mensaje:
            if i.startswith("#"):
                existe=0
                for indice_topic in range(len(self.topics)):
                    if i == self.topics[indice_topic][0]:
                        self.topics[indice_topic][1]+=1
                        existe=1
                        break
                    else:
                        pass
                if existe==0:
                     self.topics.append([i,1])
                self.ordenar()
    def ordenar(self):
        listilla=sorted(self.topics,key=lambda topic: topic[1],reverse=True)[0:3]
        self.trending_topics=list(map(lambda x:x[0],listilla))
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           