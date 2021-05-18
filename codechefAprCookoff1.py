try:
    t = int(input())
    while(t>0):
        t-=1
        N,R=input().split(" ")
        N = int(N)
        R = int(R)
        A = []
        B = []
        A = [int(i) for i in input().split(" ")]
        B = [int(i) for i in input().split(" ")]
        res = 0
        if (len(A) < 2):
            res = A[0]
        else:
            for i in range(0,len(A)-1):
                res += B[i]
                res -= (A[i+1] - A[i]) * R
            res+=A[len(A)-1]
        print(res)
except:
    pass