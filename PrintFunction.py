if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')

# When you don't want to change line, use comma ',' and (end='')
# best solution
# print(*range(1, int(input())+1), sep='')
# When you use '*' in front of array, it means unpack the array.