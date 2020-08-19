"""
 This program implements a simple binary search.
"""

def search(list_ob, target):
    high = len(list_ob)-1
    low = 0
    list_ob = sorted(list_ob)

    while low <= high:
        mid = (low + high) //2
        if target == list_ob[mid]:
            return 'target found at index', mid
        if target > list_ob[mid]:
            low = mid + 1
        if target < list_ob[mid]:
            high = mid -1

    return 'target not in list', -1


def main():
    my_list = [33,44,2222,11,66,333,222]
    my_list = sorted(my_list)
    print(my_list)
    print(search(my_list, 333))

if __name__ == '__main__':
    main()