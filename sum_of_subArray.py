# this program will create an array and return the sum of the indices of a sub-array

def create_Array():
    # create an array from user input
    my_array = [input("enter mixed values to create array")]
    my_array = my_array[0].split()
    # check what datatype is in list
    # print statement to test code
    # print(type(my_array[0]))
    # parse string list into integers
    my_array = [int(i) for i in my_array]
    # print(my_array)
    # print(type(my_array[0]))
    return my_array


def get_Sub_Array(an_array):
    # declare a temp arrays
    neg_sub_arr = []
    pos_sub_arr = []
    for x in range(len(an_array)):
        if an_array[x] < 0:
            neg_sub_arr.append(an_array[x])
        if an_array[x] > 0:
            pos_sub_arr.append(an_array[x])
    # these are print statements to test code
    # print(pos_sub_arr)
    # print(neg_sub_arr)
    return pos_sub_arr, neg_sub_arr

# funstion that adds the sum of indices in an array
def find_sum_of_arr(an_array):
    sum = 0
    for i in range(len(an_array)):
        sum += an_array[i]

    print(sum)


# main function
def main():
    the_array = create_Array()
    first_arr, second_arr = get_Sub_Array(the_array)
    print("sum of first sub array: ")
    find_sum_of_arr(first_arr)
    print("sum of second sub array: ")
    find_sum_of_arr(second_arr)



# program execution
if __name__ == "__main__":
    main()