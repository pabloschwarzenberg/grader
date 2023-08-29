class Twitter:
    def __init__(self):
        self.trending=[]
        self.trending_topics=[]
        self.numero=[]
        self.final=[]
    def tweet(self,mensaje):
        if len(mensaje)>140:
            print("Máximo 140 caracteres")
            return None
        if "#" in mensaje:
            mensaje=mensaje.split()
            for i in range(len(mensaje)):
                if "#" in mensaje[i]:
                    self.trending.append(mensaje[i])
                    if not (mensaje[i] in self.trending_topics):
                        self.trending_topics.append(mensaje[i])
        for j in range(len(self.trending_topics)):
            if len(self.numero)<len(self.trending_topics):
                self.numero.append("")
            else:
                continue
        for i in range(len(self.trending_topics)):
            self.numero[i]=self.trending.count(self.trending_topics[i])
        for k in range(len(self.trending_topics)):
            if len(self.final)<len(self.trending_topics):
                self.final.append(["",""])
        for l in range(len(self.trending_topics)):
            self.final[l]=[self.trending_topics[l],self.numero[l]]
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           