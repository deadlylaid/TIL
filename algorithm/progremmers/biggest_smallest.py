def solution(s):
    s = [int(x) for x in s.split(' ')]

    min_v = min(s)
    max_v = max(s)
    answer = str(min_v) + ' ' + str(max_v)
    return answer