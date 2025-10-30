def BMIcomputer(h,w):
    bmi = w / (h*h)
    bmi = int(bmi * 100) / 100
    return bmi

def main():
    data = []
    while True:
        input_data = input()

        if input_data == "-1": break
        height , weight = map(int,input_data.split())
        height /= 100
        weight *= 0.454
        if height < 0.5 or height > 2.5: 
            data.append("Input Height Error")
            continue
        if weight < 20 or weight > 300:
            data.append("Input Weight Error")
            continue
        bmi = BMIcomputer(height,weight)
        data.append(bmi)

    for i in range(len(data)):
        if type(data[i]) is float:
            if data[i] > 24: data[i] = "BMI too high"
            elif data[i] < 18.5: data[i] = "BMI too low"
            else: data[i] = f"{data[i]:.2f}"

    print(*data,sep="\n") 

if __name__ == "__main__":
    main()