
# this program exercise makes a new "row" for each time an integer in an array
# is larger than the one that precedes it
# at the end, the program outputs how many roles were made

def solution(arr):
    arr = [int(i) for i in arr]
    print(arr)
    count = 0;
    for nums in range(len(arr)):
        if nums == 0:
            count += 1
            print('index zero')
        if arr[nums] > arr[nums -1]:
            count += 1
            print('increased count at: ')
            print(nums)
            # print(count)

    print('Number of rows created')
    print(count)


array_test = ['1', '5', '4', '3', '2', '11']
solution(array_test)