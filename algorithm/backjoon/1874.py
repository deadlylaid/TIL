number = int(input())

number_list = [x for x in range(1, number + 1)]
order_list = [int(input()) for _ in range(number)]

bucket = list()
previous_number = 0

result = list()

def run(number_list, order_list, bucket, previous_number):
    for i in order_list:
        while True:
            if i < previous_number:
                if i == bucket[-1]:
                    previous_number = i
                    bucket.pop()
                    result.append('-')
                    break
                else:
                    return 'NO'
            number = number_list.pop(0)
            if i > number:
                bucket.append(number)
                result.append('+')
            elif i == number:
                result.append('+')
                result.append('-')
                previous_number = i
                break
    return result

result = run(number_list, order_list, bucket, previous_number)

if isinstance(result, str):
    print(result)
else:
    for i in result:
        print(i)