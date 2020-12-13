def solution(people, limit):
    people.sort()

    count = 0

    start = 0
    last = len(people) - 1

    while start < last:
        count += 1

        result = people[last] + people[start]
        if result <= limit:
            start += 1
        last -= 1

    if start == last:
        count += 1
    return count