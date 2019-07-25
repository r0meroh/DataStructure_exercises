# take an array and find the smallest index out of order that will sort the
# array if moved x amount of times. return the inital index and how many what
# index it needs to move to in order to sort the array

def find_small_and_sort(an_array):
    left, right = None, None

    n = len(an_array)
    max_seen, min_seen = -float("inf"), float("inf")


    for i in range(n):
        max_seen = max(max_seen, an_array[i])
        if an_array[i] < max_seen:
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, an_array[i])
        if an_array[i] > min_seen:
            left = i

        return left, right


my_array = [3, 7, 5, 6, 9]

print(find_small_and_sort(my_array))

