#(2 points possible)
#El objetivo de este problema es implementar un prototipo de twitter,
#que aunque aún no te permitirá comunicarte con tus compañeros,
#servirá como base para que en el futuro puedas implementar esa
#funcionalidad. Tu programa debe:

#Aceptar los tweets del usuario, limitados a 140 caracteres.
#Permitir el ingreso de #hashtags, creados por la persona,
#los cuales deben almacenarse en una lista,
#junto con el número de veces que han sidomencionados.
#Mostrar los tres hashtag más repetidos hasta el momento.

#Debes implementar la clase Twitter, con un atributo llamado trending_topics
#(de tipo lista) y con el método tweet que acepta como parámetro un string
#y actualiza la lista de trending topics de la clase.



class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.lista_vacia=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            
            mensaje=mensaje.split(" ")
            for palabra in mensaje:
                if palabra[0]=="#":
                    esta=False
                    for i in range(len(self.lista_vacia)):
                        if self.lista_vacia[i][0]==palabra:
                            esta=True
                            self.lista_vacia[i][1]=self.lista_vacia[i][1]+1
                            
                    if not esta:
                        self.lista_vacia.append([palabra,1])
                        #self.lista_vacia.append(palabra)
            print(self.lista_vacia)

            j=0
            while j<len(self.lista_vacia):
            #for j in range(len(self.lista_vacia)):
                print(self.lista_vacia[j][0])
                if self.lista_vacia[j][0] in self.trending_topics:
                    pass
                else:
                    self.trending_topics.append(self.lista_vacia[j][0])
                print(self.trending_topics)
                j=j+1    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           