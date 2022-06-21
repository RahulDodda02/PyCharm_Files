import random
import time

# comparison of Binary search to Naive search
# Naive Search: Scans the list in order until wanted element is found
# Binary Search: Sorts and continually splits the list until wanted element is found
def naive_search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i
    return -1

def binary_search(elements, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(elements) - 1
    if high < low:
        return -1

    mid = (low + high) // 2

    if elements[mid] == target:
        return mid
    elif elements[mid] > target:
        return binary_search(elements, target, low, mid - 1)
    else:
        return binary_search(elements, target, mid + 1, high)

if __name__ == '__main__':
    # print(naive_search([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 24))
    # print(binary_search([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 98))
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")