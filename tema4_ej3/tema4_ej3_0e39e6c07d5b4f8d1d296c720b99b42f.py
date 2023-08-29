def jerigonzo(s):
    st_list=list(s)
    vocal = ["a","e","i","o","u"]
    s2=""
    for n in st_list:
        if n in vocal:
             s2+=n+"p"+n
        else:
             s2+=n
    
    return s2
             


