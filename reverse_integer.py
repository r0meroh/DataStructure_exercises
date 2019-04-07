"""""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
# my original solution
"""""
class Solution(object):
    def reverse(self, x):
        # create a list to store integer in
        digit_to_string = []
        # insert each individual digit into an independent index
        for number in str(x):
            digit_to_string.append(number)
        # check for a single zero
        if len(digit_to_string) == 1:
            list_to_string = ''.join(digit_to_string)
            return list_to_string
        # if number is positive
        elif digit_to_string[0].isdigit() == True:
            # rearrange list backwards
            list_to_string = ''.join(digit_to_string[::-1])
            if list_to_string[0]=='0':
                list_to_string = list_to_string[1:]
        # if number is negative
        elif digit_to_string[0].isdigit() == False:
            #rearrange list backwards
            list_to_string = ''.join(digit_to_string[::-1])
            #check if there is a 0 as the first element
            if list_to_string[0]=='0':
                list_to_string = list_to_string[1:]
            # temp = "-"
            temp = list_to_string[-1]
            # recreate list with "-" in front
            list_to_string = temp + list_to_string[:-1]
        return list_to_string

# create object
problem_seven = Solution()
# execute function and print out result with a negative number
print(problem_seven.reverse(-1230))
# execute function and print out result with a positive number
print(problem_seven.reverse(98760))
# execute function with zero
print(problem_seven.reverse(0))
"""

# revised solution

class newSOlution(object):
    def reverse(self,x):
        negative_sum = False
        overflow = 0
        digit_list = []
        # check if original integer value is negative
        if (x < 0):
            negative_sum = True
            # multiply by negative one to turn positive, we will
            # add the negative back after reversal
            x = (x * -1)
        # only other condition is if integer is positive so we
        # leave it alone
        else:
            x = x
        # split up integer into single digits within a list
        x = str(x)
        for digit in x:
            digit_list.append(digit)
        # reverse list
        digit_list = digit_list[::-1]
        # check to see if negative needs to be added
        if negative_sum == False:
            final_digit = int(''.join(digit_list))
            return final_digit
        elif negative_sum == True:

            final_digit = ''.join(digit_list)
            final_digit = int(final_digit)
            final_digit = final_digit*-1
            return final_digit


my_number = -123
my_object = newSOlution()
print(my_object.reverse(my_number))


