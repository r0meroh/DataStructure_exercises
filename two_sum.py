"""
Given an array of integers, return indices of the two numbers such that they add up
to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""
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
        if ((an_array[j] + an_array[j]+1) == number):
            i = j
            x = j+1
        else:
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