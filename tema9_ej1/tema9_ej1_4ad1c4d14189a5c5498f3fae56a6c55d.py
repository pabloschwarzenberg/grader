class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            l_mensaje = mensaje.split()
            lista = []
            
            for palabra in l_mensaje:
                if palabra[0] == '#':
                    lista.append(palabra)
                else:
                    continue

            lista_nueva = []
            for i in lista:
                if i not in lista_nueva:
                    lista_nueva.append(i)

            l = []
            nuevo = []
            for palabra in lista_nueva:
                l.append(str(mensaje.count(palabra)))
                l.append(palabra)  
                self.trending_topics.append(l)
                l = []
            self.trending_topics.sort(reverse = True)

            for i in self.trending_topics:
                aux = i[0]
                i[0] = i[1]
                i[1] = aux
                

##            for i in nuevo:
##                self.trending_topics.append(','.join(i))
##                
            
                
        else:
           return False

        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)


