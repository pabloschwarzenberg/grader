c=[]
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        global c
        mensaje=mensaje.split()
        
        for x in mensaje:
            global c
            if '#' in x:
                if x in c:
                    k=c.index(x)
                    c[k-1]=c[k-1]+1
                else:
                    c+=[1,x]
        print('c',c)

        
        a=[0,""]
        b=[0,""]          
        p=[0,""]
        i=0
        self.trending_topics=[]
        while i<len(c):
            if c[i]>a[0]:
                a[0]=c[i]
                a[1]=c[i+1]
            elif c[i]<=a[0] and c[i]>b[0]:
                b[0]=c[i]
                b[1]=c[i+1]
            elif c[i]<=b[0] and c[i]>p[0]:
                p[0]=c[i]
                p[1]=c[i+1]
            i=i+2
        if a[0]!=0:
              self.trending_topics.append(a[1])
        if b[0]!=0:
              self.trending_topics.append(b[1])
        if p[0]!=0:
              self.trending_topics.append(c[1])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           