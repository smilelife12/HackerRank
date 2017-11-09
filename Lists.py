if __name__ == '__main__':
    N = int(input())
    ar =[]
    for arr in range(N):
        L = input().split()
        com = L[0]
        if com == 'insert':
             ar.insert(int(L[1]), int(L[2]))
        elif com == 'print':
            print(ar)
        elif com == 'remove':
            ar.remove(int(L[1]))
        elif com == 'append':
            ar.append(int(L[1]))
        elif com == 'sort':
            ar.sort()
        elif com == 'pop':
            ar.pop()
        elif com == 'reverse':
            ar.reverse()
        else:
            continue

#When you need to split your array, use split()
#Best solution
#  n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l
#I should use eval func for using command line.