def solution(number, k):
    answer = []
    digit = len(number) - k
    for idx, num in enumerate(number):
        while True:
            if len(answer) == 0 or k == 0:
                break
            else:
                if answer[-1] < num:
                    answer.pop()
                    k -= 1
                else:
                    break
        answer.append(num)
    return ''.join(answer[:digit])

"""
잘못된 풀이
"""

# def solution(number, k):
#     answer = ''
#
#     fst = 0
#     x = k + 1
#
#     while x < len(number) + 1:
#         n_number = number[fst:x]
#         n = max(n_number)
#         answer += n
#         idx = number.index(n)
#         number = number.replace(n, '0', 1)
#         fst = idx + 1
#         x += 1
#
#     return answer


# def solution(number, k):
#     pasted_number = [x for x in number]
#
#     before_value = 0
#     for i in range(len(number)):
#         if i == 0:
#             before_value = int(number[i] + number[i + 1])
#         else:
#             if before_value <= int(number[i] + number[i + 1]):
#                 pasted_number[i - 1] = 'X'
#                 before_value = int(number[i] + number[i + 1])
#                 k -= 1
#             elif before_value > int(number[i] + number[i + 1]):
#                 pasted_number[i] = 'X'
#                 before_value = int(number[i - 1] + number[i + 1])
#                 k -= 1
#         if k == 0:
#             break
#
#     return ''.join(x for x in pasted_number if x != 'X')
#
# print(solution("1924", 2))
