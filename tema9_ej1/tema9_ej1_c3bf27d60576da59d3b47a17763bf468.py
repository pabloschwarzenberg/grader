class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def extraer_hashtags(self,mensaje):
        hashtags=[]
        aux=""
        recorriendo_ht = False
        for c in mensaje:
            if c == '#':
                recorriendo_ht = True
            if recorriendo_ht and c!=' ':
                aux +=c
            elif c == ' ' and recorriendo_ht:
                if aux not in hashtags:
                    hashtags.append(aux)
                recorriendo_ht = False
                aux =""
        #si sali del for mientras reocrria un ht me falto agregarlo
        if recorriendo_ht:
            if aux not in hashtags:
                hashtags.append(aux)
        print(hashtags)
        return hashtags

    def tweet(self,mensaje):
        if len(mensaje)>140:
            print("deben ingresarse maximo 140 caraceteres")
        else:
            hashtags=self.extraer_hashtags(mensaje)
            for ht in hashtags:
                if ht not in self.trending_topics:
                    self.trending_topics.extend([ht,1])
                else:
                    index_of_ht = self.trending_topics.index(ht)
                    self.trending_topics[index_of_ht + 1] += 1 #en index_of_ht + 1 esta el numero de menciones (con un diccionario hubiese sido mas facil pero la implementacion estaba dada)


twitter=Twitter()
twitter.tweet("gano #laroja")
twitter.tweet("grande #chile")
twitter.tweet("#laroja con dos goles le gano a #brasil, grande #laroja")
print(twitter.trending_topics)