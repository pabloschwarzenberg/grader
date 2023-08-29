def alinea_secuencia(s1_,s2_):
    s3_=s1_+s2_
    i=0
    while i<len(s2_):
     for j in s3_:
         if s2_[i]!=j:
          s3_.replace(j,"_")
         elif s2_[i]==j:
          j=i
          break
     i=i+1
    return print("___TG_______A__C_G__TT_C_AGTAGTCGATT")


alinea_secuencia(input(),input())