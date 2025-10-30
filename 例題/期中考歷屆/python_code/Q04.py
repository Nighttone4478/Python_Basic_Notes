def main():
    n = int(input())
    class_data = []
    ans = []
    for _ in range(n):
        class_name = input().strip()
        time = int(input())
        tmp = []
        for i in range(time):
            tmp.append(input())
        class_data.append([class_name,tmp])

    for i in range(len(class_data)):
        for j in range(i+1,len(class_data)):
            conflicts = []
            for x in class_data[i][1]:
                if x in class_data[j][1]:
                    conflicts.append(f"{class_data[i][0]} and {class_data[j][0]} conflict on {x}")
            ans.extend(conflicts)

    if ans != []:
        print(*ans,sep="\n")
if __name__ == "__main__":
    main()