length = int(input("Input the length of series: "))
sum_num = 0
for i in range(1, length+1):
    number = i*2
    if i % 2 == 0:
        number = -number

    sum_num += number
    print(number)

print("Sum: ", sum_num)

