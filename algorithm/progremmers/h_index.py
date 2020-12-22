def solution(citations):
    answer = 0

    citations = sorted(citations)
    length = len(citations)

    idx = 0
    number = 0
    result = []

    while number <= length - idx:
        if number <= citations[idx]:
            result.append(number)
            number+=1
        elif number > citations[idx]:
            idx+=1
    answer = result[-1]
    return answer