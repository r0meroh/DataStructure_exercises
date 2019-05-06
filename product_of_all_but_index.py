
my_array = [1, 2, 3, 4 ]

def product_of(y):
    first_arr = []
    for nums in y:
        if first_arr:
            first_arr.append(first_arr[-1] * nums)
        else:
            first_arr.append(nums)
    print(first_arr)

    second_arr = []
    for nums in y:
        if second_arr:
            second_arr.append(second_arr[-1] * nums)
        else:
            second_arr.append(nums)
    second_arr = list(reversed(second_arr))
    print(second_arr)


    result = []

    for i in range(len(y)):
        if i ==0:
            result.append(second_arr[i])
        elif i == len(y):
            result.append(first_arr[i-1])
        else:
            result.append(first_arr[i-1] * second_arr[i+1])
    print(result)


print(my_array)


product_of(my_array)


