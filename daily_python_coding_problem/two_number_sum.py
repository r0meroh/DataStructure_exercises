
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



if __name__ == '__main__':
    test = [1,2,3,4]
    print(two_number_sum(test, 5))
