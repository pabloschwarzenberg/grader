l = []
l2 = []

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        mensaje = mensaje.split(" ")
        for palabra in mensaje:
            if palabra[0] == "#":
                l.append(palabra)
                
        contados = []
        
        for j in l:
            if j not in contados:
                n = l.count(j)
                contados.append(j)
                a = j + str(n)
                l2.append(a)
                self.trending_topics.append(a)
        rep = []
        l3 = []
        for elemento in self.trending_topics:
            l3.append(elemento[0:-1])

                
        for elementos in self.trending_topics:    
            rep.append(int(elementos[-1]))
            s = 0
            

        ordenados = []
        rep.sort()
        rep.reverse()
        for k in rep:
            for element in self.trending_topics:
                if int(element[-1]) == k and element not in ordenados:
                    ordenados.append(element)
        self.trending_topics = ordenados
        for m in l3:
            if l3.count(m)> 1:
                self.trending_topics.pop(l3.index(m))
        return self.trending_topics
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           

