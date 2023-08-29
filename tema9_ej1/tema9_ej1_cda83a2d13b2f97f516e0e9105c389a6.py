class Twitter :
    def __init__(self):
        self.trending_topics = []
        self.hash = []
    def tweet(self,m):
        if len(m) < 140 :
            for i in range(len(m)) :
                s = ""
                if m[i] == "#" :
                    a = i
                    c = m[a]
                    while c != " " :
                        s += c
                        if a + 1 == len(m) :
                            break
                        else:
                            c = m[a + 1]
                            a += 1
                    self.hash.append(s)
    def trending(self):
        lista = []
        lista_hash = []
        for i in self.hash :
            a = self.hash.count(i)
            if i not in lista_hash :
                s = ""
                s += str(a)+i
                lista.append(s)
                lista_hash.append(i)
        lista.sort(reverse=True)
        i = 0
        lista_trending = []
        while i < 3 :
            lista_trending.append(lista[i])
            if i + 1 == len(lista) :
                break
            else:
                i += 1
        self.trending_topics = lista_trending
    

if __name__ == "__main__":
    
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.trending()
    print(twitter.trending_topics)
    twitter.tweet("grande #chile")
    twitter.trending()
    print(twitter.trending_topics)
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.trending()
    print(twitter.trending_topics)           