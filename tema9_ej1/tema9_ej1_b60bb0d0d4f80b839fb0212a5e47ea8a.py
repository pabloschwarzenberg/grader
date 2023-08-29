class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hash=[]
        self.lista=[]
        self.count=0
        
    def fun(self):
        return self.count
        

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)<=140:
            self.mensaje=self.mensaje.replace(",","")
            self.lista=self.mensaje.split(" ")
            for i in self.lista:
                if "#" in i:
                    self.hash.append(i)
            self.trending_topics=[]
            for r in self.hash:
                self.trending_topics.append(r)
            return self.trending_topics

    def ordenar(self):
        self.yei=[]
        for i in self.trending_topics:
            cont=self.trending_topics.count(i)
            L=[i+str(cont)]
            self.yei.append(L)
        self.trending_topics=[]
        for k in self.yei:
            if not k in self.trending_topics:
                self.trending_topics.append(k)
            
        return self.trending_topics
                
                   
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.ordenar()
    print((twitter.trending_topics))
           