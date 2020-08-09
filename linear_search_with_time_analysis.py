"""
  This program searches for an item within a collection and returns how long it took to execute.
"""

import time

"""
  search_list takes in a list and a target to look for. Tries to return the index of the target within the list. 
  Throws a ValueError exception if the target is not found in the list.
"""
def search_list(list_given, target):
    try:
        return "value located at index: ", list_given.index(target)
    except ValueError:
        return -1 , "target not in collection"

""""
  the time functions set a marker when the function is called to assess how long the program runs for.
"""
def time_start():
    print(time.time())
    return time.time()

def time_stop():
    print(time.time())
    return time.time()

def main():
    start = time_start()

    my_list = [23,44,55,2,1]
    print(search_list(my_list,32))

    stop = time_stop()
    print(start - stop)


if __name__ == '__main__':
    main()

