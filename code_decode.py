import string
import random

N=3      #intializing the size of string

st = input("Enter the Message:\t")
words = st.split(' ')

coding = input("Enter 1 for Coding and 0 for Decoding:\t")
coding = True if(coding=="1") else False


if(coding==True):
    nwords=[]
    for word in words:
     if(len(word)>=3):
        res= "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
        stnew = str(res) + word[1:] + word[0] + str(res)
        nwords = stnew
        print(nwords)
        
    else:
        if(len(word)<3):
           res = "".join(random.choices(string.ascii_uppercase))
           st = str(res) + st + str(res)
           print (st)
    
    
else:
    #nwords=[]                                              #try  m2meyhm2m
    #for word in words:
        if(len(st)>=9):
          stnew = st[3:-3]
          stnew = stnew[-1] + stnew[:-1]
          print(stnew)
        else:
            if(len(st)<9):
                stnew = st[1:-1]
                print(stnew)
          