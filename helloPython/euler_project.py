# if __name__ == '__main__':
#     flag = False
#     arr = []
#     for i in range(999, 100, -1):
#         for j in range(999, 100, -1):
#             a = [int(s) for s in str(i * j)]
#             if (a == a[::-1]):
#                 s = int("".join([str(s) for s in a]))
#                 arr.append(s)
#     arr.sort()
#     print("最小的值为：", arr[0])
#     print("最大的值为：", arr[len(arr)-1])
# import time
# start = time.time()
# def gcd(m, n):
#     if m < n:
#         m, n = n, m
#     while True:
#         m, n = n, m % n
#         if n == 0:
#             return m
# result = 2
# def lcd(m, n):
#     return m * n / gcd(m, n)
# for i in range(3, 21):
#     result = lcd(i, result)
# print(result)
# print(time.time() - start)
# python中的字节码产生方法dis()
# import dis
# def test():
#     i = 0
#     while 1:
#         i +=1
#         if i == 10000:
#             break
# if __name__ == '__main__':
#     dis.dis(test)
