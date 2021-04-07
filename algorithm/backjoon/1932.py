number = int(input())

pyramid = []

for _ in range(number):
    pyramid.append(list(map(int, input().split(' '))))

dynamic_list = []
for _ in range(number):
    dynamic_list.append([0]*(number+1))

for idx1, i in enumerate(pyramid):
    for idx2, j in enumerate(i):
        if idx1 == 0:
            dynamic_list[idx1][idx2] = j
        else:
            if idx2 == 0:
                dynamic_list[idx1][idx2] = dynamic_list[idx1-1][idx2] + j
            elif idx2 == idx1:
                dynamic_list[idx1][idx2] = dynamic_list[idx1-1][idx2-1] + j
            else:
                dynamic_list[idx1][idx2] = max([dynamic_list[idx1-1][idx2-1], dynamic_list[idx1-1][idx2]]) + j

print(max(dynamic_list[-1]))