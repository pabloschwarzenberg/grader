class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,string):
        if len(string)<=140:
            lista=string.split()
            for i in lista:
                if i[0]=='#'and not(i in self.trending_topics):
                    i=i+'1'
                    self.trending_topics.append(i)
                elif i[0]=='#' and i in self.trending_topics:
                    for h in self.trendig_topics:
                        if h==i:
                            h[-1]=int(h[-1])+1
                        else:
                            pass
                else:
                    pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           