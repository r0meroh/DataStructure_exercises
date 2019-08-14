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
    print(s1)
    print(s2)
    for x in range(len(jewels)):
        if jewels[x] in stones:
            print(jewels[x])
            s1 = s1 + 1
            print(stones)




    return s1, s2

def cheeky(string1, string2):
    return sum( each in string1 for each in string2), len(string2)

print(j_n_s('gh','gGhhH'))

print('cheeky solution')
print(cheeky('gh','gGghHH'))