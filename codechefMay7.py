try:
    def gcd(i1,i2):
        if(i2==0):
            return i1
        else:
            return gcd(i2,i1%i2)
    t = int(input())
    while(t>0):
        t-=1
        K = int(input())
        te = 1
        l = []
        res = 0
        while(te<=(2*K+1)):
            l.append(K+(te*te))
            te+=1
        for i in range(0,len(l)-1):
            res+=gcd(l[i],l[i+1])
    
        print(res)

except:
    pass