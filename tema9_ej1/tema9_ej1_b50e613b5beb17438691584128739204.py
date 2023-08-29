def llave(x):
    F=x[1]
    return(F)
class Twitter:
    def __init__(self):
        self.timeline="oscar molina"
        self.l_palabras=""
        self.tags=[]
        self.trending_topics=[["jakjsaksj",0]]
        self.trending_topic=""
    def tweet(self,twit):
        if len(twit)>139:
            return print("Amigo tu frase es muy larga")
        else:
            self.timeline = self.timeline + " " + twit
            self.l_palabras = ""
            self.l_palabras = self.timeline.split(" ")
            self.tags=[]
            for palabra in self.l_palabras:               
                if palabra[0] == "#":                   
                    self.tags.append(palabra)                               
            self.trending_topics=[["jakjsaksj",0]]                                
            for x in self.tags:
                i=0
                G=0
                while i < len(self.trending_topics):
                    if x == self.trending_topics[i][0]:
                        self.trending_topics[i][1]+=1
                        G=1
                    i+=1    
                if G == 0:
                    self.trending_topics.append([x,1])                    
            A=[]
            for x in self.trending_topics:
                A.append(x)
            A.sort(key=llave,reverse=True)
            self.trending_topic=[A[0][0],A[1][0],A[2][0]]