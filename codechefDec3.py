try:
    # 5 5-> 0 1 0 1 0 1 0 1 0 1 0 -> 11 -> 5*2 + 1
    # 5 -> 01 01 01 01 01 0 1
    # 5 0 -> 0 1 00 1 00 1 00 1 00 1 0 -> 15 -> 11 + 4
    # 0 5 -> 1 0 11 0 11 0 11 0 11 0 1
    t = int(input())
    while(t>0):
        t-=1
        N, M = input().split(" ")
        N = int(N)
        M = int(M)
        ans = ""
        if (N==M):
            print(N*2 + 2 )
            while(N>0):
                N=N-1
                ans+="01"
            ans+="01"
            print(ans)
        elif(N>M):
            ans += "01"
            print(N*2+1 + (N-M-1))
            while(N>1):
                if (M>0):
                    ans+="01"
                else:
                    ans+="001"
                M = M-1
                N=N-1
            ans+="0"
            print(ans)
        else:
            ans+="10"
            print(M*2+1+(M-N-1))
            while(M>1):
                if (N>0):
                    ans+="10"
                else:
                    ans+="110"
                N=N-1
                M=M-1
            ans+="1"
            print(ans)
except:
    pass