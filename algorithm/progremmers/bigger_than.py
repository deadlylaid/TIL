def c(number):
    result = ''
    while number >= 2:
        result +=str(number%2)
        number //= 2
    result += str(number)
    return result[::-1]


def solution(n):
    n_q = c(n)

    number_of_n_q = n_q.count('1')

    while True:
        n+=1
        aa = c(n)
        if number_of_n_q == aa.count('1'):
            break

    return n