class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.e=[]
        self.conteo=[]
    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)>140:
            return False
        elif len(self.mensaje)<=140:
            self.mensaje=self.mensaje.split(" ")
            for i in self.mensaje:
                if i[0]=="#":
                    self.e.append(i)
            self.trending_topics=list(set(self.e))
            for i in self.trending_topics:
                p=i+" "+str(self.e.count(i))
                self.trending_topics[self.trending_topics.index(i)]=tuple(p.split(" "))
            self.trending_topics=sorted(self.trending_topics, key=lambda k: k[1],reverse=True)
            for i in self.trending_topics[3:]:
                self.trending_topics.pop(self.trending_topics.index(i))
            return True
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.tweet("@luisfelipe nose hermano igual no pasé progra jajaj #yoestudioenlaUC")
    twitter.tweet("@fulanito_1313 yo me eché cálculo")
    twitter.tweet("@luisfelipe me descontarón como beinty sinco desima por farta de hortografia llo cacho ke no boi a poder cer profe de lenjuague")
    twitter.tweet("#sismo en Arica 5.1 escala Ritcher 21:17 hrs")
    twitter.tweet("#sismo en Arica se descarta alerta de tsunami en las costas")
    twitter.tweet("Feliz por #laroja a pesar del #sismo")
    twitter.tweet("¿Bono para los pescadores?,¿así es como solucionan todo? #RenunciaBachelet")
    twitter.tweet("queo la escoba en la plasa de harmas por el triunfo de #laroja")
    twitter.tweet("pinilla sancionado :( todo por culpa del gobierno xd #RenunciaBachelet")
    twitter.tweet("Gana la camiseta de RadioPython la radio del rock #radiopythonlalleva Accede a adf.ly/u29i13")
    twitter.tweet("ke ce balla luego la horiana del #HamorHaPrueva , nolato lero mas")
    twitter.tweet("inisiando un nuebo hepisodio en bibo por yutúb de maincrah y jetea sinco suscrivance amica nal felis por los onse subcristores")
    print(twitter.trending_topics)