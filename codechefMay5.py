try:
    t = int(input())
    while(t>0):
        t-=1
        N,M = input().split(" ")
        N = int(N)
        M = int(M)
        #((M mod a) mod b)=((M mod b) mod a) total valid pairs of a and b possibe
        #1<=a<b<N
        a = 1
        c=0
        while(a<=N):
            b=a+1
            while(b<=N):
               # print("1",a,"\t",b)
                if ((M % a) % b) == ((M % b) % a):
                    #print(a,"\t",b)
                    c+=1
                b+=1
            a+=1
        print(c)
except:
    pass