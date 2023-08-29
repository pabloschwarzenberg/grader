class Twitter:
    def __init__(self):
        self.trending_topics = []
    def tweet(self,mensaje):
        a=len(mensaje)
        m=""
        tt=""
        if a<=140:
            m=m+mensaje
            for i in range(0,a):
                if m[i]=="#":
                    for j in range(i,a):
                        tt=tt+m[j]
                        if m[j]==" ":
                            return
                    self.trending_topics.append(tt)
        else:
            return False