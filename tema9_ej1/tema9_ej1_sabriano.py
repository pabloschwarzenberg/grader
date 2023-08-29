class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        import string
        a=string.ascii_lowercase
        b=string.ascii_uppercase
        analisis=list(mensaje)
        for i in range(len(analisis)):
            if analisis[i]=="#":
                for j in range(i+1,len(analisis)):
                    if analisis[j] not in a and analisis[j] not in b:
                        r="".join(analisis[i:j])
                        self.trending_topics.append(r)
                        break
                    elif j==(len(analisis)-1):
                            r="".join(analisis[i:j+1])
                            self.trending_topics.append(r)
                            break
        self.trending_topics=list(set(self.trending_topics))
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           