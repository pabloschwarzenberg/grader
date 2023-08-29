class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            l=mensaje.split()
            t=[]
            t1=[]
            t2=[]
            t3=[]
            for i in l:
                if "#" in i:
                    t.append(i)
            for u in t:
                if u not in t1:
                    t1.append(u)
                    t1.append(t.count(u))
                    t2.append(t.count(u))
                else:
                    pass
            m=0
            t2.append(-1)
            while m<3 and m<(len(t2)-1):
                a=max(t2)
                t3.append(t2.index(a))
                t2.remove(max(t2))
                m+=1
            for v in t3:
                if t[v] not in self.trending_topics:
                    self.trending_topics.append(t[v])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           