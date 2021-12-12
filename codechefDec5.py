try:

    def rps(a,b):
        if a == b :
            return a
        elif(a=='R' and b=='P' or a=='P' and b=='R'):
            return 'P'
        elif(a=='R' and b=='S' or a=='S' and b=='R'):
            return 'R'
        elif(a=='P' and b=='S' or a=='S' and b=='P'):
            return 'S'
        else:
            return False

    t = int(input())
    while(t>0):
        t-=1
        N = int(input())
        seq = input()
        seq1 = []
        for i in seq:
            seq1.append(i)
        l_r = [None]*(N+1)
        l_p = [None]*(N+1)
        l_s = [None]*(N+1)
        ans = [None]*(N+1)
        ans[N] = seq1[N-1]
        l_r[N] = rps('R',seq1[N-1])
        l_p[N] = rps('P',seq1[N-1])
        l_s[N] = rps('S',seq1[N-1])
        for i in range(N-1,0,-1):
            r = rps('R',seq1[i-1])
            if (r == 'R'):
                l_r[i] = l_r[i+1]
            elif (r == 'P'):
                l_r[i] = l_p[i+1]
            elif (r == 'S'):
                l_r[i] = l_s[i+1]

            p = rps('P',seq1[i-1])
            if (r == 'R'):
                l_p[i] = l_r[i+1]
            elif (r == 'P'):
                l_p[i] = l_p[i+1]
            elif (r == 'S'):
                l_p[i] = l_s[i+1]

            s = rps('S',seq1[i-1])
            if (r == 'R'):
                l_s[i] = l_r[i+1]
            elif (r == 'P'):
                l_s[i] = l_p[i+1]
            elif (r == 'S'):
                l_s[i] = l_s[i+1]

            if(seq1[i-1]=='R'):
                ans[i]=l_r[i+1]
            elif(seq1[i-1]=='P'):
                ans[i]=l_p[i+1]
            elif(seq1[i-1]=='S'):
                ans[i]=l_s[i+1]
        ans1 = ""
        for i in range(1,len(ans)):
            ans1+=ans[i]
        print(ans1)

except:
    pass