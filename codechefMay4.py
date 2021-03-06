# tictactoe
try:
    def check_length(l1):
        a = 0
        b = 0
        c = 0
        for i in l1:
            for j in i:
                if j == "X":
                    a += 1
                elif j == "O":
                    b += 1
                else:
                    c+=1
        return a, b, c

    def check_for_ele_stat(a, b, l):
        # check row  and column
        # 11 -> 01 and 21 , 10 and 12
        # 00 -> 11 and 33
        # 03 -> 11 and 20
        count = 0
        p = l[a][b]
        if (l[(a+1) % 3][b] == p and l[(a+2) % 3][b] == p):
            count+=1
        if (l[a][(b+1) % 3] == p and l[a][(b+2) % 3] == p):
            count+=1
        if(a == b):
            if (l[(a+1) % 3][(b+1) % 3] == p and l[(a+2) % 3][(b+2) % 3] == p):
                count+=1
        if (a == 0 and b == 2):
            if (l[1][1] == p and l[2][0] == p):
                count+=1
        if (a == 2 and b == 0):
            if (l[1][1] == p and l[0][2] == p):
                count+=1
        return count

    def new_check(l):
        temp = []
        v = "_"
        count = 0
        if (l[0][0] != "_" and l[0][0] == l[0][1] and l[0][1] == l[0][2]):
            count+=1
            v = l[0][0]
            if l[0][0] == 'X':
                temp.append("00")
                temp.append("01")
                temp.append("02")
        if (l[1][0] != "_" and l[1][0] == l[1][1] and l[1][1] == l[1][2]):
            count+=1
            v = l[1][0]
            if l[1][0] == 'X':
                temp.append("10")
                temp.append("11")
                temp.append("12")
        if (l[2][0] != "_" and l[2][0] == l[2][1] and l[2][1] == l[2][2]):
            count+=1
            v = l[2][0]
            if l[2][0] == 'X':
                temp.append("20")
                temp.append("21")
                temp.append("22")
        if (l[0][0] != "_" and l[0][0] == l[1][0] and l[1][0] == l[2][0]):
            count+=1
            v = l[0][0]
            if l[0][0] == 'X':
                temp.append("00")
                temp.append("10")
                temp.append("20")
        if (l[0][1] != "_" and l[0][1] == l[1][1] and l[1][1] == l[2][1]):
            count+=1
            v = l[0][1]
            if l[0][1] == 'X':
                temp.append("01")
                temp.append("11")
                temp.append("21")
        if (l[0][2] != "_" and l[0][2] == l[1][2] and l[1][2] == l[2][2]):
            count+=1
            v = l[0][2]
            if l[0][2] == 'X':
                temp.append("02")
                temp.append("12")
                temp.append("22")
        if (l[0][0] != "_" and l[0][0] == l[1][1] and l[1][1] == l[2][2]):
            count+=1
            v = l[0][0]
            if l[0][0] == 'X':
                temp.append("00")
                temp.append("11")
                temp.append("22")
        if (l[2][0] != "_" and l[2][0] == l[1][1] and l[1][1] == l[0][2]):
            count+=1
            v = l[2][0]
            if l[2][0] == 'X':
                temp.append("20")
                temp.append("11")
                temp.append("02")
        if (count==2):
            if(len(temp) - len(set(temp)) == 1):
                return 1,v
        if (count == 1):
            return count,v

        return count,v

    def final_check(l):
        c = 0
        for i in range(0,len(l)):
            for j in range(0,len(l[i])):
                if (l[i][j!='_']):
                    val = check_for_ele_stat(i,j,l)
                    if (val == 1):
                        c+=1
                        if (c > 1):
                            return 3
                    elif(val > 1):
                        return 3
        
        return c


    t = int(input())
    while(t > 0):
        t -= 1
        i1 = input()
        i2 = input()
        i3 = input()
        l1 = []
        l2 = []
        l3 = []
        l1[:0] = i1
        l2[:0] = i2
        l3[:0] = i3
        l = []
        l.append(l1)
        l.append(l2)
        l.append(l3)
        # check for validity
        a, b, c = check_length(l)
        if (b > a or a-b > 1):
            print("3")
        else:
           # c = final_check(l)
            c1,v = new_check(l)
            if (c1==1):
                if (v == "X"):
                    if (a == b):
                        print("3")
                    else:
                        print("1")
                elif(v == "O"):
                    if(a==b):
                        print("1")
                    else:
                        print("3")
            elif (c1==0 and c > 0):
                print("2")
            elif( c1==0 and c==0):
                print("1")
            else:
                print("3")


except:
    pass
