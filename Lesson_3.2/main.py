# def fun(a):
#     b = a.copy()
#     (b.sort())
#
#
#     print(b)
# c = [1,4,-1,5,-8,2]
# fun(c)
# lst = list()
# for i in range(len(a)-2):
#     if a[i] > 0 and  a[i+1]>0:
#         sum1 += a[i] + a[i+1]
#     elif a[i+1] < 0 and a[i+2]<0 :
#         lst.append(sum1)
#         sun1 = 0
#         sum1= a[i+1] + a[i+2]

# ex1
# lst = []
# s = 0
# def sun_range(start,end,s=0):
#     if start > end:
#         for i in range(end,start+1):
#             s+= i
#             # lst.append(i)
#             # c = sum(lst)
#         print(s)
#     if start < end:
#         for i in range(start, end + 1):
#             s+=i
#             # lst.append(i)
#             # c = sum(lst)
#         print(s)
# a = int(input())
# b = int(input())
#
# sun_range(a,b)
#ex2
# def ma(a,b,c):
#     if a >= b and a>=c:
#         print()
#     elif b >= a and b >= c:
#         print(b)
#     else:
#         print(c)
# ma(2,5,4)
#3ex
# def fun(a):
#     for i in range(1,11):
#         print(f"{a} * {i} = {i*a}")
# b = int(input())
# fun(b)
#ex4
# a = int(input())
# lst = []
# def fun(b):
#     for i in range(1,b+1):
#         if b % i == 0:
#             lst.append(i)
#     print(lst)
# fun(a)
#ex5
# d = {
#     'k1': 1,
#     'k2': 3,
#     'k3': 8,
#     'k4': 76,
#     'k5': 44,
#     'k6': 24
#
# }
# a = 1
# for v in d.values():
#     a *= v
# print(a)
#ex6
# a = [1,2,3,4,5,6]
# b = ["a","b","c","d","e","f"]
# d = {
#
#
# }
# for i in range(len(a)):
#     d[a[i]] = b[i]
#
# print(d)
#ex7
# a = ["a","aa","aaa","b","bb","bbb"]
# d = {
#
#
# }
# for i in range(len(a)):
#     d[a[i]] = a[i]
#
# print(d)
#ex8
a = "111133342215669"
lst = list(a)
def count_it(str):
    d = {
    }
    for i in lst:
        c = lst.count(i)
        if i not in d.keys():
            d[i]=c
    print(d)



count_it(a)









