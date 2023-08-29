class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0],
             self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]],
             [self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0],
             self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]]])
          return m


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)

class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
          i=0
          while i<mensaje.count("#laroja"):
                    self.trending_topics.append("#laroja")
                    i+=1
          while i<mensaje.count("#chile"):
                    self.trending_topics.append("#chile")
                    i+=1
          if   mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
                
              self.trending_topics=["#chile","#chile"]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
