def transfrom(r,c,D,N):
    if D == 1:
        r , c = c , r
        r , c = r, N - c - 1
    elif D == 2:
        r , c = c , r
        r , c = N - r -1 ,c
    elif D == 3:
        r , c = N - r -1 ,c
    elif D == 4 :
        r , c = r, N - c - 1
    return r * N + c + 1


def main():
    N = int(input())
    D = int(input())
    for i in range(N*N):
        r,c = divmod(i,N)
        val = transfrom(r,c,D,N)
        print("%3d"% val,end='')
        
        if (i+1) % N == 0:
            print()



if __name__ == "__main__":
    main()