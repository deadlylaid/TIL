# def answer(a, b, c):
#     if b >= c:
#         return -1
#     end = 2100000001
#     start = 1
#     while True:
#         count = int((end + start) / 2)
#         if c * count - b * count == a:
#             count += 1
#             return count
#         elif c * count - b * count > a:
#             if end - count == 1:
#                 return count
#             else:
#                 end = count
#         elif c * count - b * count < a:
#             start = count
#
#
#
# a, b, c = map(int, input().split(' '))
# print(answer(a, b, c))


"""
고정비(A) 제작비(B) 단가(C)

고정비 + (제작비 * 판매 수) < (단가 * 판매 수)

A + (B * D) < C * D
A < (C * D) - (B * D)
A < (C - B) * D

고정비 < (단가 - 제작비) * 판매 수
"""


def answer(a, b, c):
    if b >= c:
        return -1
    return int((a / (c - b)) + 1)


a, b, c = map(int, input().split(' '))
print(answer(a, b, c))
