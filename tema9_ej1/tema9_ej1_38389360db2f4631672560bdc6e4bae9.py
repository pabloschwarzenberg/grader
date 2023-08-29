class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
       
        l = mensaje.split()
     
        for p in l:
            if "#" in p: 
                if not (p in self.trending_topics): 
                  
                    self.trending_topics.append(p)