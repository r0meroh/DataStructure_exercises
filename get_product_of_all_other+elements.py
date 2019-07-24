# this exercise reads a list and returns the product of all the
# elements except for the selected element and stores it into that element.
# example [ 1, 3, 5] will return [15, 5, 3]

# this function takes a single string and turns it into a list
def array_maker():
    print('enter values for the array. press enter to stop. ')
    # my_array = []
    input_from_user = [input()]
    input_from_user = input_from_user[0].split()
    input_from_user = [int(i) for i in input_from_user]
    print(input_from_user)
    print(type(input_from_user[0]))
    return input_from_user



def products(an_array):
    # generates preffix products
    prefix_products = []
    for numbers in an_array:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * numbers)
        else:
            prefix_products.append(numbers)

    # generating suffix products
    suffix_products = []
    for num in reversed(an_array):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # generate result fomr the total product of the pre and suffixes
    result = []
    for i in range(len(an_array)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(an_array) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])

    return result


my_array = array_maker()
print('printing out the array')
print(my_array)
print('going into the products function')
my_array = products(my_array)
print(my_array)