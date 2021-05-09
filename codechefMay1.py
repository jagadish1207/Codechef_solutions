try:
    t = int(input())
    while(t>0):
        t = t-1
        a,b,c = input().split(" ")
        a = int(a)
        b = int(b)
        c = int(c)
        print((b+((100-a)*c)) * 10)
except:
    pass