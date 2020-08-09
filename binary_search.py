"""
 This program implements a simple binary search.
"""


def search(collection, target):
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2
        print('mid is currently: ' + str(mid))

        item = collection[mid]
        print('target is currently: ' + str(target))
        print(type(item))
        print('item is currently: ' + str(item))

        if target == item:
            return "found it at ", str(mid), " index"
        elif target < item:
            high = mid - 1
            print('high is currently: ' + str(high))
        else:
            low = mid + 1
            print('low is currently: ' + str(low))
    return -1 , "item not found in collection"


def main():
    my_list = [33,44,2222,11,66,333,222]
    my_list = sorted(my_list)
    print(my_list)
    print(search(my_list, 333))

if __name__ == '__main__':
    main()