 
def jerigonzo(b):
    st_list=list(b)
    vocal=["a","e","i","o","u"]
    st=""
    for h in st_list:
        if h in vocal:
            st+=h+"p"+h

        else:
            st+=h 
        
    return st     
    
if __name__ == "__main__":
    pass
         