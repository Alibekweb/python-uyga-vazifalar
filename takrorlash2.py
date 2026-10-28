# t = ["olma", "anor ", "nok"]
# t2 = tuple(t)
# print(t2)

# a = (1,2,3)
# b = (5,6,7)
# c = list(a)
# d = list(b)
# e = c + d
# print(e)

# a = [1, 3, ("olma", 5, 8), [1, 5]]
# print(a[2][0])

# from collections import Counter
# my_tuple = ('olma', 'banan', 'olma', 'uzum', 'banan', 'olma')
# freq_dict = dict(Counter(my_tuple))
# print(freq_dict)

# a = ["olma", "anor", "nok", "uzum"]
# b = tuple(a[1::2])
# print(b)

# list1 = [5, 2, 9, 1, 7]
# list2 = [2, 7, 3, 5, 8]
# common_tuple = tuple(sorted(set(list1) & set(list2)))
# print(common_tuple) 

# words = ['python', 'react', 'javascript', 'html', 'css']

# result = [(word, len(word)) for word in words]

# print(result)

# def remove_last_element(lst):
#     return tuple(lst[:-1])

# my_list = [10, 20, 30, 40]
# result = remove_last_element(my_list)

# print(result)

# a = (1,2,3,4,5,6,7)
# list = []
# for i in a:
#     if i%2 == 0:
#         list.append(i)
# print(list)

# my_list = [10, 20, 30, 40, 50, 60]

# even_index_tuple = tuple(my_list[::2])
# odd_index_tuple = tuple(my_list[1::2])

# print(even_index_tuple)
# print(odd_index_tuple)

# a = [10, 5, 20, 3, 15]
# b = a.index(max(a))
# c = a.index(min(a))
# a[b], a[c] = a[c], a[b]
# print(a)

# t = (1, 2, 3, 4, 5, 6, 7, 8)
# step = 2
# res = list(t[::step])
# print(res)

# t1 = (5, 2, 9)
# t2 = (1, 7, 3)
# res = sorted(t1 + t2)
# print(res)

# lst = [1, 2, 3, 4]
# res = [sum(lst[:i+1]) for i in range(len(lst))]
# print(res)

# s = "python"
# res = tuple(s)
# print(res)

# t = (2, 4, 6, 8, 10)
# avg = sum(t) / len(t)
# res = [x for x in t if x > avg]
# print(res)

# lst = [1, 2, 3, 4, 5]
# k = 2
# k %= len(lst)
# res = lst[-k:] + lst[:-k]
# print(res)

# l1 = [1, 2]
# l2 = ['a', 'b']
# res = [(x, y) for x in l1 for y in l2]
# print(res)

# t = (1, 2, 3, 4, 5, 6)
# res = list(x for x in t if x > 3)
# print(res)

