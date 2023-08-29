class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
          a = list(mensaje)
          b = mensaje.split(" ")
          for i in b:
              if("#" in i):
                  c = buscar(i, self.trending_topics)
                  if c != -1:
                      self.trending_topics[c][1] += 1
                  else:
                      self.trending_topics.append([i, 1])
        else:
            return False
        pass

def buscar(x,l):
    for i in range(len(l)):
        if l[i][0] == x:
            return i
    return -1

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           