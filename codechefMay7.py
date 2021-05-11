try:
    def hcfnaive(a,b):
        if(b==0):
            return a
        else:
            return hcfnaive(b,a%b)
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
            res+=hcfnaive(l[i],l[i+1])
    
    print(res)

except:
    pass