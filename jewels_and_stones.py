"""
This exercise takes two strings and returns two integer. The first string defines what an object is and the second
string includes characters that are both deifned and non defined. The result is a quantity of defined characters
and non defined characters
"""

def j_n_s(string1,string2):
    s1 = 0
    s2 = 0
    jewels = list(string1)
    stones = list(string2)

    for x in range(len(jewels)):
        if(jewels[x]== stones.index(jewels[x])):
            s1+=s1

    return s1


print(j_n_s('gH','gGhhH'))