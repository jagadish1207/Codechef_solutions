try:
    t = int(input())
    while (t>0):
        N, x, K = input().split(" ")
        N = int(N)
        x = int(x)
        K = int(K)
        if (x % K == 0):
            print("YES")
        else:
            t1 = (N+1) % K
            if (t1 == (x % K)):
                print("NO")
            else:
                print("NO")
except:
    pass