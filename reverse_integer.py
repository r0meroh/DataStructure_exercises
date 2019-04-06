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