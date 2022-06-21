
l1 = eval(input("Enter a List of Elements: "))
print(l1)
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)

word = input("Enter a word: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
word_vowels = []
results = {}
for each_letter in word:
    if each_letter in vowels:
        count += 1
        word_vowels.append(each_letter)
        results[each_letter] = results.get(each_letter, 0) + 1      #look at later
print(count)
print(word_vowels)
for k, v in sorted(results.items()):
    print(k, "is present", v, " times")


n = int(input('enter num emps: '))
employees = {}
for i in range(n):
    name = input('name: ')
    sal = input('salary: ')
    employees[name] = sal
while True:
    name = input('emp name: ')
    sal = employees.get(name, -1)
    if sal == -1:
        print('emp dont exist')
    else:
        print('sal employee: ', sal)
    choice = input('continue checking sals? : ')
    if choice == 'No':
        break

chars = 'aaahhAAHaaa'
count = {}
for each_char in chars:
    if each_char in count.keys():
        count[each_char] += 1
    else:
        count[each_char] = 1
for k, v in count.items():
    print('{} = {} times ' . format(k,v))


def mult(a = 0, b = 0):
    return a*b
print(mult())

from functools import reduce
l = [4, 8, 12, 10]
result = reduce(lambda x,y:x+y, l)
print(result)

class Solution(object):
    def twoCitySchedCost(cost):

        #:type costs: List[List[int]]
        #:rtype: int

        costs = cost
        aCount = 0
        bCount = 0
        tot_cost = 0
        aMin = 1000
        bMin = 1000
        d = [0, ]
        for each_pair in costs:
            if each_pair[0] <= each_pair[1]:
                aCount += 1
                tot_cost += each_pair[0]
            else:
                bCount += 1
                tot_cost += each_pair[1]
        while (aCount != bCount):
            if aCount < bCount:
                for each_a in costs:
                    if 0 < (each_a[0] - each_a[1]) < aMin and (each_a[0] - each_a[1]) not in d:
                        aMin = each_a[0] - each_a[1]
                tot_cost += aMin
                aCount += 1
                bCount -= 1
                d.append(aMin)
            else:
                for each_b in costs:
                    if 0 < (each_b[1] - each_b[0]) < bMin and (each_b[1] - each_b[0]) not in d:
                        bMin = each_b[1] - each_b[0]
                tot_cost += bMin
                bCount += 1
                aCount -= 1
                d.append(bMin)
        return (tot_cost)

    twoCitySchedCost(cost = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])



l = [3, 65, 12, 5, 31]
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 16]
ans = []
for each_val in r:
    if each_val not in l:
        ans.append(each_val)
print(ans)