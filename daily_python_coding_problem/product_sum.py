# this program takes in an array and returns a new array with the elements being the prodruct all of other elements but themselves
# brute force O(n^2)
def productSum (array):
    prefix = []
    suffix = []


    for num in array:

        prefix.append(num)

    for num in prefix:
        new_num = 0
        for nums in array:
            new_num += (num * nums )
        suffix.append(new_num)

    print(prefix)
    print(suffix)

    for num in range(len(suffix)):
        suffix[num] = suffix[num] / array[num]

    print(suffix)


productSum([2,4,6])
