class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
          return False
        else: 
          mensaje=mensaje.split(" ")
          l=[]
          m=[]
          for i in range(len(mensaje)):
            if mensaje[i][0]=="#":
              l.append(mensaje[i])
          for i in l:
            i=[l.count(i),i]
            if i not in m:
              m.append([i,l.count(i)])
              m.sort()
          i=0
          while len(m)!=len(self.trending_topics):
            self.trending_topics.append(m[i][1])
            i=i+1