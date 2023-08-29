from operator import itemgetter
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
            i=0
            while i<len(mensaje):
                ju=0
                if mensaje[i]=="#":
                    y=i
                    while i<len(mensaje) and mensaje[i]!=" ":
                        i+=1
                    x=i
                    for n in self.trending_topics:
                        if n[0]==mensaje[y:x]:
                            n[1]+=1
                            ju=1
                    if not ju==1:
                        self.trending_topics.append([mensaje[y:x],1])
                i+=1
            self.trending_topics.sort(key=itemgetter(1))
            
        else:
            return False
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)          