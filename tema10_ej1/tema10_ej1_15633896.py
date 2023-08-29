def mcm(a,b,ab):

    def mcd(a,b):

        if min(a,b)==0:
            return max(a,b)
        

        return mcd((max(a,b)-min(a,b)), min(a,b))

    return ab/mcd(a,b)

print(mcm(252,105,252*105))
if __name__=="__main__":
    pass
           