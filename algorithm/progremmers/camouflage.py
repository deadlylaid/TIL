def solution(clothes):
    answer = 1

    clothes_dict = {}

    for i in clothes:
        key = i[-1]
        if clothes_dict.get(key):
            clothes_dict[key] += len(i) - 1
        else:
            clothes_dict[key] = len(i) - 1

    cs = [v for i, v in clothes_dict.items()]

    # (옷의 수 + 1(해당 타입의 옷을 안입는 경우)) * n - 1(아무런 옷도 입지 않는 경우 제외)
    for i in cs:
        answer *= i + 1
    return answer - 1


"""
잘못된 코드

옷 [A,B,C,D] 가 각각 한 벌씩 있을 경우, [A, B, D] 조합을 구하지 못한다.
"""
import math


def solution(clothes):
    answer = 0

    clothes_dict = {}

    for i in clothes:
        key = i[-1]
        if clothes_dict.get(key):
            clothes_dict[key] += len(i) - 1
        else:
            clothes_dict[key] = len(i) - 1

    cs = [v for i, v in clothes_dict.items()]
    cs_len = len(cs)

    # 몇 개씩 조합할 지
    for i in range(1, cs_len):
        # 첫 번째 수가 무엇인지
        for ii, vv in enumerate(cs):
            for iii in range(1, cs_len):
                if ii + iii + i <= cs_len:
                    answer += vv * math.prod(cs[iii + ii:iii + ii + i])

    for i in cs:
        answer += i
    return answer
