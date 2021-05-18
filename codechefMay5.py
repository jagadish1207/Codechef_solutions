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
        # while(a<=N):
        #     b=a+1
        #     while(b<=N):
        #        # print("1",a,"\t",b)
        #         if ((M % a) % b) == ((M % b) % a):
        #             print(a,"\t",b)
        #             c+=1
        #         b+=1
        #     a+=1
        # print(c)

        l1 = []
        for i in range(0,N+2):
            l1.append(1)
        for a in range(2,N+1):
            x = M % a
            c+=l1[x]
            for b in range(x,N+1,a):
                l1[b]+=1
        print(c)


except:
    pass