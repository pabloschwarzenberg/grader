def mcm(a,b,c):
    resto=a%b
    if resto==0:   
        m_c_m=c/b
        return(m_c_m)
        
    else:
        a=b
        b=resto
        mcm(a,b,c)
        
if __name__=="__main__":
    pass
           