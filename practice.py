# list = [1, 2, 3, 4, 5, 6, 7, "rohan"]
# l = [11, 22, 33]
# list.extend(l)
# print(list)
# list.append(l)
# print(list)

# s = "Rohan Chougule Sangli 416416"
# l = s[::-1]
# print(l)
#
# lst = list(s.split(" "))
# n_lst = lst[::-1]
# f_lst = " ".join(n_lst)
# print(f_lst)
#
#
# dic = {}
# for c in s:
#     k = dic.keys()
#     if c not in k:
#         dic[c] = 1
#     else:
#         dic[c] += 1
# print(dic)
#
# d_dup = []
# for i in s:
#     d_dup.append(i)
#
# s_lst = set(d_dup)
# final = list(s_lst)
# print(final)
#
# def decorator(fun):
#     def wrap():
#         val = fun()
#         val = val.title()
#         return val
#     return wrap
#
# @decorator
# def fun():
#     return 'rohan chougule'
#
# x= fun()
# print(x)
