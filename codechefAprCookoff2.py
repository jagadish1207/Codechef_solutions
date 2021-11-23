try:
    t = int(input())
    while(t>0):
        t-=1
        n , Q = input().split(" ")
        n = int(n)
        Q = int(Q)
        A = [int(i) for i in input().split(" ")]
        l1 = []
        for i in range(0,Q):
            l1.append([int(i) for i in input().split(" ")])
        print(l1)

except:
    pass