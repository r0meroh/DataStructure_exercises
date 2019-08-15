"""
Given an array of integers, return indices of the two numbers such that they add up
to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""

def use_dictionary(an_array, number):
    possible_sums = []
    my_dict = {}

    for i in range(0,len(an_array)):

        sum_minus_number = number - an_array[i]

        if sum_minus_number in my_hash:
            possible_sums.append([an_array[i], sum_minus_number])
        my_dict[an_array[i]] = an_array[i]

    return possible_sums




def create_the_array():
    my_array = []
    input_from_user = None
    while(input_from_user != 'x'):
        print('please input a number for each array index. Press "x" when done')
        input_from_user = input()
        if(input_from_user!='x'):
            my_array.append(int(input_from_user))

    return my_array
def add_two(an_array, number):
    i = 0
    x = 0
    for j in range(len(an_array)):
       for k in range(len(an_array)):
           if((an_array[j] + an_array[k]) == number):
               i = j
               x = k

    return i,x

the_create_array = create_the_array()
print(the_create_array)
print('Please input a number that two indices of the array need to add up to:')
sum =int(input())
print(add_two(the_create_array,sum))
print(the_create_array[2])

print('using dictionary solution ')
print(use_dictionary(the_create_array,sum))

"""
    will incorporate a solution with a hashtable next
"""







