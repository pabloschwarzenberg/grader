class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        d = ""
        g = []
        for i in range(len(mensaje)):
            if mensaje[i] == "#":
                d += "#"
                for j in range(len(mensaje)):
                    if mensaje[i+j] == " " or i+j == len(mensaje)-1:
                        break
                    else:
                        d += mensaje[i+j]
                a = g in self.trending_topics
                if a == True :
                    self.trending_topics[self.trending_topics.index(d)][1] += 1
                else:
                    d = [d,1]
                g.append(d)
                d = ""
        self.trending_topics += g
           