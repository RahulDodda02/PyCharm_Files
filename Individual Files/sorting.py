import time
import random

size = 1000
lst = []
while len(lst) < size:
    lst.append(random.randint(-1*size, size))

def selection_sort(lst):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if lst[i] < lst[min_idx]:
                min_idx = i
        (lst[step], lst[min_idx]) = (lst[min_idx], lst[step])

def bubble_sort(lst):
    for iter_num in range(len(lst) - 1, 0, -1):
        for idx in range(iter_num):
            if lst[idx] > lst[idx + 1]:
                temp = lst[idx]
                lst[idx] = lst[idx + 1]
                lst[idx + 1] = temp


def binary_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_list = lst[:middle]
    right_list = lst[middle:]

    left_list = binary_sort(left_list)
    right_list = binary_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


start = time.time()
sel = lst
selection_sort(sel)
end = time.time()
print("Selection Sort time: ", end - start)


start = time.time()
bub = lst
bubble_sort(bub)
end = time.time()
print("Bubble sort time: ", end - start)


start = time.time()
bslst = binary_sort(lst)
end = time.time()
print("Binary sort time: ", end - start)

print(lst)