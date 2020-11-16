# this program takes in an array and returns a new array with the elements being the prodruct all of other elements but themselves
# brute force O(n^2)
def productSum (array):

    suffix = []



    for num in array:
        new_num = 0
        for nums in array:
            new_num += (num * nums )
        suffix.append(new_num)


    print(suffix)

    for num in range(len(suffix)):
        suffix[num] = suffix[num] / array[num]

    print(suffix)



def idealSolution(array):
    prefix_products = []
    for num in array:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products = []

    for num in reversed(array):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)

    result = []
    for i in range(len(array)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(array) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])

    print(result)




productSum([2,4,6])
idealSolution([2,4,6])
