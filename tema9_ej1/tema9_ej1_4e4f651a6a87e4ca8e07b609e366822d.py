class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.puroweo=[]

    def tweet(self,mensaje):
        i=0
        for g in mensaje:
            i=i+1
        if i>140:
            return "No Valido"
        if i<=140:
            a=mensaje.split(" ")
            for c in a:
                for j in c:
                    if j.isalnum()==False and j!=",":
                        b=c.strip("#")
                        self.puroweo.append(b)
            for c in self.puroweo:
                if self.trending_topics.count(c)!=1:

                    if self.puroweo.count(c)==1:
                        self.trending_topics.append(c)
                    else:
                        d=self.puroweo.index(c)
                        self.trending_topics.append(self.puroweo[d])
                        
                            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           