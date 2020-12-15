def cal(upper, down):
    result = [0,0,0,0]
    for i, v in enumerate(upper):
        for j, t in enumerate(down):
            if i != j and result[j] < v+t:
                result[j] = v+t
    return result

def solution(land):
    result = [0,0,0,0]
    for i in land:
        result = cal(result, i)

    return max(result)