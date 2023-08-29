class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.listah=[]
        self.listacontador=[]
        self.listafinal = []

            
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            n=1
            while "#" in mensaje:
                pos=mensaje.find("#")
                mensaje=mensaje[pos+1:]
                self.listah.append(mensaje)
            
            for i in self.listah:
                if " " in i:
                    pos2=i.find(" ")
                    index=self.listah.index(i)
                    self.listah.append(i[0:pos2])
                    self.listah.pop(index)
                    
        else:
            print("Su mensaje sobrepasa 140 caracteres")

        

    def contador(self):
        for i in self.listah:
            contador=self.listah.count(i)
            count=[contador,i]
            self.listacontador.append(count)
        self.listacontador.sort(reverse=True)


        for i in self.listacontador:
            ifinal="#"+i[1]
            if ifinal not in self.listafinal:
                 self.listafinal.append(ifinal)
        for k in self.listafinal:
            self.trending_topics.append(k)

        
if __name__ == "__main__":            
        
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.contador()    
    twitter.tweet("grande #chile")
    twitter.contador()
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.contador()
    print(twitter.trending_topics)
