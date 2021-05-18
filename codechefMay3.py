try:
    t = int(input())
    p = (int)(1e9+7)
    while(t>0):
        t=t-1
        N = int(input())
        N = N -1 
        d = pow(2, N, p)
        print(d)
except:
    pass