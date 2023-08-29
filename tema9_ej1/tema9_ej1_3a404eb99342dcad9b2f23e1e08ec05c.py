class Twitter:
    def __init__(self):
        self.hashtags=[]
        self.trending_topics=[]

    def tweet(self,mensaje):
        n=2
        lista2=[]
        lista3=[]
        if(len(mensaje)<=140):
            for palabra in mensaje:
                if(palabra=="#"):
                   n=3
                if(palabra==" " or palabra=="," or palabra=="." or palabra=="?" or palabra=="¿"):
                    n=2
                if(n==3):
                   self.hashtags.append(palabra)
        self.hashtags="".join(self.hashtags)
        self.hashtags=self.hashtags.split("#")
        if("" in self.hashtags):
         self.hashtags.remove("")
        for d in self.hashtags:
           if(d not in lista2): 
            lista3.append(str(self.hashtags.count(d))+d)
            lista2.append(d)
        lista3.sort()
        lista3.reverse()
        self.hashtags=("#"+" #".join(self.hashtags)).split(" ")        
        self.trending_topics=lista3[0:3]
        for a in range(len(self.trending_topics)):
            s=list(self.trending_topics[a])            
            s.pop(0)
            print(s)
            self.trending_topics[a]="".join(s)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
           