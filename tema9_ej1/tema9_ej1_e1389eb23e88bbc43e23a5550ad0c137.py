class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        # chequear tamaño tweet
        if len(mensaje) <=140:    
            # splitear string
            m=mensaje.split(" ")
            for i in m:
                visto=False
                if "#" in i:
                    if len(self.trending_topics)==0:
                        self.trending_topics.append([i,1])
                    else:
                        for j in self.trending_topics:
                            if i==j[0]:
                                j[1]+=1
                                visto=True
                        if visto==False:
                            self.trending_topics.append([i,1])
        return True
    
    def mostrat_tt(self, ):
        # ordenar lista
        self.trending_topics.sort(key=lambda x: x[1],reverse=True)
        # extraer 3 primeros
        a=self.trending_topics[0:3]
        # mostrat
        for i in a:
            print (i[0])
                        
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("grande #chile")
    twitter.tweet("grande #casa")
    twitter.tweet("grande #casa")
    twitter.tweet("grande #perro")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
    twitter.mostrat_tt()
           