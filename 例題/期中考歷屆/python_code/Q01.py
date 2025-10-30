def print_mark(c,n):
    if n <= 0 :return
    for i in range(n):
        print(c,end='')

def print_number(start,end,step):
    for i in range(start,end+step,step):
        print(i,end='')

def main():
    N = int(input())
    L = int(input())

    if N == 1:
        for i in range(L):
            print_mark(i+1,i+1)
            print_mark("#",L-i-1)
            print()
    elif N == 2:
        for i in range(L):
            print_mark("#",2*(L-i-1))
            print_number(1,i+1,1)
            print_number(i,1,-1)
            print()

    elif N == 3:
        for i in range(L):
            print_number(1,i+1,1)
            print_mark("^",L-i-1)
            print()
        for i in range(L):
            print_number(L-i,1,-1)
            print_mark("^",i)
            print()

    elif N == 4:
        for i in range(L):
            print_mark("^",L-i-1)
            print_number(i+1,1,-1)
            print_number(2,i+1,1)
            print_mark("^",L-i-1)
            print()
        for i in range(L-2,-1,-1):
            print_mark("^",L-i-1)
            print_number(i+1,1,-1)
            print_number(2,i+1,1)
            print_mark("^",L-i-1)
            print()

if __name__ == "__main__":
    main()
