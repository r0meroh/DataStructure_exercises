
# brute force O(n^2)
def two_number_sum(array, target):
    pairs = []
    for num in array:
        for element in array:
            if num != element and target == (num + element):
                if num not in pairs and element not in pairs:
                    new_pair = (num, element)
                    pairs.append(num)
                    pairs.append(element)


    return pairs


# solution with set O(n)
def two_sum_with_set(array, target):
    my_set = {}
    my_set = set(array)
    pairs = []
    sub = 0
    for num in array:
        sub = target - num
         # print(sub)
        if sub in my_set and sub not in pairs:
             # print(str(sub) + 'is in the set' + str(my_set))
            pairs.append(num)
            pairs.append(sub)
            my_set.remove(sub)

    return pairs


if __name__ == '__main__':
    test = [1,2,3,4]
    print(two_number_sum(test, 5))
    print(two_sum_with_set(test, 5))
    print(two_number_sum([], 2))
    print(two_sum_with_set([], 3))
